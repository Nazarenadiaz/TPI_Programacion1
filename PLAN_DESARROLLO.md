# Plan de Desarrollo — TPI Programación 1

> Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas.
> Documento de planificación. **No modifica código fuente todavía.**
> Alineado con `consigna.md` y `rubrica_de_evaluacion.md`.

---

## 0. Objetivo del plan

Llevar el repositorio desde su estado actual (estructura plana, funcionalidades incompletas, documentación mínima) hasta una entrega que **apunte a la calificación "Excelente (100%)"** definida en la rúbrica, manteniendo el código simple y explicable para una materia de Programación 1.

Cada paso del plan referencia el ítem de la rúbrica que ayuda a cubrir, para que el equipo sepa *por qué* hace cada cosa.

---

## 1. Diagnóstico del proyecto actual

### 1.1 Archivos existentes y responsabilidades probables

| Archivo | Responsabilidad detectada | Estado |
|---|---|---|
| `main.py` | Punto de entrada, menú principal y despacho de opciones. | Funcional. Opciones 6, 7 y 8 están como `MODULO PENDIENTE`. |
| `csv_utils.py` | Lectura/escritura del CSV y `agregar_pais` (alta con validaciones). | Funcional. Mezcla I/O de CSV con lógica de alta de país. |
| `busquedas.py` | `buscar_pais` (búsqueda parcial/insensible a mayúsculas) y `mostrar_paises` (impresión tabular). | Funcional. La utilidad de presentación `mostrar_paises` vive aquí pero la usan otros módulos. |
| `filtros.py` | Filtros por continente, rango de población y rango de superficie. | Funcional. Importa `mostrar_paises` desde `busquedas`. |
| `paises.csv` | Dataset base con cabeceras `nombre,poblacion,superficie,continente`. | OK (8 países de ejemplo). |
| `README.md` | Solo contiene el título del repo. | **Vacío de contenido**, hay que completarlo. |

### 1.2 Módulos / responsabilidades faltantes

Comparando con la consigna, faltan:

- **Actualizar país** (opción 6): cambiar población y superficie por nombre.
- **Ordenar países** (opción 7): por nombre, población o superficie, ascendente o descendente.
- **Estadísticas** (opción 8): país con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente.
- **Validaciones reutilizables**: hoy las validaciones (numéricas, no vacío, rango mín/máx) están repetidas en `csv_utils.py` y `filtros.py`. Conviene un módulo `validaciones.py`.
- **Capa de presentación de menú**: el menú vive dentro de `main.py`. Para mantener `main.py` chico conviene un `menu.py`.
- **Documentación**: README real, informe PDF, decisiones técnicas y enlace al video.

### 1.3 Riesgos e inconsistencias detectadas

- **Acoplamiento de presentación**: `mostrar_paises` está en `busquedas.py` pero la usan los filtros (y la usarán ordenamientos y estadísticas). Es una utilidad de UI que conviene mover a `paises.py` o a un módulo de presentación.
- **Mezcla de I/O y lógica de dominio**: `csv_utils.py` contiene `agregar_pais`, que pide datos por consola, valida y además persiste. Conviene separar: dominio (`paises.py`), persistencia (`csv_manager.py`) y entrada/validación (`validaciones.py`).
- **Sin `.gitignore`**: aparecerán carpetas `__pycache__/`, `.venv/` y archivos del editor en commits.
- **README vacío**: la consigna lo exige con descripción, instrucciones de uso, ejemplos y participación de los integrantes.
- **Codificación de caracteres**: el CSV usa tildes (`América`, `Á`frica). Hay que asegurar `encoding="utf-8"` en todas las lecturas/escrituras (ya está OK en `csv_utils.py`).
- **Validación de superficie negativa al actualizar**: cuando se implemente la actualización, hay que reusar las mismas validaciones que en alta.
- **Comparación de continentes**: hoy `filtrar_por_continente` compara con `==` insensible a mayúsculas pero los acentos dependen de cómo escriba el usuario (`America` vs `América`). Conviene normalizar (al menos documentar la limitación).

---

## 2. Estructura objetivo del repositorio

