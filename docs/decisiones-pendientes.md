# Decisiones pendientes

Supuestos que tomé para poder construir los cimientos. **Corrígelos** (tú o el
agrónomo) y el resto del sistema se ajusta. Marcados con el valor por defecto usado.

## D1 — Idioma
- **Supuesto:** contenido en **español técnico**; búsqueda de fuentes bilingüe
  (español + inglés). Unidades SI, altitudes en msnm.
- ¿Correcto? ¿Se necesita salida en inglés para algún cliente/exportador?

## D2 — Arquitectura
- **Supuesto:** repo de conocimiento + herramientas usado por LLM (Claude Code / MCP),
  **no** una app con interfaz gráfica. Lo "local" es correr Claude Code sobre este repo.
- ¿Se requiere en algún momento una GUI/CLI independiente para el productor?

## D3 — Formato de datos
- **Supuesto:** CSV editable como fuente de verdad + SQLite generado para consulta y
  registros. Diccionario de datos en `datos/esquema/`.
- ¿Ok, o se prefiere todo en SQLite / hoja de cálculo / Google Sheets?

## D4 — Cultivos prioritarios (¡decidir con el agrónomo!)
Propuesta de catálogo para Costa Rica. **Ordenar por prioridad** y elegir el
**cultivo piloto** para completar primero de punta a punta.

**Agroexportación / granos-frutales comerciales**
- Café (*Coffea arabica*)
- Piña (*Ananas comosus*, MD2)
- Banano (*Musa* AAA)
- Plátano (*Musa* AAB)
- Caña de azúcar (*Saccharum officinarum*)
- Palma aceitera (*Elaeis guineensis*)
- Cacao (*Theobroma cacao*)
- Cítricos (naranja *Citrus sinensis*)

**Hortalizas de altura (zona de Cartago — sinergia con RSMAIZ)**
- Papa (*Solanum tuberosum*)
- Cebolla (*Allium cepa*)
- Zanahoria (*Daucus carota*)
- Brassicas: repollo, brócoli, coliflor (*Brassica oleracea*)
- Tomate (*Solanum lycopersicum*, campo/protegido)
- Chile dulce (*Capsicum annuum*)
- Lechuga (*Lactuca sativa*), culantro (*Coriandrum sativum*)

**Raíces y tubérculos tropicales**
- Yuca (*Manihot esculenta*)
- Ñame (*Dioscorea* spp.), tiquizque/malanga (*Xanthosoma*, *Colocasia*)
- Jengibre (*Zingiber officinale*)

**Floristería / follajes / ornamentales (exportación)**
- Follajes de corte: "cuero"/leatherleaf (*Rumohra adiantiformis*), *Dracaena*,
  palmas ornamentales, *Aspidistra*.
- Flores: heliconias (*Heliconia* spp.), gerbera, crisantemo, rosas de altura.
- Plantas ornamentales en maceta de exportación.

**Forrajes / lechería de altura (sinergia con RSMAIZ)**
- Maíz forrajero para ensilaje (*Zea mays*)
- Pastos: kikuyo (*Cenchrus clandestinus*), estrella (*Cynodon*), ryegrass de altura.

> **Pendiente:** ¿empezamos por alimentación, agroexportación o floristería? ¿Hay
> una finca/caso real que dicte el orden?

## D5 — Alcance de agroquímicos
- **Supuesto:** el asistente solo recomienda productos con registro SFE vigente y
  siempre exige verificar etiqueta/carencia; ante duda, advierte y no da dosis.
- ¿Se quiere además un enfoque orgánico/agroecológico prioritario para algún cultivo?

## D6 — Teledetección
- **Supuesto:** por ahora, funciones de índices que operan sobre reflectancias dadas
  (NDVI/NDRE/GNDVI/SAVI…). La integración con imágenes reales (Sentinel/Landsat/dron,
  Google Earth Engine) queda para Fase 5.
- ¿Qué fuente de imágenes se usará? ¿Hay acceso a Google Earth Engine, dron, o API?

## D7 — Registros de finca
- **Supuesto:** esquema propio (finca → lote → labores/aplicaciones/cosechas/monitoreo)
  en CSV/SQLite. 
- ¿El agrónomo ya usa un formato de bitácora que debamos replicar?
