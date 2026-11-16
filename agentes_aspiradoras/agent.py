# Descripcion: Define el comportamiento de los robots aspiradores.
# Autores: Luis Alejandro Olvera Hernández (A01802127) y Pablo Alejandro Ortiz Montes (A01802689)
# Fecha de modificacion: 16/11/2026

from mesa.discrete_space import CellAgent


# Direcciones posibles de movimiento: las ocho celdas vecinas.
MOVIMIENTOS = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1),  (1, 0),  (1, 1)]


class Aspiradora(CellAgent):
    """Agente reactivo que aspira o se mueve segun su celda actual."""

    # Inicializa la aspiradora en la celda indicada.
    # Parametros: model (habitacion a la que pertenece), cell (celda inicial).
    # Retorna: None.
    def __init__(self, model, cell):
        super().__init__(model)
        self.cell = cell
        self.movimientos = 0

    # Ejecuta una accion: aspira si la celda esta sucia; si no, intenta moverse.
    # Parametros: ninguno.
    # Retorna: None. Actualiza la celda y el contador de movimientos cuando avanza.
    def step(self):
        coordenada = self.cell.coordinate

        if coordenada in self.model.sucias:
            self.model.sucias.remove(coordenada)
            self.cell.suciedad = 0
        else:
            cambioX, cambioY = self.random.choice(MOVIMIENTOS)
            nuevaCoordenada = (
                coordenada[0] + cambioX,
                coordenada[1] + cambioY
            )

            if (0 <= nuevaCoordenada[0] < self.model.M
                    and 0 <= nuevaCoordenada[1] < self.model.N):
                self.cell = self.model.grid[nuevaCoordenada]
                self.movimientos += 1
