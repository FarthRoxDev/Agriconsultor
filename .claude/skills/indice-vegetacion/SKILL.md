---
name: indice-vegetacion
description: >-
  Calcula e interpreta índices de vegetación (NDVI, NDRE, GNDVI, SAVI, EVI, NDWI...) a
  partir de reflectancias por banda de imágenes satelitales o de dron. Usar cuando el
  usuario aporta valores de banda o pregunta por el estado del dosel/vigor/nitrógeno/
  estrés hídrico por teledetección. La integración con imágenes reales es Fase 5.
---

# Skill: Índices de vegetación

Motor: `herramientas/agroconsultor/indices_vegetacion.py`. Referencia agronómica:
`conocimiento/indices-teledeteccion/`.

## Paso 1 — Identificar sensor y bandas
Confirma la fuente (Sentinel-2, Landsat, dron multiespectral) y **qué banda es cuál**
(rojo, verde, borde rojo, NIR, SWIR). Los índices esperan **reflectancia (0–1)**.

## Paso 2 — Elegir el índice según la pregunta
- Vigor/biomasa general → **NDVI** (se satura en dosel denso).
- Estado nitrogenado/clorofila en dosel denso → **NDRE** o **GNDVI**.
- Suelo expuesto (cultivo joven) → **SAVI** (ajustar L).
- Estrés hídrico del dosel → **NDWI/NDMI** (requiere SWIR).

## Paso 3 — Calcular e interpretar
Llama la función correspondiente. Usa `interpretar_ndvi()` solo como guía cualitativa
genérica; los **umbrales calibrados por cultivo y etapa** van en la ficha del cultivo
(cítalos). Señala cuándo el índice puede estar saturado o afectado por nubes/sombra.

## Paso 4 — Responder
Valor del índice + interpretación agronómica + qué acción sugiere (muestreo dirigido,
zona de manejo diferenciado). Marca `⟨inferencia⟩` la interpretación no respaldada por
umbral citado. Para series de tiempo o mapas por lote, ver Fase 5 en `docs/ROADMAP.md`.
