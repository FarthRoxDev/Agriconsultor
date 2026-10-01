# Agriconsultor 🌱

**Asistente agronómico de precisión para Costa Rica.** Un copiloto técnico que
*cita, calcula y registra* — no improvisa. Combina una base de conocimiento
agronómico verificable, herramientas de cálculo en Python y datos estructurados
(parámetros de cultivo, estacionalidad, suelos, clima, precios) más las bitácoras
de finca del usuario.

Está pensado para usarse con **Claude Code** sobre este repositorio (y, más
adelante, exponerse por **MCP** a otros clientes). El comportamiento del asistente
lo define [`CLAUDE.md`](./CLAUDE.md).

## Para qué sirve
- Responder consultas agronómicas con criterio **local** (zona, altitud, vertiente).
- Calcular de forma **auditable**: fertilización, riego (ET·Kc), densidades,
  grados-día, índices de vegetación (NDVI/NDRE/GNDVI…), economía.
- Cubrir **todo el ciclo** de los cultivos comerciales de CR (alimentación,
  agroexportación) y de **floristería** (follajes, flores, ornamentales).
- Llevar **registros de finca** en bases de datos propias.

## Cómo está organizado
```
CLAUDE.md              → reglas de operación del asistente (leer primero)
docs/                  → arquitectura, metodología, roadmap, decisiones, prompt maestro
conocimiento/          → saber agronómico en .md (cultivos, protocolos, suelos, clima, MIP…)
herramientas/          → paquete Python de cálculo auditable (con tests)
datos/                 → parámetros, estacionalidad, referencias y registros de finca
fuentes/               → referencias BibTeX y bitácoras de búsqueda
entregables/           → generación de informes (DOCX/PDF), presentaciones (PPTX) y libros
scripts/               → utilidades (setup-entregables.sh instala la cadena de render)
.claude/               → skills, plugins/marketplaces y hook de arranque
```

## Entregables (documentos, presentaciones, PDFs)
Agriconsultor convierte su conocimiento en productos profesionales con una cadena ya
instalada (pandoc, typst, quarto, Marp, python-pptx, PptxGenJS) y las skills oficiales
`document-skills` (pptx/docx/pdf/xlsx) + `superpowers`. Instalación reproducible:
```bash
bash scripts/setup-entregables.sh      # idempotente; también corre en SessionStart
```
Ver [`entregables/README.md`](./entregables/README.md) para recetas y plantillas.

## Estado
En construcción por fases (ver [`docs/ROADMAP.md`](./docs/ROADMAP.md)). Los cimientos
—estructura, reglas, plantillas y herramientas base— están listos; el llenado de
conocimiento y datos se hace con apoyo de un agrónomo experto y siguiendo
[`docs/PROMPT-MAESTRO.md`](./docs/PROMPT-MAESTRO.md).

## Uso rápido de las herramientas
```bash
cd herramientas
python -m pytest            # correr tests
python -c "from agroconsultor import indices_vegetacion as iv; print(iv.ndvi(nir=0.45, red=0.08))"
```

## Principios
- **Cero datos inventados** — todo con fuente y fecha, o `[NO ENCONTRADO]`.
- **Todo cálculo auditable** — fórmula, supuestos, unidades y origen de datos.
- **Contexto local manda** — nada de recetas universales.
- **Seguridad y legalidad** — agroquímicos solo con registro SFE y respetando carencia.
