# TPI Programación 1 — Gestión de Datos de Países

Aplicación de consola en Python para gestionar información de países: alta, actualización, búsqueda, filtros, ordenamientos y estadísticas básicas a partir de un archivo CSV.

> **Estado:** funcionalmente completa. Las 8 opciones del menú están implementadas y operativas.

## Requisitos

- **Python 3.12**.
- **Sin librerías externas:** el proyecto usa únicamente la biblioteca estándar (`csv`, `os`).

## Cómo ejecutar

Desde la raíz del proyecto:

```bash
python3 src/main.py
```

El programa carga los países desde `data/paises.csv` y muestra el menú principal. La ruta al CSV se calcula a partir de `__file__`, así que también funciona ejecutado desde otros directorios.

## Estructura del proyecto

```
TPI_Programacion1/
├── data/
│   └── paises.csv                  # Dataset base
├── src/
│   ├── main.py                     # Punto de entrada; carga el CSV y delega en el menú
│   ├── menu.py                     # Menú principal y despacho de opciones
│   ├── csv_manager.py              # Lectura y escritura del CSV
│   ├── validaciones.py             # Helpers de entrada validada
│   ├── paises.py                   # Dominio: alta, actualización y presentación tabular
│   ├── busquedas.py                # Búsqueda por nombre
│   ├── filtros.py                  # Filtros por continente y rangos
│   ├── ordenamientos.py            # Ordenamiento por criterio y dirección
│   └── estadisticas.py             # Estadísticas agregadas sobre la lista de países
├── docs/
│   ├── consigna.md                 # Consigna oficial
│   ├── rubrica_evaluacion.md       # Rúbrica oficial
│   ├── decisiones_tecnicas.md      # Decisiones técnicas del proyecto
│   └── objetivo_nota_maxima.md     # Checklist de criterios para nota máxima
├── README.md
└── .gitignore
```

## Módulos y responsabilidades

| Módulo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada. Carga el CSV y delega el control en `menu.ejecutar_menu`. |
| `menu.py` | Muestra el menú principal y despacha la opción elegida (`mostrar_menu`, `leer_opcion`, `ejecutar_opcion`, `ejecutar_menu`). |
| `csv_manager.py` | Lectura y escritura del CSV (`cargar_paises`, `guardar_paises`). |
| `validaciones.py` | Helpers de entrada validada (`pedir_texto_no_vacio`, `pedir_entero`, `pedir_entero_no_negativo`, `validar_rango`). |
| `paises.py` | Operaciones de dominio (`agregar_pais`, `actualizar_pais`) y presentación tabular (`mostrar_paises`). |
| `busquedas.py` | Búsqueda por nombre con coincidencia parcial e insensible a mayúsculas (`buscar_pais`). |
| `filtros.py` | Filtros por continente y por rangos de población y superficie (`filtrar_por_continente`, `filtrar_por_poblacion`, `filtrar_por_superficie`). |
| `ordenamientos.py` | Ordenamiento por nombre, población o superficie, ascendente o descendente (`ordenar_paises`, `flujo_ordenar`). |
| `estadisticas.py` | Estadísticas agregadas: máximos, mínimos, promedios y conteo por continente (`mostrar_estadisticas`). |

## Funcionalidades

Menú principal (`python3 src/main.py`):

1. Agregar país
2. Buscar país por nombre (parcial o exacta, insensible a mayúsculas)
3. Filtrar por continente
4. Filtrar por rango de población
5. Filtrar por rango de superficie
6. Actualizar país (población y superficie)
7. Ordenar países (por nombre, población o superficie, asc/desc)
8. Ver estadísticas (mayor y menor población, promedios, conteo por continente)
0. Salir

## Integrantes

- **Estudiante A:** Acosta Diaz Milagros Nazarena
- **Estudiante B:** Herrera Marcos Ezequiel
