
import mesa

from mesa.discrete_space import CellAgent, OrthogonalMooreGrid

from mesa.visualization import (
    SolaraViz,
    SpaceRenderer,
    make_plot_component,
)

from mesa.visualization.components import AgentPortrayalStyle


# ----------------------------------------
# 1. AGENT
# ----------------------------------------

class SpaceMoneyAgent(CellAgent):
    """An agent that moves and exchanges money."""

    def __init__(self, model, cell):
        super().__init__(model)

        self.cell = cell
        self.wealth = 1

    def move(self):
        """Move to a random neighboring cell."""
        self.cell = self.cell.neighborhood.select_random_cell()

    def give_money(self):
        """Give one unit of wealth to another agent in the same cell."""

        cellmates = [
            agent for agent in self.cell.agents
            if agent is not self
        ]

        if self.wealth > 0 and cellmates:
            other_agent = self.random.choice(cellmates)
            other_agent.wealth += 1
            self.wealth -= 1


# ----------------------------------------
# 2. GINI COEFFICIENT
# ----------------------------------------

def compute_gini(model):
    agent_wealths = [
        agent.wealth for agent in model.agents
    ]

    x = sorted(agent_wealths)
    n = model.num_agents

    B = sum(
        xi * (n - i)
        for i, xi in enumerate(x)
    ) / (n * sum(x))

    return 1 + (1 / n) - 2 * B


# ----------------------------------------
# 3. MODEL
# ----------------------------------------

class DataMoneyModel(mesa.Model):

    def __init__(self, n=50, width=10, height=10, rng=None):
        super().__init__(rng=rng)

        self.num_agents = n

        # Create the grid
        self.grid = OrthogonalMooreGrid(
            (width, height),
            torus=True,
            random=self.random
        )

        # Data collector
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Gini": compute_gini
            },
            agent_reporters={
                "Wealth": "wealth"
            }
        )

        # Create agents
        SpaceMoneyAgent.create_agents(
            self,
            n,
            self.random.choices(
                self.grid.all_cells.cells,
                k=n
            )
        )

    def step(self):
        self.datacollector.collect(self)

        self.agents.shuffle_do("move")
        self.agents.do("give_money")


# ----------------------------------------
# 4. AGENT VISUALIZATION
# ----------------------------------------

def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color="orange",
        size=50,
        marker="o"
    )


# ----------------------------------------
# 5. INITIAL MODEL
# ----------------------------------------

model = DataMoneyModel(
    n=50,
    width=10,
    height=10,
    rng=42
)


# ----------------------------------------
# 6. SPACE RENDERER
# ----------------------------------------

renderer = (
    SpaceRenderer(
        model=model,
        backend="matplotlib"
    )
    .setup_structure(
        color="black",
        alpha=0.2
    )
    .setup_agents(agent_portrayal)
    .render()
)

# ----------------------------------------
# 7. MODEL PARAMETERS
# ----------------------------------------

model_params = {
    "n": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of agents",
        "min": 10,
        "max": 100,
        "step": 1
    },
    "width": 10,
    "height": 10
}


# ----------------------------------------
# 8. DATA VISUALIZATION
# ----------------------------------------

GiniPlot = make_plot_component("Gini")


# ----------------------------------------
# 9. SOLARA DASHBOARD
# ----------------------------------------

page = SolaraViz(
    model,
    renderer,
    components=[GiniPlot],
    model_params=model_params,
    name="Boltzmann Wealth Model"
)

page