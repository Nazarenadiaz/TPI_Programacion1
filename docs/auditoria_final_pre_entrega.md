# Auditoría final pre-entrega

> Revisión académica completa del código antes de la rama de pulido (Hito E)
> y antes de la entrega final. **Este documento no modifica código**: solo
> identifica hallazgos y los clasifica como **Recomendado** o **No
> recomendado**, con su dificultad y beneficio esperado.
>
> Alcance auditado: `src/main.py`, `src/menu.py`, `src/csv_manager.py`,
> `src/validaciones.py`, `src/paises.py`, `src/busquedas.py`,
> `src/filtros.py`, `src/ordenamientos.py`, `src/estadisticas.py`.

---

## 0. Resumen ejecutivo

| # | Hallazgo | Tipo | Dificultad | ¿Aplicar? |
|---|---|---|---|---|
| 1 | Comprensión de listas en `filtros.py` (fuera del programa del curso) | Adecuación al curso | Baja | **Sí** |
| 2 | `int(input(...))` directo en filtros, en lugar de `pedir_entero` | Duplicación validaciones | Baja | **Sí** |
| 3 | `validar_rango` no se usa en filtros | Duplicación validaciones | Baja | **Sí** |
| 4 | Prefijos de mensaje inconsistentes (`ERROR,` vs `ERROR:`, etc.) | Mensajes | Baja | **Sí** |
| 5 | `"ERROR,Opcion invalida."` sin espacio tras la coma | Mensajes | Baja | **Sí** |
| 6 | Texto `"Ingresa"` vs `"Ingrese"` (vos vs usted) | Mensajes | Baja | **Sí** |
| 7 | Falta de tildes en mensajes y título del menú | Mensajes | Baja | **Sí** |
| 8 | `except Exception` amplio en `csv_manager.py` | Manejo de errores | Baja | **Sí** |
| 9 | `mostrar_paises`: columna "Continente" pegada a "Superficie" | Legibilidad | Baja | **Sí** |
| 10 | `agregar_pais` acepta `poblacion = 0` (asintomático) | Validación | Baja | Decisión consciente |
| 11 | Doble mensaje `"OK, ..."` al agregar/actualizar | Mensajes | Baja | **Sí** |
| 12 | `ejecutar_opcion` con cadena larga de `if/elif` | Modularidad | Media | **No** (riesgo overengineering) |
| 13 | Crear módulo `mensajes.py` o constantes globales | Centralización | Media | **No** |
| 14 | Filtro por continente sensible a tildes | UX | Media | **No** (alcance) |
| 15 | Reescritura completa del CSV en cada alta | Performance | Media | **No** |
| 16 | `paises.py` mezcla presentación (`mostrar_paises`) y dominio | Modularidad | Media | **No** |
| 17 | Falta de tests automatizados | Calidad | Alta | **No** (no exigido) |
| 18 | Funciones `obtener_*` en `ordenamientos.py` | Naming | Baja | **Sí** (mantener) |
| 19 | `flujo_ordenar` vs `mostrar_estadisticas` (naming del orquestador) | Naming | Baja | **No** |
| 20 | Default `ruta=RUTA_CSV` expuesto pero nunca usado desde fuera | Diseño | Baja | **No** |
| 21 | Renombrar archivos (`csv_manager` ya está bien) | Naming | Baja | **No** |
| 22 | Permitir actualizar nombre y continente en `actualizar_pais` | Funcionalidad | Media | **No** (alcance del Hito B) |
| 23 | Documentar decisiones en `decisiones_tecnicas.md` | Defensa oral | Baja | **Sí** |

**Conclusión:** la rama de pulido (Hito E) debe enfocarse en los hallazgos
**1, 2, 3, 4, 5, 6, 7, 8, 9, 11** (todos *Baja* dificultad y alto impacto en
rúbrica) más el **23** (preparación de la defensa). El resto son trampas de
overengineering o están fuera del alcance del TP.

