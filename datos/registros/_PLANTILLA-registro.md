# Registro de finca / lote — PLANTILLA

> Copiar a `datos/registros/<finca>/<lote>.md` (o usar la base SQLite descrita en
> `datos/esquema/registros-sqlite.md`). El asistente actualiza este archivo con cada
> labor, aplicación, monitoreo y cosecha. Es la "memoria" del cultivo del usuario.

## Identificación
- **Finca:** ___ · **Lote/parcela:** ___ · **Área (ha):** ___
- **Ubicación:** lat ___, lon ___ (WGS84) · **Altitud:** ___ msnm · **Cantón/zona:** ___
- **Cultivo:** ___ (*género especie*) · **Variedad/material:** ___
- **Sistema:** campo abierto / protegido / orgánico / convencional
- **Fecha de siembra/trasplante:** AAAA-MM-DD · **Fecha estimada de cosecha:** AAAA-MM-DD

## Suelo (último análisis)
- Fecha: ___ · Laboratorio: ___
- pH ___ · MO % ___ · N ___ · P ___ · K ___ · Ca ___ · Mg ___ · CIC ___ · (adjuntar)

## Bitácora de labores
| Fecha | Labor | Detalle | Insumo/dosis | Costo | Responsable | Notas |
|---|---|---|---|---|---|---|
| | | | | | | |

## Aplicaciones fitosanitarias / fertilización
| Fecha | Producto | I.A. | Registro SFE | Dosis | Objetivo | Carencia (PHI) | Reingreso | Notas |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Monitoreo (plagas/enfermedades/fenología)
| Fecha | Etapa/GDD | Observación | Incidencia/severidad | Umbral | Decisión |
|---|---|---|---|---|---|
| | | | | | |

## Riego
| Fecha | Lámina (mm) | Método | ETo | Kc | Notas |
|---|---|---|---|---|---|
| | | | | | |

## Cosecha
| Fecha | Cantidad | Unidad | Calidad/categoría | Destino | Precio | Notas |
|---|---|---|---|---|---|---|
| | | | | | | |

## Resumen económico del ciclo
- Costo total: ___ · Ingreso: ___ · Margen: ___ · Relación B/C: ___
- (usar `herramientas/agroconsultor/economia.py` para el cálculo)
