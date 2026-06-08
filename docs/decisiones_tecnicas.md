# Decisiones técnicas

**Gestión de Datos de Países**.

Documento conciso con las decisiones de diseño que dieron forma al proyecto. Cada entrada incluye la decisión y su justificación.

---

## 1. Python 3.12 con biblioteca estándar

- **Decisión:** el proyecto se desarrolla en Python **3.12** y utiliza únicamente la biblioteca estándar (`csv`, `os`).
- **Justificación:** una versión estable del intérprete y la ausencia de dependencias externas hacen que el programa corra con cualquier instalación limpia de Python 3.12, sin pasos de setup. La demo es reproducible directamente con `python3 src/main.py`.

## 2. Persistencia en archivo CSV con UTF-8

- **Decisión:** los datos se persisten en `data/paises.csv` con cabecera `nombre,poblacion,superficie,continente` y codificación UTF-8. La lectura y escritura se hacen con el módulo estándar `csv` (`DictReader`/`DictWriter`).
- **Justificación:** el CSV es un formato simple, inspeccionable a ojo y compatible con cualquier editor o planilla. UTF-8 permite preservar tildes y caracteres especiales (`América`, `África`, `Japón`) sin transformaciones.

## 3. Ruta del CSV resuelta con `__file__`

- **Decisión:** la ruta a `data/paises.csv` se calcula a partir de la ubicación del módulo (`__file__`), no del directorio de trabajo del proceso.
- **Justificación:** el programa funciona igual ejecutado desde la raíz del proyecto o desde cualquier otra carpeta. Evita errores frecuentes de "archivo no encontrado" según desde dónde se invoque.

## 4. Modelo de datos: lista de diccionarios

- **Decisión:** cada país es un `dict` con cuatro claves (`nombre`, `poblacion`, `superficie`, `continente`); la colección es una `list` de esos `dict`.
- **Justificación:** se mapea uno a uno con las filas del CSV, hace que cada atributo sea accesible por nombre (`pais["poblacion"]` antes que `pais[1]`) y mantiene el modelo de datos a la vista en cualquier punto del código.

## 5. Estructura `src/`, `data/`, `docs/`

- **Decisión:** el proyecto se organiza en tres carpetas: `src/` para el código fuente, `data/` para el dataset y `docs/` para la documentación. La raíz queda con `README.md`, `.gitignore` y las tres carpetas.
- **Justificación:** separa responsabilidades del repositorio (código, datos, documentación) y mantiene la raíz limpia para que el evaluador encuentre rápido lo importante al abrir GitHub.

## 6. Un módulo por responsabilidad

- **Decisión:** el código se reparte en módulos especializados dentro de `src/`: `main`, `menu`, `csv_manager`, `validaciones`, `paises`, `busquedas`, `filtros`, `ordenamientos` y `estadisticas`. Cada módulo expone funciones con una única responsabilidad.
- **Justificación:** dividir el programa en módulos especializados permite mantener el código organizado, evitar mezclar responsabilidades y facilitar tanto el mantenimiento como la comprensión del sistema.

## 7. Validaciones centralizadas en `validaciones.py`

- **Decisión:** la entrada del usuario pasa siempre por helpers reutilizables: `pedir_texto_no_vacio`, `pedir_entero`, `pedir_entero_no_negativo` y `validar_rango`. Los módulos de menú llaman a estos helpers y manejan el caso `None` cuando la validación falla.
- **Justificación:** un único lugar define cómo se valida cada tipo de entrada y qué mensaje de error se muestra. Cualquier ajuste en el formato de error se hace una sola vez y se propaga al resto del programa.

## 8. Cohesión por entidad: `mostrar_paises` vive en `paises.py`

- **Decisión:** las operaciones principales sobre países (alta, actualización y visualización) se implementan en `paises.py`.
- **Justificación:** concentrar estas funciones en un mismo módulo mejora la cohesión del código y facilita localizar la lógica relacionada con la entidad principal del sistema.

## 9. `actualizar_pais` modifica solo población y superficie

- **Decisión:** la opción 6 del menú permite cambiar exclusivamente los campos `poblacion` y `superficie` de un país existente. `nombre` y `continente` no se editan.
- **Justificación:** `nombre` y `continente` actúan como identidad del registro. Mantenerlos inmutables permite que la búsqueda case-insensitive sea determinista y evita estados intermedios donde el mismo país podría aparecer dos veces tras un renombrado.

## 10. Mensajes con prefijos consistentes

- **Decisión:** todo mensaje al usuario usa uno de tres prefijos: `OK: `, `ERROR: `, `ADVERTENCIA: `. La convención se aplica de forma uniforme en todos los módulos.
- **Justificación:** el usuario puede identificar rápidamente si una acción fue exitosa, produjo una advertencia o generó un error. Además, la salida mantiene un formato uniforme en todo el sistema.
