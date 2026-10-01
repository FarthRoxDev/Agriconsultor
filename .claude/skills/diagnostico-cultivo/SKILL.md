---
name: diagnostico-cultivo
description: >-
  Diagnóstico agronómico estructurado ante un problema de cultivo (bajo vigor,
  amarillamiento, manchas, poca producción, plaga sospechada). Usar cuando el usuario
  describe un síntoma o problema en campo y hay que llegar a una causa probable y una
  recomendación. Guía la toma de contexto, el descarte de causas y la respuesta con
  fuentes.
---

# Skill: Diagnóstico de cultivo

Sigue la metodología de `docs/metodologia-agronomica.md` y las reglas de `CLAUDE.md`.

## Paso 1 — Ubicar el contexto (no diagnosticar sin esto)
Pregunta lo que falte: cultivo y variedad, zona/cantón, **altitud (msnm)**, etapa
fenológica, sistema (abierto/protegido/orgánico/convencional), síntoma exacto y
distribución (¿focal o generalizado? ¿hojas viejas o nuevas?), historial reciente
(riego, fertilización, aplicaciones, clima), y análisis de suelo/foliar si existen.

## Paso 2 — Descartar por bloques (árbol de causas)
Recorre en orden y descarta con evidencia:
1. **Abiótico/manejo:** agua (déficit/exceso, drenaje, sales), nutrición
   (patrón del síntoma por hoja vieja vs. nueva), pH, daño mecánico/fitotoxicidad.
2. **Biótico:** patrón y signos de plaga/enfermedad (consultar
   `conocimiento/plagas-enfermedades/`).
3. **Ambiental:** heladas, viento, exceso de radiación, fotoperiodo/altitud.

## Paso 3 — Consultar conocimiento y datos
Lee la monografía en `conocimiento/cultivos/<slug>/` (§5 nutrición, §7 MIP) y la ficha
de suelo/clima pertinente. Si hay imágenes/índices, apóyate en
`herramientas/agroconsultor/indices_vegetacion.py`.

## Paso 4 — Responder
Diagnóstico (con nivel de confianza y causas alternativas) → qué confirmar (muestreo,
análisis) → recomendación accionable (con dosis solo si hay registro SFE y carencia
verificados) → qué medir/registrar. Cita en formato de hallazgo. Marca `⟨inferencia⟩`
lo que no sea dato duro.

## Paso 5 — Registrar
Si el usuario lleva bitácora, anota el hallazgo en `datos/registros/` (tabla de
monitoreo).
