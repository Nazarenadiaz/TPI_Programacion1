# Objetivo: nota máxima

> Checklist en español alineada con la rúbrica oficial (`docs/rubrica_evaluacion.md`).
> Cada ítem marca lo que el equipo se compromete a cumplir para apuntar a **Excelente (100%)**.
> Se actualiza durante el desarrollo: marcar `[x]` cuando esté cubierto y anotar la evidencia (archivo, función o sección que lo respalda).

---

## I. Marco Teórico e Investigación (30%)

### Marco teórico — Conceptos fundamentales (15 pts)
- [ ] Listas: definidas y vinculadas al proyecto (colección de países).
- [ ] Diccionarios: definidos y vinculados al proyecto (representación de un país).
- [ ] Funciones: definidas y vinculadas a la modularización del código.
- [ ] Condicionales: definidos y vinculados a filtros, validaciones y menú.
- [ ] Ordenamientos: definidos y vinculados al módulo de ordenamientos.
- [ ] Estadísticas: definidas y vinculadas al módulo de estadísticas.
- [ ] Archivos CSV: definidos y vinculados a la persistencia del dataset.
- **Evidencia esperada:** capítulo "Marco Teórico" del informe PDF.

### Fuentes bibliográficas (10 pts)
- [ ] Al menos **3 fuentes** académicas o técnicas pertinentes.
- [ ] Citas correctamente formateadas (autor, título, año, URL si aplica).
- **Evidencia esperada:** sección "Bibliografía / Webgrafía" del informe PDF.

### Conclusiones (5 pts)
- [ ] Aprendizajes claros sobre estructuras de datos.
- [ ] Aprendizajes claros sobre modularidad.
- [ ] Aprendizajes claros sobre estadísticas.
- [ ] Reflexión grupal (no genérica) sobre dificultades y soluciones.
- **Evidencia esperada:** sección "Dificultades y Conclusiones" del informe PDF.

---

## II. Desarrollo del Software (60%)

### Funcionalidad (20 pts)
- [ ] Carga de CSV con manejo de errores.
- [ ] Agregar país con validaciones.
- [ ] Actualizar población y superficie de un país existente.
- [ ] Búsqueda por nombre (parcial y exacta, insensible a mayúsculas).
- [ ] Filtro por continente.
- [ ] Filtro por rango de población.
- [ ] Filtro por rango de superficie.
- [ ] Ordenamiento por nombre / población / superficie (asc/desc).
- [ ] Estadísticas: mayor población, menor población, promedio de población, promedio de superficie, conteo por continente.
- [ ] Robustez ante entradas inválidas y resultados vacíos.

### Estructuras de datos (10 pts)
- [ ] País modelado como `dict` con claves `nombre`, `poblacion`, `superficie`, `continente`.
- [ ] Colección de países como `list` de `dict`.
- [ ] Decisión justificada en `docs/decisiones_tecnicas.md`.

### Modularidad y funciones (10 pts)
- [ ] Un archivo `.py` por responsabilidad en `src/`.
- [ ] Cada función cumple **una sola tarea**.
- [ ] Funciones cortas (~30 líneas como referencia).
- [ ] Sin lógica duplicada entre módulos.

### Manejo de archivos CSV (5 pts)
- [ ] Lectura con `try/except` y manejo de archivo inexistente.
- [ ] Conversión segura de tipos (`int` para población y superficie).
- [ ] Filas incompletas o inválidas se ignoran con advertencia clara.
- [ ] Escritura con UTF-8 y cabecera consistente.

### Lógica condicional y ordenamiento (5 pts)
- [ ] Filtros precisos (rangos inclusivos `mín <= valor <= máx`).
- [ ] Ordenamientos por múltiples criterios.
- [ ] Soporte de orden ascendente y descendente.
- [ ] Sin comportamientos sorpresivos al ordenar (estabilidad documentada).

### Legibilidad y comentarios (5 pts)
- [ ] Nombres en español descriptivos.
- [ ] Docstring breve al inicio de cada función.
- [ ] Comentarios solo donde el *por qué* no es obvio.
- [ ] Estilo consistente (indentación 4 espacios, líneas razonables).

### Manejo de errores (5 pts)
- [ ] `try/except` en cada `input()` numérico.
- [ ] `try/except` en lectura y escritura del CSV.
- [ ] Sin `except:` desnudo (capturar excepciones específicas).
- [ ] Mensajes claros y específicos en español (`OK,` / `ERROR,` / `ADVERTENCIA,`).
- [ ] El programa nunca cae por una entrada inválida.

---

## III. Entregables y Presentación (10%)

### Carpeta digital (3 pts)
- [ ] Estructura `src/`, `data/`, `docs/` aplicada.
- [ ] `docs/` contiene marco teórico (vía PDF), código (vía `src/`), capturas (en informe) y conclusiones.

### Repositorio GitHub (4 pts)
- [ ] Repositorio **público** antes de la entrega.
- [ ] `README.md` detallado con descripción, requisitos, cómo ejecutar, ejemplos por funcionalidad, integrantes, link al video, link al PDF.
- [ ] Historial de commits ordenado, ramas por feature mergeadas a `main`.
- [ ] Tag `v1.0` en el commit de entrega.

### Video tutorial (3 pts)
- [ ] Duración entre **10 y 15 minutos**.
- [ ] **Ambos integrantes** aparecen a cámara al inicio.
- [ ] Explicación teórica + demostración completa del programa.
- [ ] Link público funcionando, incluido en `README.md`.

---

## Reglas excluyentes (no fallar nunca)
- [ ] Video presente y dentro del rango 10–15 min.
- [ ] Ambos integrantes a cámara al inicio del video.
- [ ] Repositorio público.
- [ ] CSV base versionado en `data/paises.csv`.
- [ ] Proyecto ejecutable: `python src/main.py` corre sin errores.
