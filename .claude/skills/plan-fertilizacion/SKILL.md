---
name: plan-fertilizacion
description: >-
  Construye un plan de fertilización por balance de nutrientes para un cultivo y lote,
  a partir del rendimiento meta, la extracción del cultivo y el análisis de suelo. Usar
  cuando el usuario pide dosis de N-P-K (u otros), un programa de abonado por etapa, o
  cuánto fertilizante comprar. Calcula con herramientas, no a ojo.
---

# Skill: Plan de fertilización

Reglas: `CLAUDE.md` §2 (cálculo auditable) y §5 (convenciones). Motor de cálculo:
`herramientas/agroconsultor/fertilizacion.py`.

## Paso 1 — Reunir datos (pídelos si faltan)
- Cultivo, variedad, área (ha), **rendimiento meta** (t/ha).
- **Análisis de suelo** (con unidades del laboratorio) y profundidad muestreada.
- Sistema de riego/manejo (afecta eficiencia de uso del nutriente).

## Paso 2 — Tomar coeficientes de `datos/`
- Extracción por t de producto → `datos/parametros/extraccion_nutrientes.csv`.
- Factores de disponibilidad del suelo → `conocimiento/suelos/` (con su justificación).
- Si un coeficiente no está o dice `EJEMPLO_NO_VALIDADO`, **detente**: búscalo con
  fuente (formato de hallazgo) o dilo como `[NO ENCONTRADO]`. No inventes.

## Paso 3 — Calcular
1. `extraccion_por_rendimiento(extraccion_por_t, rendimiento_t_ha)` por nutriente.
2. Estimar aporte del suelo (kg/ha) desde el análisis.
3. `Nutriente(...).dosis_kg_ha()` con la eficiencia de uso apropiada.
4. `dosis_fuente_comercial(dosis, riqueza_pct)` para traducir a producto (urea, KCl…).
5. Repartir por etapa según la monografía del cultivo.

## Paso 4 — Responder
Tabla por nutriente y por etapa: dosis del elemento, fuente comercial, kg/ha y total
para el área. Muestra fórmula, supuestos, unidades y de qué archivo salió cada
coeficiente. Añade encalado/enmiendas si el pH lo exige. Cita fuentes.

## Paso 5 — Registrar
Anota el plan en `datos/registros/` (tabla de aplicaciones/labores).
