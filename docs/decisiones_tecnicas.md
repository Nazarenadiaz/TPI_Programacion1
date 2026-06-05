# Decisiones técnicas

**Gestión de Datos de Países**.

---

## 1. Versión de Python

- **Intérprete oficial del proyecto:** Python **3.12**.
- Motivo: versión estable, ampliamente soportada y compatible con las características usadas en la materia.
- No se usan características experimentales ni específicas de versiones más nuevas.

## 2. Persistencia: archivo CSV

- Los datos se persisten en un único archivo CSV: `data/paises.csv`.
- Formato con cabecera `nombre,poblacion,superficie,continente`.
- Lectura y escritura con el módulo estándar `csv` (sin librerías externas).
- Codificación de archivo: **UTF-8**, para soportar tildes y caracteres como `América`, `África`, `Japón`.
- La ruta al CSV se calcula a partir de la ubicación del módulo (`__file__`), no del directorio de trabajo. Así el programa funciona ejecutado desde cualquier carpeta con `python src/main.py`.

## 3. Modelo de datos: lista de diccionarios

- Cada país se representa como un `dict` con cuatro claves:
  - `nombre` (str)
  - `poblacion` (int)
  - `superficie` (int)
  - `continente` (str)
- La colección de países es una `list` de esos `dict`.
- Justificación:
  - Coincide con las estructuras enseñadas en Programación 1 (listas y diccionarios).
  - Es el modelo más simple y explicable en el video.
  - Se mapea directamente a las filas del CSV.

## 4. Estructura de carpetas: `src/`, `data/`, `docs/`

- **`src/`** contiene todo el código fuente Python.
- **`data/`** contiene el dataset (`paises.csv`) y cualquier futuro archivo de datos.
- **`docs/`** contiene toda la documentación: consigna oficial, rúbrica de evaluación, decisiones técnicas, objetivo de nota máxima e informe PDF final.
- La raíz queda limpia: `README.md`, `.gitignore`, `PLAN_DESARROLLO.md` y las tres carpetas.
- Justificación:
  - Separación clara entre código, datos y documentación.
  - Facilita la lectura del repositorio en GitHub
  - Coherente con los criterios de la rúbrica (modularidad, repositorio organizado).

## 5. Sin librerías externas

- Solo se usan módulos de la biblioteca estándar de Python (`csv`, `os`, etc.).
- No hay `requirements.txt` ni instalación de paquetes.
- Justificación:
  - Restricción académica.
  - Asegura que el proyecto corre con cualquier instalación limpia de Python 3.12.
  - Hace la demo del video reproducible sin pasos de setup.

## 6. Sin clases, salvo necesidad estricta

- El proyecto se modela exclusivamente con **funciones**, **listas** y **diccionarios**.
- No se definen clases propias.
- Justificación:
  - El programa de Programación 1 prioriza estructuras de datos y funciones.
  - El dominio (un país con cuatro atributos) se cubre perfectamente con un `dict`.
  - Introducir clases agregaría complejidad sin valor académico aquí.

## 7. Sin base de datos

- La única forma de persistencia es el archivo CSV.
- No hay servicios externos.
- Motivo: restricción académica + mantener el proyecto explicable.
