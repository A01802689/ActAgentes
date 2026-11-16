import mesa
from mesa.discrete_space import OrthogonalMooreGrid

from agent import Aspiradora


class Habitacion(mesa.Model):
    def __init__(self, M=10, N=10, num_agentes=5, pct_sucias=0.3, rng=None):
        super().__init__(rng=rng)
        self.M = M
        self.N = N

        self.grid = OrthogonalMooreGrid((M, N), torus=False, random=self.random)
        self.grid.create_property_layer("suciedad", default_value=0, dtype=int)

        todas = [celda.coordinate for celda in self.grid.all_cells]
        cantidad = int(len(todas) * pct_sucias)
        self.sucias = set(self.random.sample(todas, cantidad))
        for coord in self.sucias:
            self.grid[coord].suciedad = 1 

        Aspiradora.create_agents(self, num_agentes, cell=self.grid[(1, 1)])

        self.tiempo_limpieza = 0 if not self.sucias else None

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Celdas limpias (%)": lambda m: m.porcentaje_limpias(),
                "Movimientos totales": lambda m: m.movimientos_totales(),
            }
        )
        self.datacollector.collect(self)

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)

        if not self.sucias:
            self.tiempo_limpieza = self.steps
            self.running = False

    def porcentaje_limpias(self):
        total = self.M * self.N
        return 100 * (total - len(self.sucias)) / total

    def movimientos_totales(self):
        return self.agents.agg("movimientos", sum)