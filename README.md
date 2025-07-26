# SufCactus.py - Visualizador de Cactus de Sufijo en Tkinter

Este proyecto es una aplicación gráfica en Python que permite visualizar y analizar el cactus de sufijo de un string, usando dos alternativas de construcción. Está diseñado para facilitar la comprensión de estructuras de sufijos en cadenas, útil en bioinformática, teoría de la computación y análisis de textos.

## Características

- Interfaz gráfica con Tkinter.
- Permite ingresar el string manualmente o cargarlo desde un archivo `.txt`.
- Visualización gráfica del cactus de sufijo usando dos alternativas:
  - Alternativa 1: Construcción basada en ramas padre.
  - Alternativa 2: Construcción basada en sufijos.
- Tabla de profundidades de sufijos.
- Validación de entrada (sin espacios, termina en `$`).
- Exporta el resultado a `resultado.txt`.
- Tooltips explicativos en los campos y botones.

## Requisitos

- Python 3.x
- numpy

Instala las dependencias con:

```
pip install numpy
```

## Uso

1. Ejecuta el script:
   ```
   python SufCactus.py
   ```
2. Ingresa el string en el campo de texto (sin espacios y terminando en `$`), o usa el botón "Cargar archivo" para cargarlo desde un `.txt`.
3. Haz clic en "Alternativa 1" o "Alternativa 2" para visualizar el cactus de sufijo.
4. Usa "Tabla de Profundidad" para ver la profundidad de cada sufijo.
5. "Computar y guardar" ejecuta ambas alternativas y guarda el resultado en `resultado.txt`.

## Estructura de archivos

- `SufCactus.py`: Script principal de la aplicación.
- `resultado.txt`: Archivo de salida generado al guardar resultados.

## Notas

- El string debe estar en mayúsculas, sin espacios y terminar con `$`.
- El archivo de entrada debe contener una sola línea de texto válida.
- La interfaz está optimizada para Linux Mint, pero funciona en cualquier sistema con Python y Tkinter.