---

## 1. Duplicación de código

### 1.1 Comprensión de listas en `filtros.py`

- **Archivo afectado:** `src/filtros.py` (`filtrar_por_poblacion`, `filtrar_por_superficie`).
- **Problema:** se usa una *list comprehension* (`[pais for pais in paises if minimo <= pais["poblacion"] <= maximo]`). Las comprensiones de listas **no están en el temario** del curso (Funciones, parámetros, alcance, `input`, `print`, `len`, `pass`, listas, diccionarios, CSV, modularización básica). En el Hito C ya se eliminaron las `lambda` por la misma razón.
- **Cambio propuesto:** reemplazar por un `for` + `append` explícito. Patrón ya usado en `busquedas.buscar_pais` y `filtros.filtrar_por_continente`.
- **Beneficio esperado:** consistencia con el resto del proyecto y con el temario; defendible en la oral. Mejora I.1 (Adecuación al enunciado).
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.** Es prerrequisito antes de la entrega.

### 1.2 `agregar_pais` y `actualizar_pais` repiten la validación de superficie > 0

- **Archivo afectado:** `src/paises.py`.
- **Problema:** ambas funciones tienen el mismo bloque:
  ```python
  if superficie == 0:
      print("ERROR, La superficie debe ser mayor a cero.")
      return paises
  ```
- **Cambio propuesto:** dejarlo como está. Son 2 ocurrencias de 3 líneas. Extraerlo a un helper `pedir_entero_positivo` agrega indirección sin reducir realmente la complejidad. Si se aplica el hallazgo **2** (usar `pedir_entero` en filtros), `validaciones.py` ya cumple su rol. Una tercera variante para "> 0" agrega ruido.
- **Dificultad:** Baja.
- **Recomendación:** **No recomendado.** Riesgo de overengineering (M.E.5).

---

## 2. Duplicación de validaciones

### 2.1 `int(input(...))` directo en filtros

- **Archivo afectado:** `src/filtros.py` (`filtrar_por_poblacion`, `filtrar_por_superficie`).
- **Problema:** ambas funciones implementan a mano `try: int(input(...)); except ValueError: print("ERROR, ...")` cuando ya existe `validaciones.pedir_entero`.
- **Cambio propuesto:** reemplazar por dos llamadas a `pedir_entero(...)`; verificar que ambos valores no sean `None` antes de comparar.
- **Beneficio esperado:** elimina duplicación, unifica el mensaje de error de "número entero", reduce el `try/except` repetido. Sube II.3 (Modularidad) y II.7 (Manejo de errores).
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.** Es M.E.4 del informe de mejoras pendientes.

### 2.2 `validar_rango` no se usa en los filtros

- **Archivo afectado:** `src/filtros.py`.
- **Problema:** el chequeo `if minimo > maximo` está duplicado en `filtrar_por_poblacion` y `filtrar_por_superficie`, con un mensaje también duplicado. Existe `validaciones.validar_rango` que ya hace exactamente eso (incluyendo la verificación de no-negatividad que actualmente falta).
- **Cambio propuesto:** después de aplicar 2.1, llamar a `validar_rango(minimo, maximo)` y devolver si es `False`.
- **Beneficio esperado:** una sola fuente de verdad para validar rangos. Cubre indirectamente el observación #8 del informe (rangos negativos rechazados).
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.** Es M.E.4 + #8 del informe.

### 2.3 `pedir_texto_no_vacio` y validación inline en `busquedas.py` / `filtros.py`

- **Archivos afectados:** `src/busquedas.py` (`buscar_pais`), `src/filtros.py` (`filtrar_por_continente`).
- **Problema:** ambos hacen `input(...).strip()` y un `if not termino: print("ERROR, ...")`. Existe `pedir_texto_no_vacio`.
- **Cambio propuesto:** reemplazar por `termino = pedir_texto_no_vacio(...)` y devolver si es `None`.
- **Beneficio esperado:** consistencia con `agregar_pais` y `actualizar_pais` (que ya lo usan); un único mensaje de error para "valor vacío".
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.**

