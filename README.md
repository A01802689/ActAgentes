# Actividad Agentes Aspiradoras

## Información académica

**Materia:** Modelación de sistemas multiagentes con gráficas computacionales (Gpo 301)

**Autores:**
- Luis Alejandro Olvera Hernández
- Pablo Alejandro Ortiz Montes

## Descripción

Implementación de un sistema multiagente de limpieza utilizando Python y Mesa. El proyecto simula una habitación con diferentes cantidades de aspiradoras que se desplazan de manera aleatoria y limpian las celdas sucias.

## Estructura del repositorio

```text
ActAgentes/
│
├── agentes_aspiradoras/
│   ├── agent.py
│   ├── app.py
│   └── model.py
│
├── tutorial/
│   ├── agent.py
│   ├── app.py
│   ├── model.py
│   └── money_model.ipynb
│
├── Agentes Aspiradoras.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

## Descripción de los archivos

La carpeta `agentes_aspiradoras` contiene la implementación de nuestra actividad:

- **agent.py:** Define el comportamiento de las aspiradoras. Cada agente puede limpiar una celda sucia o desplazarse aleatoriamente hacia alguna de las ocho celdas vecinas.
- **model.py:** Define el modelo de simulación, incluyendo la habitación, la generación de suciedad, la creación de agentes y la recopilación de estadísticas.
- **app.py:** Configura la visualización interactiva del modelo mediante SolaraViz, permitiendo ejecutar y observar la simulación.

La carpeta `tutorial` contiene los archivos y el notebook desarrollados durante el tutorial de Mesa, que utilizamos como referencia para nuestra implementación.

Otros archivos:

- **Agentes Aspiradoras.pdf:** Documento con la configuración experimental, los resultados, el análisis y las conclusiones de la actividad.
- **requirements.txt:** Contiene las dependencias necesarias para ejecutar el proyecto.
- **.gitignore:** Especifica los archivos y carpetas que Git debe ignorar.

## Requisitos

- Python 3 instalado.
- Dependencias especificadas en `requirements.txt`.

## Instalación y ejecución

Los siguientes comandos deben ejecutarse desde la carpeta raíz del repositorio.

**1. Crear un entorno virtual:**

```powershell
python -m venv envModel
```

**2. Activar el entorno virtual:**

```powershell
.\envModel\Scripts\Activate.ps1
```

**3. Instalar las dependencias:**

```powershell
pip install -r requirements.txt
```

**4. Entrar a la carpeta de la actividad:**

```powershell
cd agentes_aspiradoras
```

**5. Ejecutar la aplicación:**

```powershell
solara run app.py
```

Al ejecutar el comando, Solara iniciará un servidor local. Abre en el navegador la dirección que aparecerá en la terminal, normalmente `http://localhost:8765`.

## Visualización de la simulación

La aplicación presenta un entorno interactivo dividido en dos secciones:

**Controles y parámetros:**

- Play Interval: velocidad de ejecución de la simulación.
- Render Interval: frecuencia de actualización de las gráficas.
- Reset: reinicia la simulación.
- Play/Pause: permite iniciar o detener la ejecución.
- Step: avanza un paso de simulación.
- Ancho y alto: dimensiones de la habitación.
- Agentes: cantidad de aspiradoras.
- Proporción de celdas sucias: porcentaje inicial de suciedad.
- Tiempo máximo: límite de pasos de la simulación.

**Visualizaciones:**

- Habitación: muestra la distribución de los agentes dentro de la cuadrícula.
- Porcentaje de celdas limpias: muestra cómo aumenta la limpieza conforme avanza la simulación.
- Movimientos totales: muestra la cantidad acumulada de desplazamientos realizados por las aspiradoras.
- Tiempo transcurrido: representa los pasos ejecutados durante la simulación.

Los parámetros pueden modificarse para observar cómo cambia el comportamiento del sistema al utilizar diferentes cantidades de aspiradoras y condiciones iniciales.

## Objetivo

Analizar cómo la cantidad de agentes influye en el rendimiento de un sistema multiagente de limpieza, considerando el tiempo necesario para completar la tarea, el porcentaje final de celdas limpias y el número total de movimientos realizados.