# Plan de actualización de documentación

> Revisión documental previa al PR de la rama `feature/core-functionality`.
> El código está funcionalmente completo (Hitos A–E). Este plan **solo
> define qué documentos tocar y qué cambiar**; la implementación se hace
> en commits posteriores. Alineado con `copilot_rules.md`,
> `PLAN_DESARROLLO.md`, `docs/consigna.md`, `docs/rubrica_evaluacion.md`
> y `docs/auditoria_final_pre_entrega.md`.

---

## 1. Estado actual de la documentación

| Documento | Estado | Acción |
|---|---|---|
| `README.md` | **Desactualizado.** Indica "en desarrollo", lista módulos viejos (`csv_utils.py`), marca opciones 6–8 como pendientes. | **Reescribir secciones desactualizadas** (estado, estructura, funcionalidades). |
| `docs/decisiones_tecnicas.md` | **Incompleto.** Cubre 7 decisiones; faltan las que la auditoría (sec. 9.2) recomienda dejar por escrito. | **Ampliar** con 6 decisiones nuevas. |
| `docs/informe_mejoras_pendientes.md` | **Desactualizado.** Las observaciones #1–#11 y la sección "Mejoras a evaluar en Hito E" ya se aplicaron o se descartaron en firme. | **Marcar resueltas/descartadas** sin reescribir el documento. |
| `docs/objetivo_nota_maxima.md` | **Desactualizado.** Checklist sin marcar; muchos ítems II ya están cubiertos por código. | **Tildar ítems II completados** con evidencia (archivo/función). |
| `docs/auditoria_final_pre_entrega.md` | **Histórico, vigente como auditoría pre-Hito E.** Refleja el estado *antes* del pulido. | **Dejar como está** (cierre histórico). Opcional: una nota de cierre al final. |
| `docs/plan_feature_core_functionality.md` | **Histórico.** Plan de la rama, no espec ejecutable. | **Dejar como está** (registro de planificación). |
| `docs/consigna.md` | Documento oficial de la cátedra. | **No tocar.** |
| `docs/rubrica_evaluacion.md` | Documento oficial de la cátedra. | **No tocar.** |
| `PLAN_DESARROLLO.md` | Plan general del TP. Referencia útil. | **No tocar** o nota mínima de cierre si conviene. |

**Documentos completos y al día:** `consigna.md`, `rubrica_evaluacion.md`,
`plan_feature_core_functionality.md`, `auditoria_final_pre_entrega.md`.

**Documentos desactualizados que requieren cambios obligatorios antes
del PR:** `README.md`, `decisiones_tecnicas.md`,
`informe_mejoras_pendientes.md`, `objetivo_nota_maxima.md`.

---

## 2. Plan de actualización — `README.md`

Reescribir las siguientes secciones (el resto se mantiene):

### 2.1 Estado del proyecto
- Reemplazar el bloque "*en desarrollo*" por: **"Funcionalmente completo. Las 8 opciones del menú están operativas."**

### 2.2 Descripción final
- Una línea: aplicación de consola en Python 3.12 que gestiona países desde un CSV (alta, búsqueda, filtros, actualización, ordenamiento, estadísticas).

### 2.3 Requisitos
- Confirmar **Python 3.12**, sin librerías externas, solo biblioteca estándar (`csv`, `os`).

### 2.4 Cómo ejecutar
- Mantener `python src/main.py` desde la raíz del repo.
- Aclarar que el CSV se resuelve con `__file__`, así que también funciona desde otros directorios.

### 2.5 Estructura final
Reemplazar el árbol actual por la estructura real:

```
TPI_Programacion1/
├── data/paises.csv
├── src/
│   ├── main.py
│   ├── menu.py
│   ├── csv_manager.py
│   ├── validaciones.py
│   ├── paises.py
│   ├── busquedas.py
│   ├── filtros.py
│   ├── ordenamientos.py
│   └── estadisticas.py
├── docs/
│   ├── consigna.md
│   ├── rubrica_evaluacion.md
│   ├── decisiones_tecnicas.md
│   ├── objetivo_nota_maxima.md
│   ├── informe_mejoras_pendientes.md
│   ├── auditoria_final_pre_entrega.md
│   ├── plan_feature_core_functionality.md
│   └── plan_actualizacion_documentacion.md
├── README.md
├── PLAN_DESARROLLO.md
└── .gitignore
```

