---
name: plan-riego
description: >-
  Calcula requerimiento de riego de un cultivo por el método FAO-56 (ETc = ETo x Kc)
  y balance con la precipitación efectiva. Usar cuando el usuario pregunta cuánto y
  cuándo regar, la lámina o el volumen de agua, o si el riego es rentable. Calcula con
  herramientas.
---

# Skill: Plan de riego

Motor: `herramientas/agroconsultor/riego_et.py`. Reglas: `CLAUDE.md`.

## Paso 1 — Reunir datos
- Cultivo y **etapa** (para el Kc), área (ha), sistema y su **eficiencia** (goteo,
  aspersión, gravedad).
- **ETo** de la zona (IMN, estación o cálculo aparte) y precipitación del periodo.

## Paso 2 — Coeficientes
- Kc por etapa → `datos/parametros/coeficientes_kc.csv` (si dice
  `EJEMPLO_NO_VALIDADO`, buscar con fuente o marcar `[NO ENCONTRADO]`).

## Paso 3 — Calcular
1. `etc(eto, kc)` → ETc (mm/día) o `etc_periodo(serie_eto, kc)`.
2. `precip_efectiva_usda(precip)` si no se tiene medida directa.
3. `requerimiento_neto_riego(etc_mm, precip_efectiva_mm)`.
4. `requerimiento_bruto_riego(neto, eficiencia)`.
5. `lamina_a_volumen(lamina_mm, area_ha)` → m³ para el lote.

## Paso 4 — Responder
Lámina neta y bruta (mm), volumen (m³), frecuencia sugerida y señales de estrés a
vigilar. Muestra fórmula, supuestos y origen del Kc y la ETo. Sobre rentabilidad del
riego: usar `economia.py` comparando el costo del agua/energía con el incremento de
rendimiento esperado ⟨inferencia, con supuestos explícitos⟩.

## Paso 5 — Registrar
Anota lámina y fecha en `datos/registros/` (tabla de riego).