---

## 3. Inconsistencias en mensajes al usuario

### 3.1 Prefijos mezclados (`ERROR,` vs `ERROR:`, `ADVERTENCIA,` vs `ADVERTENCIA:`, `OK,`)

- **Archivos afectados:** todos los módulos excepto `validaciones.py` (que es el único que ya usa `ERROR:`).
- **Inventario actual:**
  - `ERROR, ...` (coma + espacio) — `csv_manager.py`, `paises.py`, `busquedas.py`, `filtros.py`, `ordenamientos.py`.
  - `ERROR,Opcion invalida.` (coma sin espacio) — `menu.py`, línea de opción inválida.
  - `ERROR: ...` (dos puntos + espacio) — `validaciones.py`.
  - `ADVERTENCIA: ...` — `main.py`.
  - `ADVERTENCIA, ...` — `csv_manager.py`.
  - `OK, ...` — `csv_manager.py`, `paises.py`.
- **Cambio propuesto:** unificar a la convención del plan: **`ERROR: `, `ADVERTENCIA: `, `OK: `** (dos puntos + un espacio) en todos los archivos. Sin crear módulo de mensajes; sin constantes globales. Es un *find & replace* manual cuidadoso.
- **Beneficio esperado:** los mensajes se ven idénticos en el video. Mejora II.6 (Legibilidad) y II.7 (Manejo de errores). Defendible: "decidimos un único formato".
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.** Es M.E.2 del informe.

### 3.2 `"ERROR,Opcion invalida."` sin espacio después de la coma

- **Archivo afectado:** `src/menu.py` (línea de la rama `else:` de `ejecutar_opcion`).
- **Problema:** rompe el patrón aún antes de unificar prefijos. Es un detalle que cualquier evaluador detecta.
- **Cambio propuesto:** queda corregido al aplicar 3.1 (`"ERROR: Opcion invalida."`).
- **Recomendación:** **Recomendado** (subsume en 3.1).

### 3.3 `"Ingrese..."` vs `"Ingresa..."` (formal vs informal)

- **Archivos afectados:** `src/busquedas.py` (`"Ingrese el nombre o parte..."`), `src/filtros.py` (`"Ingresa el continente: "`), `src/ordenamientos.py` (`"Elegi un criterio: "`, `"Elegi una direccion: "`), `src/menu.py` (`"Elegi una opcion: "`).
- **Problema:** mezcla de tratamiento (`Ingrese` = usted; `Ingresa`, `Elegi` = vos/tú). Es muy visible en la demo.
- **Cambio propuesto:** unificar a una sola forma. Recomendación: **vos/tú** (forma corta), porque ya predomina (`Elegi`, `Ingresa`). Cambiar `"Ingrese el nombre..."` a `"Ingresa el nombre..."`. Sin agregar tildes (ver 3.4).
- **Beneficio esperado:** voz consistente en toda la app. Mejora II.6 (Legibilidad) y la prolijidad del video.
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.**

### 3.4 Falta de tildes en mensajes y título del menú

- **Archivos afectados:** `menu.py` (`"GESTION DE DATOS DE PAISES"`, opciones del menú), prácticamente todos los módulos.
- **Problema:** título del menú sin tildes (`GESTIÓN`, `PAÍSES`); columnas (`Poblacion`, `Pais`); mensajes (`"Pais con mayor poblacion: ..."`, `"Paises ordenados..."`). En cambio, los datos del CSV sí tienen tildes (`América`, `África`, `Japón`). El contraste se nota en el video.
- **Cambio propuesto:** dos opciones, elegir una y aplicarla en todo el proyecto:
  - **(A)** Agregar tildes a todos los textos visibles. Requiere revisar 30+ strings.
  - **(B)** Dejar sin tildes en strings y mantener tildes solo en datos del CSV. Es la decisión actual de facto.
