# Informe de mejoras pendientes

> Observaciones detectadas sobre el código existente (`src/main.py`, `src/busquedas.py`, `src/csv_utils.py`, `src/filtros.py`) durante la fase de reorganización (rama `chore/repo-structure`).
> **Este documento es solo una bitácora.** Ninguna de estas mejoras se implementa en esta rama; cada una queda asignada a una rama futura del plan.

---

## Formato de cada observación

- **Módulo afectado**
- **Problema observado**
- **Por qué importa**
- **Impacto:** requisito de la consigna ↔ solo calidad de código
- **Rama futura donde se aborda**
- **Cómo explicárselo al compañero/a**

---

## 1. `mostrar_paises` vive en `src/busquedas.py` pero la usan los filtros

- **Módulo afectado:** `src/busquedas.py`, `src/filtros.py`.
- **Problema observado:** la función de presentación tabular `mostrar_paises` está definida en `busquedas.py` y se importa desde `filtros.py`. Cuando aparezcan `ordenamientos.py` y `estadisticas.py`, también tendrán que importarla desde ahí.
- **Por qué importa:** un módulo de búsqueda no debería ser la fuente de una utilidad compartida. Genera dependencias cruzadas innecesarias y dificulta explicar la modularización.
- **Impacto:** **solo calidad de código** (modularidad). No afecta el funcionamiento.
- **Rama futura:** `feature/search-and-filters` (Paso 5) o `feature/country-crud` (Paso 4), cuando se cree `paises.py`. La utilidad `mostrar_paises` se moverá a `paises.py`.
- **Cómo explicarlo:** "Mover `mostrar_paises` al módulo de dominio `paises.py` para que cualquier módulo que necesite imprimir países la importe desde un único lugar, y dejar `busquedas.py` enfocado solo en buscar."

## 2. `csv_utils.py` mezcla persistencia con lógica de alta de país

- **Módulo afectado:** `src/csv_utils.py` (función `agregar_pais`).
- **Problema observado:** `csv_utils.py` contiene `cargar_paises`, `guardar_paises` **y** `agregar_pais`. La última pide datos por consola, valida y persiste. Mezcla I/O de archivo con interacción con el usuario y reglas de negocio.
- **Por qué importa:** rompe el principio "una función = una responsabilidad" y dificulta reutilizar las validaciones desde otros flujos (actualización, importación masiva, tests manuales).
- **Impacto:** **solo calidad de código** (modularidad). La funcionalidad existente se mantiene.
- **Rama futura:**
  - `feature/csv-validations` (Paso 3): renombrar `csv_utils.py` → `csv_manager.py` dejándolo solo con `cargar_paises` y `guardar_paises`.
  - `feature/country-crud` (Paso 4): mover `agregar_pais` a `paises.py` y reutilizar `validaciones.py`.
- **Cómo explicarlo:** "Separar el módulo en tres responsabilidades: leer/escribir CSV (`csv_manager.py`), pedir y validar datos del usuario (`validaciones.py`), y operar sobre la lista de países (`paises.py`)."

## 3. Validaciones duplicadas entre módulos

- **Módulo afectado:** `src/csv_utils.py` (alta) y `src/filtros.py` (rangos).
- **Problema observado:** el patrón `try: int(input(...)) ; except ValueError: print(ERROR,...)` se repite literalmente en `agregar_pais`, `filtrar_por_poblacion` y `filtrar_por_superficie`.
- **Por qué importa:** cualquier cambio (por ejemplo, agregar mensaje en español más claro o normalizar formato) hay que hacerlo en varios lugares. Es exactamente el tipo de duplicación que la rúbrica penaliza en "Modularidad" y "Manejo de errores".
- **Impacto:** **solo calidad de código** (DRY, modularidad).
- **Rama futura:** `feature/csv-validations` (Paso 3) — crear `validaciones.py` con `pedir_entero`, `pedir_texto_no_vacio`, `validar_rango`.
- **Cómo explicarlo:** "Extraer las validaciones repetidas a un módulo `validaciones.py` y hacer que los filtros y el alta llamen siempre a esas funciones."

## 4. Opciones 6, 7 y 8 del menú no implementadas

- **Módulo afectado:** `src/main.py`.
- **Problema observado:** las opciones "Actualizar pais", "Ordenar paises" y "Ver estadisticas" solo imprimen `MODULO PENDIENTE`.
- **Por qué importa:** son **funcionalidades obligatorias** según la consigna (sección "Funcionalidades mínimas del sistema") y representan parte sustancial del puntaje II.1 Funcionalidad (20 pts).
- **Impacto:** **requisito de la consigna**. Sin esto, el proyecto no aprueba el bloque de funcionalidad.
- **Rama futura:**
  - `feature/country-crud` (Paso 4): opción 6 (Actualizar).
  - `feature/sorting-and-statistics` (Paso 6): opciones 7 y 8.
- **Cómo explicarlo:** "Cada opción pendiente del menú se cubre con un módulo dedicado (`paises.py`, `ordenamientos.py`, `estadisticas.py`) y se invoca desde `menu.py`."

## 5. El menú vive dentro de `main.py`

- **Módulo afectado:** `src/main.py`.
- **Problema observado:** `mostrar_menu` y el `while True / if-elif` que despacha cada opción están en `main.py`. A medida que se agreguen las opciones 6, 7 y 8 con sus invocaciones, `main.py` crece.
- **Por qué importa:** `main.py` debería ser un punto de entrada mínimo. Tener menú + despacho ahí limita la legibilidad y la facilidad de extender.
- **Impacto:** **solo calidad de código** (modularidad, legibilidad).
- **Rama futura:** `feature/menu-and-flow` (Paso 2) — extraer a `src/menu.py` con `mostrar_menu` y `ejecutar_opcion(opcion, paises)`.
- **Cómo explicarlo:** "Que `main.py` solo cargue los datos y delegue al bucle del menú, definido en `menu.py`. Así si agregamos opciones, tocamos un solo archivo."