### 2.1 Estructura actual (plana)

```
TPI_Programacion1/
├── busquedas.py
├── csv_utils.py
├── filtros.py
├── main.py
├── paises.csv
└── README.md
```

### 2.2 Estructura objetivo (decidida)

```
TPI_Programacion1/
│
├── data/
│   └── paises.csv
│
├── src/
│   ├── main.py
│   ├── menu.py
│   ├── csv_manager.py
│   ├── paises.py
│   ├── busquedas.py
│   ├── filtros.py
│   ├── ordenamientos.py
│   ├── estadisticas.py
│   └── validaciones.py
│
├── docs/
│   ├── consigna.md
│   ├── consigna.pdf
│   ├── rubrica_evaluacion.md
│   ├── rubrica_evaluacion.pdf
│   ├── decisiones_tecnicas.md
│   ├── objetivo_nota_maxima.md
│   └── informe.pdf                  (al final del proyecto)
│
├── README.md
├── .gitignore
└── PLAN_DESARROLLO.md
```

> **Decisión adoptada:** se trabaja con esta estructura desde el inicio del proyecto. La migración se hace **ahora**, en la primera fase, mientras el código es chico y mover archivos cuesta poco.

### 2.3 Justificación de cada carpeta y archivo

**Carpeta `data/`**
- Aísla los datos del código. Si mañana se agregan más datasets o se reemplaza el CSV, el cambio queda contenido.
- Hace obvio en el video y en el informe PDF dónde están los datos.

**Carpeta `src/`**
- Separa el código fuente de la documentación y los datos.
- Permite que `README.md` y `PLAN_DESARROLLO.md` queden visibles en la raíz del repositorio (lo primero que ve el evaluador en GitHub).
- Evita que `__pycache__/` ensucie la raíz.

**Carpeta `docs/`**
- Centraliza toda la documentación académica y técnica.
- Mantiene la raíz del repo limpia (solo README, plan, `.gitignore`).
- Permite al evaluador encontrar consigna, rúbrica e informe en un solo lugar.

**Archivos `src/*`**
- `main.py`: punto de entrada mínimo. Solo orquesta carga de datos y arranque del menú.
- `menu.py`: dibuja el menú y resuelve la opción elegida.
- `csv_manager.py`: solo lectura/escritura del CSV. Sin `input()` ni lógica de negocio.
- `paises.py`: operaciones de dominio sobre la lista de países (alta, actualización) y utilidad `mostrar_paises`.
- `busquedas.py`: búsqueda por nombre (parcial/exacta).
- `filtros.py`: filtros por continente y por rango.
- `ordenamientos.py`: ordenar por nombre / población / superficie, asc/desc.
- `estadisticas.py`: máximos, mínimos, promedios y conteos por continente.
- `validaciones.py`: helpers de validación reutilizables (`pedir_entero`, `pedir_texto_no_vacio`, `validar_rango`).

**Archivos `docs/*`**
- `consigna.md` y `consigna.pdf`: copia versionada de la consigna oficial, para que el repo sea autocontenido.
- `rubrica_evaluacion.md` y `rubrica_evaluacion.pdf`: rúbrica oficial. Sirve de checklist de calidad.
- `decisiones_tecnicas.md`: bitácora corta de decisiones (por qué diccionarios y no clases, por qué `csv` estándar, manejo de tildes, etc.). Insumo directo del informe PDF.
- `objetivo_nota_maxima.md`: mapa explícito entre lo que pide la rúbrica para "Excelente (100%)" y lo que el equipo se compromete a entregar.
- `informe.pdf`: documento académico final (carátula, índice, marco teórico, decisiones técnicas, dificultades, bibliografía, links).

**Raíz**
- `README.md`: descripción, requisitos, instrucciones de uso, ejemplos, integrantes, link al video, link al PDF.
- `.gitignore`: ignora `__pycache__/`, `.venv/`, `.DS_Store`, `*.pyc`.
- `PLAN_DESARROLLO.md`: este documento.

### 2.4 Por qué migrar ahora y no al final