- **Recomendación:** **Recomendado (A)**, porque la rúbrica valora "claridad" y la falta de tildes es lo primero que comenta un evaluador. Si se opta por (B), documentarlo explícitamente en `docs/decisiones_tecnicas.md` para que aparezca en la defensa como decisión consciente.
- **Beneficio esperado:** mejora II.6 (Legibilidad) y la impresión general en la entrega.
- **Dificultad:** Baja (solo strings).

### 3.5 Doble mensaje `"OK, ..."` al agregar/actualizar

- **Archivos afectados:** `src/paises.py` (`agregar_pais`, `actualizar_pais`) + `src/csv_manager.py` (`guardar_paises`).
- **Problema:** al ejecutar opción 1 o 6, el usuario ve dos mensajes seguidos:
  ```
  OK, Datos guardados correctamente.
  OK, Pais 'Argentina' actualizado correctamente.
  ```
  El primer mensaje es ruido: la operación es "agregar/actualizar país", no "guardar archivo".
- **Cambio propuesto:** quitar el `print("OK: Datos guardados correctamente.")` de `guardar_paises`. Si la persistencia falla, ya se imprime un `ERROR:`. El éxito lo confirma quien llama (`agregar_pais`, `actualizar_pais`) con su propio mensaje contextual.
- **Beneficio esperado:** salida más limpia y profesional. Mejora II.6 (Legibilidad).
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.**

---

## 4. Inconsistencias de naming

### 4.1 `obtener_nombre`, `obtener_poblacion`, `obtener_superficie`

- **Archivo afectado:** `src/ordenamientos.py`.
- **Observación:** los nombres son claros y se introdujeron explícitamente para reemplazar `lambda`. Buen ejemplo para defensa oral.
- **Recomendación:** **Mantener.** No renombrar.

### 4.2 `flujo_ordenar` vs `mostrar_estadisticas` (orquestadores con prefijos distintos)

- **Archivos afectados:** `src/ordenamientos.py`, `src/estadisticas.py`.
- **Problema (menor):** dos funciones que cumplen el mismo rol (orquestar la opción del menú) usan prefijos distintos: `flujo_*` vs `mostrar_*`.
- **Cambio propuesto:** dos opciones:
  - **(A)** Renombrar `flujo_ordenar` a `mostrar_orden_paises` o `ordenar_y_mostrar`.
  - **(B)** Dejar como está.
- **Recomendación:** **No recomendado** cambiar. La diferencia refleja una distinción real: `flujo_ordenar` requiere submenú (criterio + dirección); `mostrar_estadisticas` no requiere interacción adicional. El nombre `flujo_*` comunica eso. Cambiarlo es maquillaje.

### 4.3 Función `cantidad_por_continente` devuelve dict, pero `mostrar_estadisticas` la imprime como tabla

- **Archivos afectados:** `src/estadisticas.py`.
- **Observación:** los nombres son consistentes con el patrón "función pura + función de presentación". Buen modelo a destacar en la defensa.
- **Recomendación:** **Mantener.**

---

## 5. Legibilidad

### 5.1 `mostrar_paises`: columna "Continente" pegada a "Superficie"

- **Archivo afectado:** `src/paises.py` (`mostrar_paises`).
- **Problema visible:**
  ```
  Nombre                    Poblacion  Superficie (km²)Continente
  Argentina                45,376,763         2,780,400América
  ```
  No hay separación entre el valor numérico de superficie y el continente. Es lo más obvio del video.
- **Cambio propuesto:** ajustar anchos:
  ```python
  print(
      f"\n{'Nombre':<20}"
      f"{'Poblacion':>15}  "
      f"{'Superficie (km²)':>18}  "
      f"{'Continente':<12}"
  )
  print("-" * 75)
  ```
  (separador de 2 espacios entre columnas). Aplicar el mismo cambio en la fila de datos.