### 2.6 Explicación de módulos principales
Tabla breve (una línea por módulo):

| Módulo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada; carga CSV y delega en el menú. |
| `menu.py` | Menú principal y despacho de opciones. |
| `csv_manager.py` | Lectura y escritura del CSV. |
| `validaciones.py` | Helpers de entrada validada. |
| `paises.py` | Dominio de países: alta, actualización, presentación tabular. |
| `busquedas.py` | Búsqueda por nombre. |
| `filtros.py` | Filtros por continente y rangos. |
| `ordenamientos.py` | Ordenamiento por criterio y dirección. |
| `estadisticas.py` | Estadísticas agregadas sobre la lista. |

### 2.7 Opciones del menú
Actualizar las 8 opciones **sin** marcas de "en desarrollo".

### 2.8 Ejemplos de uso
Agregar 2–3 ejemplos de salida real (capturas de texto, no de imagen):
- Búsqueda por nombre (`Argentina`).
- Filtro por rango de población.
- Estadísticas.

### 2.9 Integrantes
Mantener tal cual (Herrera Marcos Ezequiel, Acosta Diaz Milagros Nazarena).

### 2.10 Enlaces de la entrega
Mantener placeholders **`pendiente`** para video y PDF; reemplazar cuando estén disponibles.

---

## 3. Plan de actualización — `docs/decisiones_tecnicas.md`

Agregar 6 secciones nuevas (numeradas a partir de 8). Para cada una: 1
párrafo + 1 viñeta de "por qué se descartó la alternativa". Sin
reescribir lo existente.

| # | Decisión | Síntesis |
|---|---|---|
| 8 | **Sin lambdas ni comprensiones de listas** | El temario de Programación 1 cubre `for`, `if`, `def`, listas y diccionarios. Se reemplazaron las `lambda` (Hito C) y las comprensiones (Hito E) por funciones nombradas y `for`/`append`. Defendible en oral. |
| 9 | **Despacho del menú con `if/elif`, no con dict** | Las funciones de cada opción tienen firmas distintas (algunas devuelven la lista actualizada, otras no). Un dict obligaría a wrappers o `lambdas` que ofuscan el flujo. Ver auditoría 6.2 / M.E.1. |
| 10 | **Sin `mensajes.py` ni constantes globales para prefijos** | Tres cadenas estáticas (`ERROR: `, `ADVERTENCIA: `, `OK: `) no justifican un módulo. La unificación se hizo por *find & replace* en Hito E. Ver auditoría 7. |
| 11 | **`actualizar_pais` solo cambia población y superficie** | `nombre` y `continente` son la identidad del país; cambiarlos equivale a un alta + baja. Mantenerlos inmutables simplifica la búsqueda case-insensitive y evita estados intermedios. |
| 12 | **`mostrar_paises` vive en `paises.py`** | Cohesión por entidad: dominio + presentación tabular del mismo concepto. Crear un `presentacion.py` para una sola función agregaría un archivo a defender sin valor real. Ver auditoría 6.1. |
| 13 | **Sin tests automatizados ni type hints** | Ninguno está en el temario ni en la rúbrica. La validación es la defensa oral + ejecución del programa. |

Adicional opcional: ampliar la sección 4 con una línea sobre que `docs/`
ahora aloja también auditoría y planes de rama (registro histórico).

---

## 4. Plan de actualización — `docs/informe_mejoras_pendientes.md`

**No reescribir.** Solo agregar marcadores de estado al inicio de cada
observación. Formato sugerido: `> Estado: RESUELTA en Hito X` /
`> Estado: DESCARTADA (decisión consciente)`.