1. **Costo bajo ahora, alto después**: hoy hay 4 archivos `.py` y casi cero dependencias entre ellos. Mover y arreglar los `import` es un commit chico. Al final del proyecto habrá ~9 módulos y mover todo cerca de la entrega es riesgo innecesario.
2. **Evita reescribir rutas dos veces**: si el CSV se mueve a `data/` al final, hay que tocar `csv_utils.py`, `main.py` y posibles módulos nuevos. Hecho ahora, los módulos nuevos ya nacen con la ruta correcta.
3. **Disciplina desde el día uno**: con `src/` y `data/` definidos, el equipo no tiene que decidir dónde poner cada archivo nuevo.
4. **Mejor demo en video**: una estructura ordenada se explica en 30 segundos. Una raíz con 15 archivos sueltos no.
5. **Cubre criterios de la rúbrica desde el principio**: "Modularidad y Funciones (10 pts)" y "Repositorio GitHub (4 pts)" se benefician de tener carpetas claras desde el primer commit.

### 2.5 Resolución técnica de la migración

- Ejecutar el programa **desde la raíz del repo**: `python src/main.py`.
- Para leer el CSV sin depender del directorio de trabajo, calcular la ruta así:
  ```python
  import os
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  RUTA_CSV = os.path.join(BASE_DIR, "data", "paises.csv")
  ```
- Documentar en el README el comando exacto: `python src/main.py`.
- No usar `__init__.py` ni paquetes: los `import` siguen siendo simples (`from menu import ...`) porque `src/` es el directorio del script de entrada.

---

## 3. Estrategia de ramas

Flujo simple basado en `main`. Una rama por paquete de trabajo, merge con Pull Request o merge local cuando esté revisado por ambos integrantes.

```
main
 ├── chore/project-analysis-plan          (este documento)
 ├── chore/repo-structure                 (migración a src/, data/, docs/)
 ├── feature/menu-and-flow                (menu.py + main.py limpio)
 ├── feature/csv-validations              (csv_manager.py + validaciones.py)
 ├── feature/country-crud                 (paises.py: alta + actualización)
 ├── feature/search-and-filters           (revisión de busquedas.py y filtros.py)
 ├── feature/sorting-and-statistics       (ordenamientos.py + estadisticas.py)
 └── docs/readme-and-final-report         (README final, informe PDF, link video)
```

Reglas:
- Todas las ramas salen de `main` actualizado.
- Commits pequeños y descriptivos, consistentes en idioma (español o inglés, elegir uno).
- Antes de mergear: probar manualmente todas las opciones del menú con `python src/main.py`.
- Tag `v1.0` al cerrar la entrega.

---

## 4. Hoja de ruta de implementación

> Cada paso indica los **ítems de la rúbrica** que ayuda a cubrir (entre paréntesis).

### Paso 0 — `chore/project-analysis-plan`
- **Objetivo**: dejar el plan documentado.
- **Archivos**: `PLAN_DESARROLLO.md`.
- **Resultado esperado**: plan revisado por ambos integrantes.
- **Aporte a la rúbrica**: II.3 Modularidad (define la organización), III.2 Repositorio.
- **Checklist manual**:
  - [ ] El archivo existe en la raíz.
  - [ ] Ambos integrantes lo leyeron y aceptaron.

### Paso 1 — `chore/repo-structure` (FASE DE ORGANIZACIÓN)
- **Objetivo**: dejar el repositorio con la estructura final de carpetas **antes** de tocar lógica nueva.
- **Acciones**:
  - Crear carpetas `src/`, `data/`, `docs/`.
  - Mover los `.py` actuales a `src/`:
    - `main.py` → `src/main.py`
    - `csv_utils.py` → `src/csv_utils.py` (se renombrará a `csv_manager.py` en el Paso 3).
    - `busquedas.py` → `src/busquedas.py`
    - `filtros.py` → `src/filtros.py`
  - Mover el dataset: `paises.csv` → `data/paises.csv`.
  - Ajustar la ruta del CSV en `csv_utils.py` con `os.path` calculado desde `__file__` (ver § 2.5). **Es el único cambio de código permitido en este paso**: hacer que el programa siga ejecutándose desde la nueva ubicación.
  - Copiar la consigna y la rúbrica a `docs/`:
    - `consigna.md`, `consigna.pdf` (exportar desde el MD).
    - `rubrica_evaluacion.md`, `rubrica_evaluacion.pdf`.
  - Crear documentos guía:
    - `docs/decisiones_tecnicas.md` (bitácora viva de decisiones técnicas).
    - `docs/objetivo_nota_maxima.md` (mapa rúbrica ↔ acciones, ver § 5).
  - Crear `.gitignore` en la raíz (`__pycache__/`, `.venv/`, `.DS_Store`, `*.pyc`, `.idea/`, `.vscode/`).
  - Reemplazar el `README.md` mínimo por una versión inicial con: título, descripción breve, requisitos (Python 3.12), cómo ejecutar (`python src/main.py`), estructura del proyecto, integrantes (placeholders) y secciones reservadas para video y PDF.