- **Beneficio esperado:** salida prolija, lectura cómoda. Mejora II.6 directamente.
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.** Es la observación #6 del informe.

### 5.2 Magic numbers en `mostrar_menu` (`45`)

- **Archivo afectado:** `src/menu.py`.
- **Observación:** `"=" * 45` aparece dos veces dentro de la misma función.
- **Cambio propuesto:** una variable local `ANCHO = 45` al inicio de `mostrar_menu`. **No** una constante de módulo.
- **Recomendación:** opcional. Aceptable dejarlo como está.

### 5.3 `csv_manager.cargar_paises`: condición de fila incompleta extensa

- **Archivo afectado:** `src/csv_manager.py`.
- **Observación:** el `if (not fila.get("nombre") or ...)` ocupa 6 líneas. Es legible. No tocar.
- **Recomendación:** **Mantener.**

---

## 6. Modularidad

### 6.1 `paises.py` contiene `mostrar_paises` (presentación) además del dominio

- **Archivo afectado:** `src/paises.py`.
- **Observación:** mezcla función de presentación (`mostrar_paises`) con operaciones de dominio (`agregar_pais`, `actualizar_pais`). Para un TP académico, agruparlas tiene sentido (el dominio es "país", la presentación tabular también es "de país"). Mover `mostrar_paises` a un nuevo módulo `presentacion.py` solo agregaría un archivo más para defender.
- **Recomendación:** **Mantener.** Documentar la decisión en `decisiones_tecnicas.md` ("una sola unidad de cohesión por entidad").

### 6.2 `ejecutar_opcion` con cadena larga de `if/elif`

- **Archivo afectado:** `src/menu.py`.
- **Problema:** 8 ramas. Tentación de reemplazar por un diccionario `{"1": agregar_pais, ...}`.
- **Cambio propuesto:** **no reemplazar.** Las funciones tienen firmas distintas:
  - `agregar_pais(paises) -> paises` (devuelve la lista actualizada).
  - `actualizar_pais(paises) -> paises`.
  - `buscar_pais(paises) -> None`.
  - `flujo_ordenar(paises) -> None`.
  - etc.
  
  Para usar un dict habría que envolver cada una en una función adaptadora o duplicar la lógica de "asignar o no" según el caso. El resultado sería más confuso que el `if/elif` actual.
- **Recomendación:** **No recomendado.** Es M.E.1 del informe; ya se documentó como riesgo de overengineering.

### 6.3 `csv_manager.py` no importa nada del proyecto

- **Observación:** correcto. Mantener así.

### 6.4 Posibles imports circulares

- **Análisis:** el grafo es estricto:
  - `validaciones` → nada
  - `csv_manager` → nada
  - `paises` → `csv_manager`, `validaciones`
  - `busquedas` → `paises`
  - `filtros` → `paises`
  - `ordenamientos` → `paises`
  - `estadisticas` → nada
  - `menu` → `paises`, `busquedas`, `filtros`, `ordenamientos`, `estadisticas`
  - `main` → `csv_manager`, `menu`
  
  Sin ciclos. **No tocar.**
- **Recomendación:** **Mantener.**

---

## 7. Riesgos de overengineering (qué NO hacer)

| Tentación | Por qué resistirla |
|---|---|
| Crear `mensajes.py` o constantes globales para `ERROR: `, `ADVERTENCIA: `, `OK: ` | No hay traducciones, ni reuso real. Tres cadenas estáticas no requieren un módulo. |
| Reemplazar `ejecutar_opcion` por dict de funciones | Las firmas distintas obligan a wrappers que ofuscan el flujo. Ver **6.2**. |
| Crear módulo `presentacion.py` para `mostrar_paises` | Una función presentacional no justifica un módulo separado en un TP. |
| Agregar `unicodedata` para normalizar tildes en filtros | Aporta robustez al precio de explicar `unicodedata.normalize` en la defensa. |
| Tipar todas las funciones (`def f(paises: list[dict]) -> dict`) | Type hints no están en el temario; mostrar tipados parciales o erróneos en la defensa es peor que no tenerlos. |
| Reemplazar `if/elif` largos por `match/case` | `match/case` no está en el temario. |
| Capturar `KeyboardInterrupt` y mostrar mensaje | Caso borde que la consigna no pide; agrega rama de manejo de errores difícil de defender. |
| Agregar tests automatizados (`pytest`/`unittest`) | La rúbrica no los pide. La defensa oral suple. |

