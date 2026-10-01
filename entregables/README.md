# Entregables — generación de documentos, presentaciones y PDFs

Subsistema para convertir el conocimiento agronómico de Agriconsultor (monografías,
planes, diagnósticos, registros) en **entregables profesionales**: informes (DOCX/PDF),
presentaciones (PPTX/slides) y libros/manuales (PDF de alta calidad). Mantiene
**paridad**: una sola fuente puede producir varios formatos.

## Principio: una fuente → varios formatos (paridad)
Siempre que se pueda, escribir el contenido **una vez** (Markdown o Quarto) y generar los
formatos con herramientas de conversión/maquetación, en vez de mantener copias paralelas.

```
                 ┌──────────────┐
  fuente única → │  .qmd / .md  │
                 └──────┬───────┘
          ┌────────────┼───────────────┬───────────────┐
          ▼            ▼                ▼               ▼
        PDF/libro    DOCX            PPTX/slides      HTML
       (Quarto/      (pandoc)      (pandoc/Marp/     (Quarto/
        typst)                      PptxGenJS)        Marp)
```

## Herramientas instaladas (ver `scripts/setup-entregables.sh`)
| Herramienta | Rol | Verificado |
|---|---|---|
| **pandoc** 3.12 | Conversor universal (MD↔DOCX↔PDF↔…); motor de paridad | ✅ |
| **typst** 0.15.1 | Maquetación tipo libro; **motor PDF de pandoc** (`--pdf-engine=typst`) | ✅ |
| **quarto** 1.11.5 | Una fuente `.qmd` → libro, slides y PDF; ideal para informes técnicos | ✅ |
| **python-pptx** 1.0.2 | Generar/editar `.pptx` desde Python (control fino, data-driven) | ✅ |
| **python-docx** | Generar/editar `.docx` desde Python | ✅ |
| **PptxGenJS** | Alternativa JS para `.pptx` (local en `entregables/`) | ✅ |
| **Marp** 4.5.1 | Slides desde Markdown | ⚠️ ver nota de navegador |

### Skills y plugins de Claude (declarados en `.claude/settings.json`)
- **document-skills** (`@anthropic-agent-skills`): skills oficiales de **PowerPoint, Word,
  PDF y Excel** — la vía preferida cuando se trabaja dentro de Claude Code.
- **superpowers** (`@superpowers-dev`): flujo de trabajo por fases (TDD, depuración,
  colaboración) para tareas complejas.
- Marketplaces disponibles para instalar más plugins: `claude-plugins-official`,
  `awesome-claude-plugins` (incluye `theme-factory`, `canvas-design`, `artifacts-builder`),
  `anthropic-agent-skills`, `superpowers-dev`.

## Qué usar según el entregable
- **Informe técnico / monografía imprimible (PDF + DOCX):** Quarto (`.qmd`) o Markdown +
  pandoc. PDF de alta calidad con `--pdf-engine=typst` (no requiere LaTeX).
- **Presentación (PPTX editable para el agrónomo/cliente):** document-skills (pptx) o
  PptxGenJS/python-pptx cuando el contenido es data-driven (p. ej. tablas de rendimiento).
- **Presentación rápida desde Markdown:** Marp.
- **Manual/libro multi-capítulo (varios cultivos):** Quarto book → PDF (typst) + HTML.
- **Documento Word para firmar/enviar:** document-skills (docx) o pandoc.

## Recetas rápidas
```bash
# Markdown -> Word
pandoc informe.md -o informe.docx

# Markdown/Quarto -> PDF de alta calidad (motor typst, sin LaTeX)
pandoc informe.md --pdf-engine=typst -o informe.pdf

# Quarto: una fuente -> PDF y HTML
quarto render informe.qmd --to pdf
quarto render informe.qmd --to html

# Slides desde Markdown (Marp) — para PDF/PPTX ver nota de navegador
cd entregables && npx marp plantillas/presentacion.md -o salidas/presentacion.html

# PPTX data-driven con PptxGenJS (Node) o python-pptx (Python)
cd entregables && node plantillas/presentacion-pptxgenjs.js
python3 entregables/plantillas/presentacion-python-pptx.py
```

## Nota de navegador (Marp y export a PDF/PPTX de slides)
Marp exporta HTML sin navegador, pero **PDF/PPTX/PNG requieren Chromium**. En este entorno
hay Chromium preinstalado; usar:
```bash
export CHROME_PATH=/opt/pw-browsers/chromium   # o la ruta real de chromium
npx marp deck.md --pdf --no-sandbox -o salidas/deck.pdf
```
Si Marp se cuelga en un sandbox sin navegador, preferir Quarto/pandoc+typst para el PDF.

## Convenciones
- Fuentes editables en `entregables/plantillas/`; resultados en `entregables/salidas/`
  (ignorada por git). Los datos provienen de `datos/` y el texto de `conocimiento/`.
- Toda cifra en un entregable conserva su **fuente** (regla `CLAUDE.md`). No generar un
  informe con números sin respaldo.