- **Resultado esperado**: el programa funciona exactamente igual que antes ejecutado con `python src/main.py` y el repo ya tiene la estructura final.
- **Aporte a la rúbrica**: III.1 Carpeta digital, III.2 Repositorio (README inicial), II.3 Modularidad (carpetas claras).
- **Checklist manual**:
  - [ ] `python src/main.py` arranca y muestra el menú.
  - [ ] Se cargan los 8 países desde `data/paises.csv`.
  - [ ] Las opciones existentes (1, 2, 3, 4, 5) siguen funcionando igual.
  - [ ] `docs/` contiene consigna, rúbrica, `decisiones_tecnicas.md` y `objetivo_nota_maxima.md`.
  - [ ] `.gitignore` impide que `__pycache__/` aparezca en `git status`.
  - [ ] El README inicial explica cómo correr el programa.

### Paso 2 — `feature/menu-and-flow`
- **Objetivo**: separar el menú de `main.py` y dejar `main.py` mínimo.
- **Archivos**:
  - Nuevo: `src/menu.py` (función `mostrar_menu`, función `ejecutar_opcion(opcion, paises)`).
  - Modificar: `src/main.py` (solo carga datos y delega).
- **Resultado**: el programa arranca y muestra el menú igual que antes.
- **Aporte a la rúbrica**: II.3 Modularidad (10 pts), II.6 Legibilidad (5 pts).
- **Checklist manual**:
  - [ ] El menú se muestra correctamente.
  - [ ] La opción 0 sale del programa.
  - [ ] Una opción inválida muestra mensaje de error claro.

### Paso 3 — `feature/csv-validations`
- **Objetivo**: separar persistencia y validaciones.
- **Archivos**:
  - Renombrar: `src/csv_utils.py` → `src/csv_manager.py`. Solo `cargar_paises` y `guardar_paises`.
  - Nuevo: `src/validaciones.py` con `pedir_entero(mensaje, minimo=None)`, `pedir_texto_no_vacio(mensaje)`, `validar_rango(min_, max_)`.
- **Resultado**: el CSV sigue cargando OK; los módulos piden datos validados sin duplicar código.
- **Aporte a la rúbrica**: II.4 CSV (5 pts), II.7 Manejo de errores (5 pts), II.3 Modularidad.
- **Checklist manual**:
  - [ ] Cargar `data/paises.csv` muestra los 8 países.
  - [ ] Una fila incompleta del CSV se ignora con advertencia.
  - [ ] `pedir_entero` rechaza letras y vacíos.

### Paso 4 — `feature/country-crud`
- **Objetivo**: implementar alta (mover desde `csv_utils.py`) y actualización (opción 6).
- **Archivos**:
  - Nuevo: `src/paises.py` con `agregar_pais`, `actualizar_pais`, `mostrar_paises`.
  - Modificar: `src/menu.py` para invocar `actualizar_pais` en la opción 6.
- **Resultado**: opciones 1 y 6 funcionan completas.
- **Aporte a la rúbrica**: II.1 Funcionalidad (20 pts), II.2 Estructuras de datos (10 pts).
- **Checklist manual**:
  - [ ] Alta de país nuevo funciona y persiste en `data/paises.csv`.
  - [ ] Alta rechaza nombre duplicado, vacío y números negativos.
  - [ ] Actualización de un país existente cambia los valores y los persiste.
  - [ ] Actualización de un país inexistente muestra error claro.