---

## 8. Riesgos para la defensa oral

### 8.1 Inconsistencias visibles en mensajes

- **Riesgo alto.** Si el evaluador ejecuta el programa y ve `ERROR,Opcion invalida.` (sin espacio), `ADVERTENCIA: ...` (con dos puntos) y `OK, Datos guardados...` (con coma) en la misma sesión, hará la observación. Difícil de defender salvo confesando el descuido.
- **Mitigación:** aplicar **3.1, 3.2, 3.3, 3.4, 3.5** antes de grabar el video.

### 8.2 `lambda` y comprensiones de listas: contenido fuera del programa

- **Riesgo medio.** Las `lambda` ya se eliminaron (Hito C). Las **comprensiones de listas** en `filtros.py` siguen presentes y un docente podría preguntar "¿esto lo vieron en clase?". Si la respuesta honesta es "no, lo aprendí buscando", el riesgo es la sospecha de IA generativa sin curaduría.
- **Mitigación:** aplicar **1.1**.

### 8.3 `except Exception` genérica

- **Riesgo bajo.** Es defendible ("queremos atrapar cualquier problema de I/O"), pero la convención del proyecto pide ser específicos.
- **Mitigación:** aplicar **8** del resumen (reemplazar por `except (OSError, csv.Error)` en lectura y `except OSError` en escritura). No es bloqueante.

### 8.4 Decisiones documentadas

- **Riesgo medio.** Si en la defensa preguntan "¿por qué no hicieron X?" y X es algo razonable que descartaron (módulo de mensajes, tildes, dispatch con dict), la respuesta debe estar escrita en `docs/decisiones_tecnicas.md`. Improvisar transmite que no se pensó.
- **Mitigación:** ver **23**.

### 8.5 `actualizar_pais` no permite actualizar nombre ni continente

- **Riesgo bajo.** Es una decisión razonable (esos campos son "identidad" del país; si querés cambiarlos, eliminás y agregás). Pero hay que poder defenderla.
- **Mitigación:** una línea en `decisiones_tecnicas.md`: *"`actualizar_pais` solo cambia datos numéricos para preservar la identidad del país. Cambiar nombre o continente equivale a un alta + baja."*

---

## 9. Cambios que pueden mejorar la nota

### 9.1 Aplicar todos los hallazgos de dificultad **Baja** marcados Recomendado

Suma puntaje en:
- **II.3 Modularidad** (eliminar duplicación de validaciones).
- **II.6 Legibilidad** (mensajes uniformes, tabla prolija).
- **II.7 Manejo de errores** (un mensaje por categoría; excepciones específicas en CSV).
- **I.1 Adecuación al enunciado** (sin elementos fuera del temario).

### 9.2 Documentar decisiones técnicas

- **Archivo:** `docs/decisiones_tecnicas.md` (ya existe; revisar y completar).
- **Contenido sugerido:** anotar cada *"No recomendado"* de esta auditoría con su justificación. Cuando el evaluador pregunte "¿por qué no hicieron X?", la respuesta está escrita.
- **Beneficio:** reduce el riesgo de la defensa oral.
- **Dificultad:** Baja.
- **Recomendación:** **Recomendado.**

### 9.3 Revisar `README.md` para que refleje los 8 módulos

