# Índices de teledetección — referencia agronómica

Interpretación de índices de vegetación para uso agronómico. El cálculo lo hace
`herramientas/agroconsultor/indices_vegetacion.py`; aquí va **qué significan** y
**cuándo usar cada uno**. Los umbrales calibrados por cultivo/etapa van en la
monografía de cada cultivo, no aquí (y siempre citados).

## Bandas (Sentinel-2 como referencia)
| Banda | Sentinel-2 | λ aprox. | Uso |
|---|---|---|---|
| Azul | B2 | 490 nm | corrección atmosférica (EVI) |
| Verde | B3 | 560 nm | clorofila (GNDVI, GCI) |
| Rojo | B4 | 665 nm | absorción de clorofila (NDVI, SAVI) |
| Borde rojo | B5–B7 | 705–783 nm | N/clorofila en dosel denso (NDRE) |
| NIR | B8/B8A | 842/865 nm | estructura/biomasa del dosel |
| SWIR | B11/B12 | 1610/2190 nm | agua de la vegetación (NDWI, NDMI) |

## Qué índice para qué pregunta
| Pregunta | Índice | Nota |
|---|---|---|
| ¿Cuánto vigor/biomasa verde? | NDVI | Se **satura** en dosel denso. |
| ¿Estado de N/clorofila en dosel cerrado? | NDRE, GNDVI | Menos saturación que NDVI. |
| Cultivo joven con suelo expuesto | SAVI | Ajustar factor de suelo L. |
| Reducir efecto suelo+atmósfera en biomasa alta | EVI | Coeficientes MODIS/S2. |
| Estrés hídrico del dosel | NDWI, NDMI | Requiere SWIR. |

## Cautelas
- Verificar que los valores sean **reflectancia (0–1)**, no niveles digitales.
- Enmascarar nubes/sombras/agua antes de promediar por lote.
- Un índice no diagnostica la causa: dirige el **muestreo en campo**. Marcar
  `⟨inferencia⟩` toda lectura sin umbral citado.

## Fuentes de fórmulas
Rouse et al. (1974) NDVI · Gitelson et al. (1996) GNDVI · Barnes et al. (2000) NDRE ·
Huete (1988) SAVI · Huete et al. (2002) EVI · Gao (1996) NDWI. Registrar la cita
completa en `fuentes/refs/` al usarlas en una ficha.