## 6. Formato visual de `mostrar_paises` sin separación entre columnas

- **Módulo afectado:** `src/busquedas.py` (función `mostrar_paises`).
- **Problema observado:** los anchos de formato (`<20`, `>15`, `>18`, `<15`) dejan a "Continente" pegado a "Superficie (km²)" en la cabecera y los valores. Ejemplo visible al ejecutar una búsqueda:
  ```
  Nombre                    Poblacion  Superficie (km²)Continente
  Argentina                45,376,763         2,780,400América
  ```
- **Por qué importa:** afecta la prolijidad de la salida que se muestra en el video. La rúbrica valora la legibilidad.
- **Impacto:** **solo calidad de código / UX**. No rompe funcionalidad.
- **Rama futura:** `feature/search-and-filters` (Paso 5) cuando se mueva `mostrar_paises` a `paises.py`.
- **Cómo explicarlo:** "Agregar un espacio mínimo entre columnas y revisar anchos para que la tabla se vea prolija en el video."

## 7. Filtros por continente sin normalización de tildes

- **Módulo afectado:** `src/filtros.py` (función `filtrar_por_continente`).
- **Problema observado:** la comparación es insensible a mayúsculas pero **sensible a tildes**. Buscar `america` no encuentra `América` solo si el usuario olvida la tilde, pero `América` ≠ `America` en `lower()`.
- **Por qué importa:** el dataset tiene tildes (`América`, `África`); un usuario que escriba sin tildes no obtiene resultados. Afecta la experiencia de la demo.
- **Impacto:** **calidad de código / UX**, con borde sobre requisito (la consigna pide "Filtrar por continente" — funciona, pero con la limitación).
- **Rama futura:** `feature/search-and-filters` (Paso 5). Se puede resolver con una función `normalizar(texto)` que pase a minúsculas y quite tildes con `unicodedata` (estándar, no es librería externa).
- **Cómo explicarlo:** "Comparar continentes ignorando tildes para que `america` también encuentre `América`. Es un detalle de UX que ayuda al video."

## 8. Filtros de rango aceptan valores negativos

- **Módulo afectado:** `src/filtros.py` (`filtrar_por_poblacion`, `filtrar_por_superficie`).
- **Problema observado:** se valida `minimo > maximo` pero no se valida que ambos sean `>= 0`. Un usuario podría ingresar `-100` como mínimo.
- **Por qué importa:** no rompe nada (no hay países con valores negativos) pero el manejo de errores es más débil.
- **Impacto:** **solo calidad de código** (manejo de errores).
- **Rama futura:** `feature/csv-validations` (Paso 3) o `feature/search-and-filters` (Paso 5), usando `validaciones.py`.
- **Cómo explicarlo:** "Agregar a `validar_rango` que ambos extremos sean enteros no negativos, y aplicarlo en los dos filtros de rango."

## 9. `except Exception as e` demasiado amplio en `csv_utils.py`

- **Módulo afectado:** `src/csv_utils.py` (`cargar_paises`, `guardar_paises`).
- **Problema observado:** se captura `Exception` genérica. Esconde errores inesperados (por ejemplo, un bug de programación) bajo un mensaje genérico de "Al leer el archivo CSV".
- **Por qué importa:** la convención del proyecto pide capturar excepciones específicas (`OSError`, `ValueError`, `csv.Error`).
- **Impacto:** **solo calidad de código** (manejo de errores). Para una entrega académica el riesgo es mínimo.
- **Rama futura:** `feature/csv-validations` (Paso 3) cuando se renombre a `csv_manager.py`.
- **Cómo explicarlo:** "Reemplazar `except Exception` por `except (OSError, csv.Error)` para distinguir un error de archivo de un error de programación."

## 10. `agregar_pais` reescribe todo el CSV en cada alta

- **Módulo afectado:** `src/csv_utils.py` (`agregar_pais` + `guardar_paises`).
- **Problema observado:** cada vez que se agrega un país, el archivo entero se reescribe.
- **Por qué importa:** con 8 países es irrelevante. Con miles, sería lento. Para este TP no es un problema real.
- **Impacto:** **solo calidad de código** (rendimiento, no requerido por la rúbrica).
- **Rama futura:** **no se aborda**. Documentado solo para mencionarlo en el informe PDF como decisión consciente ("se prioriza simplicidad sobre rendimiento, dataset pequeño").
- **Cómo explicarlo:** "Lo dejamos así a propósito: para el tamaño del CSV es perfectamente aceptable y mantiene el código simple."

---

## Resumen rápido

| # | Tema | Impacto | Rama futura |
|---|---|---|---|
| 1 | `mostrar_paises` mal ubicada | Calidad | Paso 4 o 5 |
| 2 | Mezcla I/O + dominio en `csv_utils.py` | Calidad | Pasos 3 y 4 |
| 3 | Validaciones duplicadas | Calidad | Paso 3 |
| 4 | Opciones 6, 7 y 8 sin implementar | **Consigna** | Pasos 4 y 6 |
| 5 | Menú dentro de `main.py` | Calidad | Paso 2 |
| 6 | Formato visual de tabla | Calidad / UX | Paso 5 |
| 7 | Filtro por continente sin tildes | Calidad / UX | Paso 5 |
| 8 | Rangos aceptan negativos | Calidad | Paso 3 o 5 |
| 9 | `except Exception` amplio | Calidad | Paso 3 |
| 10 | Reescritura completa del CSV al agregar | Aceptable | No se aborda |