### Paso 5 — `feature/search-and-filters`
- **Objetivo**: consolidar los módulos de búsqueda y filtros.
- **Archivos**: `src/busquedas.py`, `src/filtros.py`.
- **Cambios**:
  - Mover `mostrar_paises` a `paises.py` y actualizar imports.
  - Confirmar búsqueda parcial e insensible a mayúsculas.
  - Confirmar manejo de filtros sin resultados.
- **Resultado**: opciones 2, 3, 4 y 5 estables.
- **Aporte a la rúbrica**: II.1 Funcionalidad, II.5 Lógica condicional (5 pts).
- **Checklist manual**:
  - [ ] Búsqueda con coincidencia parcial encuentra "arg" → Argentina.
  - [ ] Búsqueda sin coincidencias muestra mensaje claro.
  - [ ] Filtro por continente inexistente devuelve mensaje claro.
  - [ ] Filtros por rango aceptan límites iguales (mín == máx).

### Paso 6 — `feature/sorting-and-statistics`
- **Objetivo**: completar opciones 7 y 8.
- **Archivos**:
  - Nuevo: `src/ordenamientos.py` con `ordenar_paises(paises, criterio, ascendente)`.
  - Nuevo: `src/estadisticas.py` con `pais_mayor_poblacion`, `pais_menor_poblacion`, `promedio_poblacion`, `promedio_superficie`, `cantidad_por_continente`, `mostrar_estadisticas`.
- **Resultado**: el menú está 100% funcional.
- **Aporte a la rúbrica**: II.1 Funcionalidad, II.5 Lógica condicional y ordenamiento.
- **Checklist manual**:
  - [ ] Ordenar por nombre asc y desc da resultados correctos.
  - [ ] Ordenar por población y superficie en ambos sentidos funciona.
  - [ ] Estadísticas muestran país con mayor/menor población correctamente.
  - [ ] Promedios coinciden con cálculo manual sobre el CSV.
  - [ ] Conteo por continente coincide con el dataset.

### Paso 7 — `docs/readme-and-final-report`
- **Objetivo**: cerrar la entrega académica.
- **Archivos**:
  - `README.md` final (descripción completa, ejemplos por funcionalidad, integrantes, link al video, link al PDF).
  - `docs/decisiones_tecnicas.md` actualizado con todo lo decidido.
  - `docs/objetivo_nota_maxima.md` con autoevaluación contra la rúbrica.
  - `docs/informe.pdf` (formato profesional, carátula, índice, marco teórico, decisiones técnicas, diagrama de flujo, dificultades, bibliografía, links).
- **Resultado**: repositorio listo para zipear y entregar.
- **Aporte a la rúbrica**: I (Marco teórico, 30%), III (Entregables, 10%).
- **Checklist manual**:
  - [ ] README explica cómo correr `python src/main.py`.
  - [ ] README incluye al menos un ejemplo por funcionalidad.
  - [ ] PDF respeta carátula, índice, marco teórico, decisiones técnicas, dificultades, bibliografía y links.
  - [ ] Video sube a una plataforma con permiso público y el link funciona.

---

## 5. Conexión con la rúbrica de evaluación

Mapa explícito entre cada criterio puntuado y las acciones del plan que lo cubren. Esta tabla también es la base de `docs/objetivo_nota_maxima.md`.

