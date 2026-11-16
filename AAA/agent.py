from mesa.discrete_space import CellAgent

Movimientos = [(-1, -1), (-1, 0), (-1, 1),
               ( 0, -1),          ( 0, 1),
               ( 1, -1), ( 1, 0), ( 1, 1)]


class Aspiradora(CellAgent):
    def __init__(self, model, cell):
        super().__init__(model)
        self.cell = cell
        self.movimientos = 0

    def step(self):
        coord = self.cell.coordinate  
        if coord in self.model.sucias:
            self.model.sucias.remove(coord)
            self.cell.suciedad = 0 
        else:
            x, y = self.random.choice(Movimientos)
            nueva = (coord[0] + x, coord[1] + y)

            if 0 <= nueva[0] < self.model.M and 0 <= nueva[1] < self.model.N:
                self.cell = self.model.grid[nueva]
                self.movimientos += 1