| # | Tema | Estado final |
|---|---|---|
| 1 | `mostrar_paises` mal ubicada | **RESUELTA** — Hito B (movida a `paises.py`). |
| 2 | Mezcla I/O + dominio en `csv_utils.py` | **RESUELTA** — Hito A (rename) + Hito B (`agregar_pais` movida). |
| 3 | Validaciones duplicadas | **RESUELTA** — Hito A (`validaciones.py`) + Hito E (filtros usan `pedir_entero` + `validar_rango`). |
| 4 | Opciones 6, 7, 8 sin implementar | **RESUELTA** — Hitos B/C/D. |
| 5 | Menú dentro de `main.py` | **RESUELTA** — `menu.py` ya existe. |
| 6 | Formato visual de tabla | **RESUELTA** — Hito E (anchos ajustados). |
| 7 | Filtro por continente sin tildes | **DESCARTADA** — agregar `unicodedata` excede el temario. Ver auditoría 7. |
| 8 | Rangos aceptan negativos | **RESUELTA** — `validar_rango` cubre el caso desde Hito A. |
| 9 | `except Exception` amplio | **RESUELTA** — Hito E (`(OSError, csv.Error)` y `OSError`). |
| 10 | Reescritura completa del CSV al agregar | **DESCARTADA** — irrelevante para 8 países; decisión consciente. |
| 11 | Inconsistencia de prefijos | **RESUELTA** — Hito E (unificados a `:` y espacio). |
| M.E.1 | Dispatch con dict | **DESCARTADA** — riesgo de overengineering (firmas distintas). |
| M.E.2 | Unificación de prefijos | **RESUELTA** — Hito E. |
| M.E.3 | Constantes para textos del menú | **DESCARTADA**. |
| M.E.4 | `pedir_entero` + `validar_rango` en filtros | **RESUELTA** — Hito E. |
| M.E.5 | Inline de submenús cortos | **RESUELTA (mantenido)**. |

Cierre: agregar al final una línea **"Hito E completado. Sin pendientes
abiertos para esta entrega."**

---

## 5. Plan de actualización — `docs/objetivo_nota_maxima.md`

Tildar **solo los ítems del bloque II** que ya están cubiertos por
código. Para cada uno, agregar evidencia entre paréntesis con el
formato `(archivo.py :: función)`.

### II.1 Funcionalidad — todos completables hoy
- [x] Carga de CSV con manejo de errores `(csv_manager.py :: cargar_paises)`
- [x] Agregar país con validaciones `(paises.py :: agregar_pais)`
- [x] Actualizar población y superficie `(paises.py :: actualizar_pais)`
- [x] Búsqueda por nombre `(busquedas.py :: buscar_pais)`
- [x] Filtro por continente `(filtros.py :: filtrar_por_continente)`
- [x] Filtro por rango de población `(filtros.py :: filtrar_por_poblacion)`
- [x] Filtro por rango de superficie `(filtros.py :: filtrar_por_superficie)`
- [x] Ordenamiento por nombre/población/superficie asc/desc `(ordenamientos.py :: ordenar_paises)`
- [x] Estadísticas `(estadisticas.py :: mostrar_estadisticas)`
- [x] Robustez ante entradas inválidas `(validaciones.py)`

### II.2 Estructuras de datos
- [x] País como `dict` `(paises.csv → cargar_paises)`
- [x] Lista de `dict` `(toda la app)`
- [x] Decisión documentada `(decisiones_tecnicas.md §3)`

### II.3 Modularidad
- [x] Un archivo por responsabilidad `(src/)`
- [x] Una sola tarea por función
- [x] Funciones cortas
- [x] Sin lógica duplicada `(validaciones.py centraliza inputs)`

### II.4 Manejo CSV
- [x] `try/except` en lectura `(csv_manager.py :: cargar_paises)`
- [x] Conversión segura `(int(...))` con manejo de `ValueError`
- [x] Filas inválidas con advertencia `(csv_manager.py)`
- [x] Escritura UTF-8 con cabecera `(csv_manager.py :: guardar_paises)`

### II.5 Lógica condicional y orden
- [x] Rangos inclusivos `(filtros.py)`
- [x] Múltiples criterios `(ordenamientos.py)`
- [x] Asc/desc `(ordenamientos.py :: pedir_direccion)`
- [x] Estabilidad documentada → **agregar línea** en `decisiones_tecnicas.md` §8.

### II.6 Legibilidad
- [x] Nombres en español
- [x] Docstring breve por función
- [x] Estilo consistente
- [x] Comentarios solo cuando el *por qué* no es obvio