| Bloque | Criterio (puntos) | Acciones del plan que apuntan a "Excelente (100%)" |
|---|---|---|
| I.1 | Conceptos fundamentales (15) | Marco teórico del PDF redactado a partir de `docs/decisiones_tecnicas.md`, cubriendo listas, diccionarios, funciones, condicionales, ordenamientos, estadísticas y CSV, vinculados al proyecto real. |
| I.2 | Fuentes bibliográficas (10) | Recopilar 3 o más fuentes (docs oficiales de Python sobre `csv`, listas, dicts; bibliografía de la cátedra) y citarlas correctamente en el PDF. |
| I.3 | Conclusiones (5) | Sección de conclusiones del PDF con aprendizajes sobre estructuras de datos, modularidad y estadísticas, no genérica. |
| II.1 | Funcionalidad (20) | Pasos 4, 5 y 6: las 8 funcionalidades del menú funcionan y son robustas (sin resultados, rangos inválidos, archivos faltantes). |
| II.2 | Estructuras de datos (10) | Decisión documentada: lista de diccionarios. Justificada en `decisiones_tecnicas.md`. |
| II.3 | Modularidad y funciones (10) | Estructura `src/` con un archivo por responsabilidad. Funciones cortas con una sola tarea (ver § 6 Convenciones). |
| II.4 | Manejo de CSV (5) | `csv_manager.py` con `try/except`, validación de filas incompletas, conversión segura de tipos. Ya parcialmente implementado en `csv_utils.py`. |
| II.5 | Lógica condicional y ordenamiento (5) | `ordenamientos.py` con criterio + dirección. Filtros con condicionales claras. |
| II.6 | Legibilidad y comentarios (5) | Nombres en español descriptivos, docstrings breves, comentarios solo donde el *por qué* no es obvio. |
| II.7 | Manejo de errores (5) | `try/except` en `input()` numéricos, en lectura/escritura del CSV, mensajes claros en español con prefijo `ERROR,`. |
| III.1 | Carpeta digital (3) | Estructura `src/`, `data/`, `docs/` desde el Paso 1. `docs/` reúne marco teórico, capturas y conclusiones. |
| III.2 | Repositorio GitHub (4) | Repo público, README detallado con instrucciones, ejemplos, integrantes y links. Historial limpio de commits por feature. |
| III.3 | Video tutorial (3) | 10–15 min, ambos integrantes a cámara desde el inicio, explicación teórica + demo completa de todas las funcionalidades. |

### Reglas excluyentes (no fallar nunca)
- [ ] El video dura entre 10 y 15 minutos.
- [ ] Ambos integrantes aparecen a cámara al inicio del video.
- [ ] El repositorio es público antes de la entrega.
- [ ] El CSV base está versionado en `data/paises.csv`.
- [ ] El proyecto se ejecuta sin errores con `python src/main.py`.

---

## 6. Development Conventions

Convenciones obligatorias del proyecto. Todo código y documentación nuevos deben respetarlas.

### Lenguaje y herramientas
- **Python 3.12** (intérprete oficial del proyecto).
- **Sin librerías externas**: solo biblioteca estándar (`csv`, `os`, etc.).
- **Sin base de datos**: persistencia únicamente sobre `data/paises.csv`.
- **Sin clases** salvo que sea estrictamente necesario.

### Estructuras de datos
- **Listas y diccionarios** como estructuras principales.
- Cada país es un `dict` con claves `nombre`, `poblacion`, `superficie`, `continente`.
- La colección de países es una `list` de esos `dict`.

### Funciones
- **Una función = una responsabilidad**. Si una función supera ~30 líneas o hace dos cosas, dividirla.
- Nombres descriptivos en español (`agregar_pais`, `filtrar_por_continente`).
- Docstring breve al inicio de cada función explicando qué hace.

### Estilo de código
- **Prefiere soluciones simples a soluciones inteligentes**: comprensible antes que cortita o "elegante".
- **Legibilidad sobre optimización**: el evaluador y el equipo tienen que poder leer y explicar cada línea en el video.
- Indentación de 4 espacios, líneas razonablemente cortas.

### Idioma
- **Identificadores**: pueden quedar en español (ya es el estilo del proyecto).
- **Comentarios**: en español.
- **Documentación** (`README.md`, `docs/*.md`, PDF): en español.
- **Mensajes al usuario** (consola): en español, claros, con prefijos consistentes (`OK,`, `ERROR,`, `ADVERTENCIA,`).
- **Video**: en español.
- **Commits**: español o inglés, consistente a lo largo del proyecto.

