# Arquitectura de Agriconsultor

## Idea central

Agriconsultor no es una aplicación con interfaz gráfica: es un **repositorio de
conocimiento + herramientas** que un modelo de lenguaje (Claude Code, o cualquier
cliente vía MCP) usa como "cerebro externo" para actuar como agrónomo experto de
Costa Rica. El valor no está en un ejecutable, sino en tres capas que el modelo
consulta y combina:

```
        ┌───────────────────────────────────────────────┐
        │  Modelo (Claude Code / MCP)                     │
        │  Razona siguiendo CLAUDE.md                     │
        └───────────────┬───────────────────────────────┘
                        │ consulta / invoca
   ┌────────────────────┼─────────────────────┬──────────────────┐
   ▼                    ▼                     ▼                  ▼
CONOCIMIENTO         HERRAMIENTAS            DATOS             SKILLS
(.md, criterio)      (Python, cálculo)   (CSV/SQLite)     (.claude/skills)
conocimiento/        herramientas/          datos/          flujos guiados
```

- **Conocimiento (`conocimiento/`)** — el criterio agronómico en prosa técnica
  verificable: monografías de cultivo, protocolos de decisión, suelos, clima,
  nutrición, MIP, interpretación de índices. Es lo que el modelo *lee* para tener
  criterio local.
- **Herramientas (`herramientas/`)** — funciones Python **deterministas y
  auditables** para lo que no se debe estimar "a ojo": índices de vegetación,
  grados-día, balance hídrico/ET, densidades, fertilización, economía. El modelo
  *ejecuta* estas funciones en vez de calcular mentalmente.
- **Datos (`datos/`)** — parámetros por cultivo (Kc, densidades, extracción),
  fenología/estacionalidad, referencias (suelos, clima, precios) y los **registros
  de finca** del usuario (sus propias bases de datos de cultivos).

## Por qué esta separación

1. **Verificabilidad:** el conocimiento cita fuentes; las herramientas muestran
   fórmulas; los datos tienen diccionario. Nada es una caja negra.
2. **Sin alucinación de números:** un LLM no debe inventar una dosis o un NDVI.
   Se fuerza el uso de datos versionados y funciones probadas (con tests).
3. **Evolutivo:** el agrónomo corrige `.md`; el ingeniero mejora Python; los datos
   crecen — sin reescribir el sistema.
4. **Portátil:** funciona local en Claude Code hoy; mañana se expone por MCP a
   ChatGPT u otros clientes sin cambiar el contenido.

## Flujo de una consulta (ejemplo)

Usuario: *"¿Cuánto nitrógeno le pongo a mi lote de papa en Tierra Blanca?"*

1. El modelo lee `CLAUDE.md` §4 (protocolo) → pide datos faltantes (variedad,
   análisis de suelo, rendimiento meta, área).
2. Lee `conocimiento/cultivos/papa/papa.md` §5 (nutrición) y
   `conocimiento/suelos/andisoles.md`.
3. Toma coeficientes de `datos/parametros/cultivos_parametros.csv`.
4. Ejecuta `herramientas/agroconsultor/fertilizacion.py` con esos datos.
5. Responde: diagnóstico → dosis por etapa (con fórmula y fuente) → riesgos → qué
   registrar. Guarda el plan en `datos/registros/` si el usuario lleva bitácora.

## Roadmap de capacidades (resumen; detalle en ROADMAP.md)

- **Fase 1 — Cimientos (esta):** estructura, CLAUDE.md, plantillas, herramientas
  base funcionales (índices, grados-día, ET, unidades), esquema de datos.
- **Fase 2 — Contenido:** completar cultivos prioritarios y protocolos con el
  agrónomo; poblar `datos/parametros/`.
- **Fase 3 — Cálculo agronómico:** fertilización y economía guiadas por datos;
  tests de cobertura.
- **Fase 4 — Registros:** bitácoras de finca en SQLite; consultas e informes.
- **Fase 5 — Teledetección:** integración con imágenes (Sentinel/Landsat, dron) y
  APIs (p. ej. Google Earth Engine) para NDVI/NDRE/GNDVI operativos.
- **Fase 6 — Distribución:** empaquetado como servidor MCP.

## Decisiones de diseño registradas

- **Idioma:** español técnico (contenido), con búsqueda bilingüe. Ver
  `docs/decisiones-pendientes.md`.
- **Formato de datos:** CSV como fuente editable + SQLite generado para consulta.
- **Python:** biblioteca pura, sin dependencias pesadas en el núcleo de cálculo;
  las integraciones externas (teledetección) se aíslan en módulos opcionales.