### II.7 Manejo de errores
- [x] `try/except` en cada `input()` numérico `(validaciones.py :: pedir_entero)`
- [x] `try/except` en CSV `(csv_manager.py)`
- [x] Sin `except:` desnudo `(Hito E)`
- [x] Mensajes en español con prefijos unificados
- [x] El programa nunca cae por entrada inválida

### Bloques sin tildar
- **I** (Marco teórico, fuentes, conclusiones) → depende del PDF.
- **III.1** (Estructura digital) → tildable hoy.
- **III.2** (Repo, README, tag `v1.0`) → README pendiente; tag al final.
- **III.3** (Video) → pendiente.
- **Reglas excluyentes**: tildar las que dependen de código (CSV
  versionado, programa ejecutable, repo público).

---

## 6. Plan de actualización — `docs/auditoria_final_pre_entrega.md`

**Dejar como está.** El documento es una foto del código *antes* del
Hito E y tiene valor histórico para la defensa oral ("sabíamos qué
había que pulir y lo aplicamos"). Reescribirlo destruiría esa
trazabilidad.

Acción opcional (1 línea al final, antes del cierre):

> **Estado post-Hito E:** todos los hallazgos *Recomendado* (1, 2, 3,
> 4, 5, 6, 7, 8, 9, 11, 23) se aplicaron. Trazabilidad en
> `docs/informe_mejoras_pendientes.md`.

---

## 7. Plan de actualización — `docs/plan_feature_core_functionality.md`

**Dejar como está.** Es el plan de implementación de la rama: registro
histórico que muestra que el equipo planifica antes de codear.
Consistente con `PLAN_DESARROLLO.md` y con la auditoría.

Acción opcional (1 línea al final):

> **Estado:** Hitos A, B, C, D y E completados. Rama lista para PR.

---

## 8. Commits sugeridos

Dos commits separados para facilitar la revisión del PR:

1. **`docs: actualizar README y decisiones técnicas para entrega final`**
   - `README.md` (estado, estructura, módulos, ejemplos).
   - `docs/decisiones_tecnicas.md` (secciones 8–13).

2. **`docs: cerrar mejoras pendientes y checklist de nota máxima`**
   - `docs/informe_mejoras_pendientes.md` (marcadores de estado).
   - `docs/objetivo_nota_maxima.md` (ítems II tildados con evidencia).
   - Notas de cierre opcionales en `auditoria_final_pre_entrega.md` y
     `plan_feature_core_functionality.md`.

Si se prefiere un único commit: **`docs: actualizar documentación
final para PR de feature/core-functionality`**.

---

## 9. Recomendación sobre el PR

**Abrir el PR después de actualizar README y decisiones técnicas.**

Justificación:
- El código está completo, probado y consistente. No hay razón para
  bloquear el PR esperando el video o el PDF.
- El `README.md` actual indica "*en desarrollo*" y lista
  `csv_utils.py`: cualquier revisor (incluido el docente que mire el
  repo en GitHub) lo notará. **Es bloqueante**.
- Las decisiones de la auditoría que pueden aparecer en la defensa
  (`if/elif` vs dict, sin `mensajes.py`, sin tildes en filtros)
  conviene que estén escritas antes del PR para no quedar "a defender
  oralmente".
- Los demás docs (`informe_mejoras_pendientes.md`,
  `objetivo_nota_maxima.md`) son **deseables pero no bloqueantes**
  para el PR; pueden ir en un segundo commit dentro de la misma rama
  o en una rama corta posterior `docs/cierre-final`.
- Los enlaces a video y PDF son **placeholders aceptables**: se
  reemplazan cuando estén listos, sin necesidad de re-abrir PR.

**Resumen de prioridad:**

| Acción | Antes del PR | Después del PR |
|---|---|---|
| Actualizar `README.md` | ✅ obligatorio | — |
| Actualizar `decisiones_tecnicas.md` | ✅ recomendado | aceptable |
| Marcar `informe_mejoras_pendientes.md` | aceptable | ✅ |
| Tildar `objetivo_nota_maxima.md` (II) | aceptable | ✅ |
| Notas de cierre en auditoría/plan | opcional | opcional |
| Video y PDF | — | ✅ (post-grabación) |
| Tag `v1.0` | — | ✅ (entrega final) |