### Manejo de errores
- **Mensajes claros y específicos**: indicar qué falló y qué se esperaba.
- `try/except` en cada punto donde el usuario ingresa datos numéricos.
- `try/except` en lectura y escritura del CSV.
- No usar `except:` desnudo: capturar excepciones específicas (`ValueError`, `OSError`).
- Nunca dejar caer el programa por una entrada inválida del usuario.

---

## 7. Reparto sugerido entre integrantes

> Reparto justo. Los dos tocan código, README, PDF y video.

### Estudiante A — *Dominio y datos*
- Pasos 3 y 4: `csv_manager.py`, `validaciones.py`, `paises.py` (alta y actualización).
- Sección del informe PDF: marco teórico (listas, diccionarios, archivos CSV) y decisiones técnicas de persistencia.
- En el video: explica el flujo de carga del CSV, alta y actualización.

### Estudiante B — *Consultas, ordenamientos y estadísticas*
- Pasos 5 y 6: revisión de `busquedas.py`/`filtros.py`, `ordenamientos.py`, `estadisticas.py`.
- Sección del informe PDF: marco teórico (condicionales, ordenamientos, estadísticas) y diagrama de flujo del menú.
- En el video: explica búsquedas, filtros, ordenamientos y estadísticas.

### Trabajo compartido
- Paso 1 (migración a `src/`+`data/`+`docs/`), Paso 2 (`menu.py`) y Paso 7 (README, PDF final) los firman ambos.
- Code review cruzado en cada Pull Request antes de mergear a `main`.
- Edición y grabación del video: ambos hablan en partes equivalentes y aparecen a cámara desde el inicio.

---

## 8. Definición de terminado (Definition of Done)

El proyecto está completo cuando **todos** los puntos siguientes están tildados.

### Funcionalidad
- [ ] El menú muestra y ejecuta correctamente las 9 opciones (0 a 8).
- [ ] Agregar país valida nombre, población, superficie y continente, y persiste en `data/paises.csv`.
- [ ] Actualizar país encuentra por nombre y permite cambiar población y superficie.
- [ ] Búsqueda por nombre soporta coincidencia parcial (insensible a mayúsculas).
- [ ] Filtros por continente, rango de población y rango de superficie funcionan y manejan resultados vacíos.
- [ ] Ordenamiento por nombre, población y superficie, ascendente y descendente.
- [ ] Estadísticas: mayor y menor población, promedio de población, promedio de superficie y cantidad por continente.

### Calidad de código
- [ ] Cada módulo de `src/` tiene una responsabilidad clara.
- [ ] Sin clases (salvo justificación) y sin librerías externas.
- [ ] Funciones cortas, con docstring breve.
- [ ] Manejo de errores con mensajes claros en cada `input()` numérico y en lectura del CSV.
- [ ] Cumple las convenciones de la sección 6.

### Repositorio
- [ ] Estructura `src/`, `data/`, `docs/` aplicada y respetada.
- [ ] `README.md` en español con descripción, requisitos, instrucciones de uso, ejemplos, integrantes, link al video y link al PDF.
- [ ] `.gitignore` presente y efectivo.
- [ ] `data/paises.csv` con datos válidos.
- [ ] `docs/` contiene `consigna.*`, `rubrica_evaluacion.*`, `decisiones_tecnicas.md`, `objetivo_nota_maxima.md` y `informe.pdf`.
- [ ] Historial de commits ordenado, ramas por feature mergeadas a `main`.
- [ ] Tag `v1.0` en el commit de entrega.
- [ ] Repositorio público.

### Entregables académicos
- [ ] Informe PDF en español con carátula, índice, marco teórico, decisiones técnicas y diagrama de flujo, dificultades, bibliografía y links.
- [ ] Video en español de 10 a 15 minutos, público, mostrando todos los flujos, con ambos integrantes a cámara desde el inicio.
- [ ] ZIP final con código fuente + PDF.
- [ ] Participación equitativa documentada en README y video.

### Autoevaluación contra la rúbrica
- [ ] `docs/objetivo_nota_maxima.md` actualizado, con cada criterio marcado como cubierto y con evidencia (archivo, función o sección que lo respalda).
- [ ] Las 5 reglas excluyentes de la rúbrica están verificadas (ver § 5).
