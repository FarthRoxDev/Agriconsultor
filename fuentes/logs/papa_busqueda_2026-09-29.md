# Bitácora de búsqueda — Papa (*Solanum tuberosum*) — 2026-09-29

Cultivo piloto. Registro de búsquedas para respaldar la monografía
`conocimiento/cultivos/papa/papa.md`. Cumple la regla de trazabilidad del `CLAUDE.md`.

| Fecha | Tema/afirmación buscada | Motor/base | Términos | Resultado | Fuente hallada (URL) | Confianza |
|---|---|---|---|---|---|---|
| 2026-09-29 | Guía técnica del cultivo de papa en Costa Rica | Firecrawl (web) | "INTA Costa Rica guía técnica cultivo de papa Solanum tuberosum" | encontrado | https://repositorio.iica.int/items/92ed779a-341e-4c9b-97bb-d69faee9defe | alto |
| 2026-09-29 | Manual institucional CR (autores, ISBN, año) | Firecrawl (scrape ficha IICA) | página del ítem | encontrado | Avilés Chaves & Piedra Naranjo (2016), INTA/PRIICA, ISBN 978-9968-586-11-5, https://hdl.handle.net/11324/3145 | alto |
| 2026-09-29 | Texto completo del manual (sitio, fertilización, MIP, rendimiento) | Firecrawl (PDF, extracción por consulta) | pp.1-22 markdown; pp.40-52 y 56-88 extracción dirigida | **ENCONTRADO** — extraídos sitio, clima, variedades, fenología, siembra, fertilización (absorción p.52), MIP (p.56-88), cosecha (p.86). Costos (Cap.3 p.87) no extraídos. | https://repositorio.iica.int/bitstreams/06ba5470-8a6b-45c0-a1af-2f4f6c9f54c4/download | alto |
| 2026-09-29 | Descarga directa por curl | Bash curl vía proxy | CONNECT | **[NO ENCONTRADO]** por esta vía — proxy del entorno devuelve 403 al host; usar Firecrawl. | — | — |

## Otras fuentes candidatas localizadas (por evaluar/priorizar)
- CIP — *Manual del cultivo de papa para pequeños productores*: https://cipotato.org/genebankcip/publications/manual-del-cultivo-de-papa-para-pequenos-productores/ (institucional, regional; verificar aplicabilidad a CR).
- INTA Costa Rica — nota 2025 sobre liberación de nuevas variedades con aptitud para proceso (Centro Experimental Carlos Durán): referencia en redes; **buscar la publicación técnica primaria**, no la red social.
- UNA (Nicaragua) — *Guía MIP en el cultivo de la papa* (PDF): https://cenida.una.edu.ni/relectronicos/RENH10M722.pdf (regional; usar solo como apoyo, priorizar fuente CR).

## Pendientes de búsqueda (para completar la monografía)
- [ ] SFE Costa Rica: registro vigente de plaguicidas y **periodos de carencia (PHI)** para papa (tizón tardío, polilla).
- [ ] INTA/MAG: variedades liberadas y recomendadas en CR (Floresta, Única y otras) con fuente primaria.
- [ ] CIA-UCR: interpretación de análisis de suelo en andisoles de Cartago; factores de disponibilidad de nutrientes.
- [ ] Rendimientos reales en CR (t/ha) por zona: INEC/SEPSA o INTA.
- [ ] Coeficientes de cultivo (Kc) FAO-56 para papa y extracción de nutrientes (kg/t) con fuente citable.
- [ ] Precios de referencia (CNP/SEPSA) y estructura de costos por ha.