- **Archivo:** `README.md`.
- **Acción:** verificar que liste correctamente los archivos en `src/` (incluyendo los creados en Hitos B/C/D: `paises.py`, `validaciones.py`, `ordenamientos.py`, `estadisticas.py`) y un comando de ejecución correcto (`python src/main.py`).
- **Recomendación:** **Recomendado.**

### 9.4 Verificar `informe_mejoras_pendientes.md`

- **Archivo:** `docs/informe_mejoras_pendientes.md`.
- **Acción:** después de aplicar el Hito E, marcar como **resueltas** las observaciones #1, #2, #3, #4, #9, #11. Dejar la sección "Mejoras a evaluar en Hito E" actualizada con lo que se aplicó y lo que se descartó.
- **Recomendación:** **Recomendado.**

---

## 10. Lo que ya está bien (defendible sin cambios)

- **Cálculo de `RUTA_CSV` con `__file__`**: el programa funciona desde cualquier directorio. Defendible.
- **Sin imports circulares**: el grafo de dependencias es estricto y plano.
- **Sin clases**: respetando el temario.
- **`if __name__ == "__main__"`** solo en `main.py`: convención correcta.
- **Funciones puras en `estadisticas.py` + función orquestadora `mostrar_estadisticas`**: separación de cálculo y presentación. Buen ejemplo para destacar en la defensa.
- **`ordenar_paises` devuelve nueva lista** (no muta la original): defendible y verificable en la demo.
- **`agregar_pais` rechaza duplicados case-insensitive** y **`actualizar_pais` busca case-insensitive**: consistentes entre sí.
- **`validaciones.py` no importa nada del proyecto**: módulo independiente, fácil de testear manualmente.
- **`csv_manager.py` no importa nada del proyecto**: capa de persistencia aislada.
- **Sin uso de `lambda`** después del Hito C.
- **Sin uso de `collections.Counter`** ni librerías externas en `estadisticas.py`.

---

## 11. Plan recomendado para Hito E

Aplicar, en este orden:

1. **3.1 + 3.2 + 3.5 (prefijos unificados).** Pase de `find & replace`.
2. **5.1 (tabla `mostrar_paises`).** Ajuste de anchos.
3. **3.3 (uniformar `Ingresa`/`Elegi`).**
4. **3.4 (decidir tildes A o B y aplicar).**
5. **2.1 + 2.2 (filtros usan `pedir_entero` + `validar_rango`).**
6. **2.3 (búsqueda y filtro de continente usan `pedir_texto_no_vacio`).**
7. **1.1 (eliminar comprensiones de listas en filtros).**
8. **#9 del informe (`except` específicos en `csv_manager`).**
9. **9.2 (actualizar `decisiones_tecnicas.md`).**
10. **9.4 (actualizar `informe_mejoras_pendientes.md`).**
11. **9.3 (revisar `README.md`).**

Cada paso es un commit pequeño. Probar `python src/main.py` después de cada uno.

---

## 12. Cierre

- **Estado funcional:** completo. Las 8 opciones del menú funcionan, no se detectaron defectos bloqueantes.
- **Estado de calidad:** sólido en estructura modular y manejo de errores básicos; **mejorable** en uniformidad de mensajes y en eliminar elementos fuera del temario (comprensiones de listas).
- **Riesgo principal de pérdida de puntaje:** **inconsistencia visual de mensajes** (II.6 y II.7) y **uso de comprensiones de listas** (I.1). Ambos resolubles en una sola tarde.
- **Riesgo principal de defensa oral:** preguntas sobre las comprensiones de listas en `filtros.py` y sobre por qué se descartaron alternativas (mensajes centralizados, dispatch con dict). Mitigado documentando decisiones.

> Este documento es la última pasada de revisión antes de cerrar la rama
> `feature/core-functionality`. Ninguno de los hallazgos requiere reescribir
> el proyecto: todos los **Recomendados** son ediciones puntuales de
> dificultad **Baja**.
