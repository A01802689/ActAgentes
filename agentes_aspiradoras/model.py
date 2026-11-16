# Descripcion: Crea la habitacion, administra las aspiradoras y recopila estadisticas.
# Autores: Luis Alejandro Olvera Hernández (A01802127) y Pablo Alejandro Ortiz Montes (A01802689)
# Fecha de modificacion: 16/11/2026

import mesa
from mesa.discrete_space import OrthogonalMooreGrid

from agent import Aspiradora


class Habitacion(mesa.Model):
    """Modelo de una habitacion con celdas limpias y sucias."""

    # Inicializa la habitacion, distribuye la suciedad y crea las aspiradoras.
    # Parametros: M y N (dimensiones), numAgentes (cantidad de robots),
    # pctSucias (proporcion sucia entre 0 y 1), maxPasos (limite de pasos),
    # rng (semilla para repetir la misma distribucion inicial).
    # Retorna: None.
    def __init__(self, M=10, N=10, numAgentes=5, pctSucias=0.3,
                 maxPasos=1000, rng=42):
        super().__init__(rng=rng)

        self.M = M
        self.N = N
        self.numAgentes = numAgentes
        self.pctSucias = pctSucias
        self.maxPasos = maxPasos

        self.grid = OrthogonalMooreGrid(
            (M, N), torus=False, random=self.random
        )
        self.grid.create_property_layer("suciedad", default_value=0, dtype=int)

        todasLasCeldas = [celda.coordinate for celda in self.grid.all_cells]
        cantidadSucias = int(len(todasLasCeldas) * pctSucias)
        self.sucias = set(self.random.sample(todasLasCeldas, cantidadSucias))

        for coordenada in self.sucias:
            self.grid[coordenada].suciedad = 1

        # Se conserva la coordenada (1, 1) utilizada en la propuesta original.
        Aspiradora.create_agents(
            self, numAgentes, cell=self.grid[(1, 1)]
        )

        self.tiempoLimpieza = 0 if not self.sucias else None
        self.running = bool(self.sucias)

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Celdas limpias (%)": lambda modelo: modelo.porcentajeLimpias(),
                "Movimientos totales": lambda modelo: modelo.movimientosTotales(),
                "Tiempo transcurrido": lambda modelo: modelo.steps,
            }
        )
        self.datacollector.collect(self)

    # Avanza un paso y detiene el modelo al limpiar todo o alcanzar maxPasos.
    # Parametros: ninguno.
    # Retorna: None. Actualiza tiempoLimpieza solo si se limpiaron todas las celdas.
    def step(self):
        if self.running:
            self.agents.shuffle_do("step")

            if not self.sucias:
                self.tiempoLimpieza = self.steps
                self.running = False
            elif self.steps >= self.maxPasos:
                self.running = False

            self.datacollector.collect(self)

    # Calcula el porcentaje de celdas limpias en la habitacion.
    # Parametros: ninguno.
    # Retorna: porcentaje de celdas limpias entre 0 y 100.
    def porcentajeLimpias(self):
        totalCeldas = self.M * self.N
        return 100 * (totalCeldas - len(self.sucias)) / totalCeldas

    # Suma los movimientos realizados por todas las aspiradoras.
    # Parametros: ninguno.
    # Retorna: numero total de movimientos exitosos.
    def movimientosTotales(self):
        return self.agents.agg("movimientos", sum)
