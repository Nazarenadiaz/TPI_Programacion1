# TPI Programación 1 — Gestión de Datos de Países

Aplicación de consola en Python para gestionar información de países: alta, búsqueda, filtros, ordenamientos y estadísticas básicas a partir de un archivo CSV.

> **Estado:** en desarrollo. El menú está disponible y las opciones 1 a 5 funcionan. Las opciones 6, 7 y 8 (actualizar, ordenar, estadísticas) están en construcción y se completan en las próximas ramas de trabajo.

## Requisitos

- **Python 3.12** (no requiere librerías externas; solo biblioteca estándar).

## Cómo ejecutar

Desde la raíz del repositorio:

```bash
python src/main.py
```

El programa carga los países desde `data/paises.csv` y muestra el menú principal.

## Estructura del proyecto

```
TPI_Programacion1/
├── data/
│   └── paises.csv                  # Dataset base
├── src/
│   ├── main.py                     # Punto de entrada
│   ├── busquedas.py                # Búsqueda por nombre
│   ├── csv_utils.py                # Lectura/escritura del CSV y alta de país
│   └── filtros.py                  # Filtros por continente y rangos
├── docs/
│   ├── consigna.md                 # Consigna oficial
│   ├── rubrica_evaluacion.md       # Rúbrica oficial
│   ├── decisiones_tecnicas.md      # Decisiones técnicas del proyecto
│   ├── objetivo_nota_maxima.md     # Checklist de criterios para nota máxima
│   └── informe_mejoras_pendientes.md  # Mejoras detectadas y a abordar en próximas ramas
├── README.md
├── PLAN_DESARROLLO.md              # Plan de desarrollo completo
└── .gitignore
```

## Funcionalidades

Menú principal (`python src/main.py`):

1. Agregar país
2. Buscar país por nombre (parcial o exacta)
3. Filtrar por continente
4. Filtrar por rango de población
5. Filtrar por rango de superficie
6. Actualizar país *(en desarrollo)*
7. Ordenar países *(en desarrollo)*
8. Ver estadísticas *(en desarrollo)*
0. Salir

## Integrantes

- **Estudiante A:** *pendiente*
- **Estudiante B:** *pendiente*

## Enlaces de la entrega

- **Video demostrativo:** *pendiente*
- **Informe PDF:** *pendiente*
