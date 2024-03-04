# Proyecto de Análisis de Datos

Este proyecto está diseñado para analizar el rendimiento de un sistema computacional a través de diversas configuraciones y parámetros. Utiliza datos obtenidos de simulaciones para examinar el tiempo de ejecución de procesos bajo diferentes condiciones.
Si quiere cambiar o generar nuevos archivos, se utiliza el analisis.py. En este se encuentra la seed para el módulo de random, esto presentará nuevos resultados. 
Asimismo, en el main se imprimen en la consola los datos estadísticos, pero también se encuentran archivos xlsx en la carpeta Data. 

## Descripción del Proyecto

El proyecto consta de un conjunto de clases y funciones que permiten analizar y visualizar los datos obtenidos de las simulaciones del sistema computacional. A continuación, se detallan las principales características del proyecto:

### Clase `Analisis`

La clase `Analisis` es la principal responsable de cargar, procesar y analizar los datos obtenidos de las simulaciones. Esta clase incluye los siguientes métodos:

- `stats_intervalos()`: Calcula y muestra las estadísticas de tiempo de ejecución para distintos intervalos de instrucciones.
- `stats_RAM200()`: Calcula y muestra las estadísticas de tiempo de ejecución para procesos con 200 de RAM.
- `stats_dobleCPU()`: Calcula y muestra las estadísticas de tiempo de ejecución para procesos con doble CPU.

### Métodos de Visualización

El proyecto incluye métodos de visualización para representar los resultados de manera gráfica. Estos métodos generan gráficos de barras que muestran el tiempo promedio de ejecución y la desviación estándar para diferentes configuraciones de procesos y recursos.

## Uso del Proyecto

Para utilizar el proyecto, sigue estos pasos:

1. Asegúrate de tener instaladas las bibliotecas necesarias, como pandas, numpy y matplotlib.
2. Ejecuta el archivo principal del proyecto para iniciar la interfaz de usuario.
3. Selecciona las estadísticas que deseas observar: tiempo con distintos intervalos de instrucciones, tiempo de procesos con 200 de RAM o tiempo con doble CPU.
4. Observa los resultados presentados y realiza el análisis correspondiente.

## Archivos del Proyecto

- `analisis.py`: Contiene la implementación de la clase `Analisis` y sus métodos.
- `Data/`: Carpeta que contiene los archivos CSV generados por las simulaciones.
- `README.md`: Documentación del proyecto en español.


