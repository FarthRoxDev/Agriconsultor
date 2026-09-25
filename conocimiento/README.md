# Base de conocimiento

Criterio agronómico verificable en `.md`. Es lo que el asistente **lee** para tener
criterio local. Toda cifra sigue el formato de hallazgo del `CLAUDE.md`.

| Carpeta | Contenido | Estado |
|---|---|---|
| `cultivos/` | Monografías por cultivo (usar `_PLANTILLA-cultivo.md`) | Plantilla lista |
| `protocolos/` | Árboles de decisión: diagnóstico, fertilización, riego, MIP, análisis | Por completar |
| `suelos/` | Suelos de CR (andisoles, ultisoles…), interpretación de análisis | Por completar |
| `clima/` | Zonas agroclimáticas, régimen por vertiente, ETo, heladas | Por completar |
| `nutricion/` | Nutrición vegetal, extracción, síntomas de deficiencia | Por completar |
| `plagas-enfermedades/` | Fichas MIP (agente, umbral, monitoreo, manejo, carencia) | Por completar |
| `indices-teledeteccion/` | Interpretación agronómica de NDVI/NDRE/GNDVI/SAVI… | Referencia base |

## Cómo agregar conocimiento
1. Elige la carpeta y copia la plantilla si existe.
2. Completa con datos **citados** (fuente + fecha + confianza). Lo que no encuentres,
   `[NO ENCONTRADO]` + registro en `fuentes/logs/`.
3. Distingue dato duro de `⟨inferencia⟩`.
4. Marca el estado de la ficha (borrador → revisada por agrónomo → validada).
5. Vuelca los números reutilizables a `datos/parametros/` con su fuente.
