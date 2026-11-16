# Descripcion: Interfaz visual de la simulacion de agentes aspiradores con SolaraViz.
# Autores: Luis Alejandro Olvera Hernández (A01802127) y Pablo Alejandro Ortiz Montes (A01802689)
# Fecha de modificacion: 16/11/2026

from mesa.visualization import SolaraViz, SpaceRenderer, make_plot_component
from mesa.visualization.components import AgentPortrayalStyle, PropertyLayerStyle

from model import Habitacion


# Define la apariencia de cada aspiradora en la cuadrícula.
# Parametros: agent (aspiradora que se va a representar).
# Retorna: estilo visual del agente.
def agentPortrayal(agent):
    return AgentPortrayalStyle(color="tab:blue", marker="o", size=60)


# Define la apariencia de la capa que representa la suciedad.
# Parametros: layer (capa de propiedades de la cuadrícula).
# Retorna: estilo visual de la capa de suciedad o None si no corresponde.
def propertyLayerPortrayal(layer):
    if layer.name == "suciedad":
        return PropertyLayerStyle(
            color="saddlebrown", alpha=0.6, colorbar=False
        )
    return None


# Mantiene la misma escala horizontal y vertical en la visualizacion.
# Parametros: ax (eje de Matplotlib).
# Retorna: None.
def postProcess(ax):
    ax.set_aspect("equal")


# La semilla se mantiene fija en 42 para repetir la misma suciedad inicial.
# No modificarla entre las cinco configuraciones manuales.
modelParams = {
    "rng": 42,
    "M": {
        "type": "SliderInt", "value": 10, "label": "Ancho (M)",
        "min": 3, "max": 30, "step": 1,
    },
    "N": {
        "type": "SliderInt", "value": 10, "label": "Alto (N)",
        "min": 3, "max": 30, "step": 1,
    },
    "numAgentes": {
        "type": "SliderInt", "value": 5, "label": "Agentes",
        "min": 1, "max": 30, "step": 1,
    },
    "pctSucias": {
        "type": "SliderFloat", "value": 0.3, "label": "Proporcion de celdas sucias",
        "min": 0.0, "max": 1.0, "step": 0.05,
    },
    "maxPasos": {
        "type": "SliderInt", "value": 1000, "label": "Tiempo maximo (pasos)",
        "min": 100, "max": 5000, "step": 100,
    },
}

modelo = Habitacion()

renderer = (
    SpaceRenderer(modelo, backend="matplotlib")
    .setup_agents(agentPortrayal)
    .setup_propertylayer(propertyLayerPortrayal)
)
renderer.draw_propertylayer()
renderer.draw_agents()
renderer.post_process = postProcess


graficaLimpias = make_plot_component("Celdas limpias (%)")
graficaMovimientos = make_plot_component("Movimientos totales")
graficaTiempo = make_plot_component("Tiempo transcurrido")

page = SolaraViz(
    modelo,
    renderer,
    components=[graficaLimpias, graficaMovimientos, graficaTiempo],
    model_params=modelParams,
    name="Aspiradoras",
)
page
