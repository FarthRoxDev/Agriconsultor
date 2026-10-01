# Diccionario de datos

Define la estructura de los archivos en `datos/`. Regla (CLAUDE.md): **toda fila con
un número debe tener `fuente` y `fecha_consulta`**. Estados posibles del campo `estado`:

- `EJEMPLO_NO_VALIDADO` — fila de muestra para enseñar el formato; **no usar** como dato real.
- `CITADO` — valor real **con fuente citada**, pendiente de validación por el agrónomo.
- `VALIDADO` — valor con fuente **y** revisado/validado por el agrónomo.

Las filas de ejemplo se reemplazan por valores `CITADO` al hallar la fuente, y pasan a
`VALIDADO` solo tras la revisión del agrónomo.

Convención de valores faltantes: celda vacía o `[POR COMPLETAR]`. Nunca inventar.

## `parametros/cultivos_parametros.csv`
Un renglón por cultivo (o cultivo+variedad). Parámetros agronómicos base.

| Columna | Tipo | Unidad | Descripción |
|---|---|---|---|
| slug | texto | — | identificador del cultivo (coincide con `conocimiento/cultivos/<slug>`) |
| nombre_comun | texto | — | nombre común CR |
| nombre_cientifico | texto | — | género especie |
| tipo | texto | — | grano/hortaliza/raiz/frutal/forraje/follaje/flor/ornamental |
| altitud_min_msnm | número | msnm | altitud mínima apta |
| altitud_max_msnm | número | msnm | altitud máxima apta |
| ph_min | número | — | pH mínimo óptimo |
| ph_max | número | — | pH máximo óptimo |
| densidad_plantas_ha | número | plantas/ha | densidad de siembra recomendada |
| dist_hileras_m | número | m | distancia entre hileras |
| dist_plantas_m | número | m | distancia entre plantas |
| tbase_gdd_c | número | °C | temperatura base para grados-día |
| ciclo_dias | número | días | duración típica del ciclo (a cosecha) |
| rend_bueno_t_ha | número | t/ha | rendimiento bueno en CR |
| rend_medio_t_ha | número | t/ha | rendimiento medio en CR |
| estado | texto | — | EJEMPLO_NO_VALIDADO / VALIDADO |
| fuente | texto | — | URL/DOI/institución |
| fecha_consulta | fecha | AAAA-MM-DD | fecha de consulta de la fuente |

## `parametros/coeficientes_kc.csv`
Coeficientes de cultivo (Kc, FAO-56) por etapa. Un renglón por cultivo+etapa.

| Columna | Tipo | Unidad | Descripción |
|---|---|---|---|
| slug | texto | — | cultivo |
| etapa | texto | — | inicial/desarrollo/media/final (FAO-56) |
| kc | número | — | coeficiente de cultivo |
| duracion_dias | número | días | duración de la etapa |
| estado | texto | — | EJEMPLO_NO_VALIDADO / VALIDADO |
| fuente | texto | — | referencia |
| fecha_consulta | fecha | AAAA-MM-DD | |

## `parametros/fenologia_estacionalidad.csv`
Ventanas de siembra/cosecha y etapas por zona/vertiente.

| Columna | Tipo | Unidad | Descripción |
|---|---|---|---|
| slug | texto | — | cultivo |
| zona | texto | — | zona agroclimática / cantón / vertiente |
| vertiente | texto | — | Pacifico / Caribe |
| mes_siembra_inicio | número | mes 1–12 | inicio ventana de siembra |
| mes_siembra_fin | número | mes 1–12 | fin ventana de siembra |
| mes_cosecha_inicio | número | mes 1–12 | inicio ventana de cosecha |
| mes_cosecha_fin | número | mes 1–12 | fin ventana de cosecha |
| estado | texto | — | EJEMPLO_NO_VALIDADO / VALIDADO |
| fuente | texto | — | referencia |
| fecha_consulta | fecha | AAAA-MM-DD | |

## `parametros/extraccion_nutrientes.csv`
Extracción de nutrientes por tonelada de producto (para `fertilizacion.py`).

| Columna | Tipo | Unidad | Descripción |
|---|---|---|---|
| slug | texto | — | cultivo |
| n_kg_por_t | número | kg N / t | nitrógeno removido por t de producto |
| p2o5_kg_por_t | número | kg P₂O₅ / t | fósforo (como óxido) |
| k2o_kg_por_t | número | kg K₂O / t | potasio (como óxido) |
| ca_kg_por_t | número | kg Ca / t | calcio |
| mg_kg_por_t | número | kg Mg / t | magnesio |
| estado | texto | — | EJEMPLO_NO_VALIDADO / VALIDADO |
| fuente | texto | — | referencia |
| fecha_consulta | fecha | AAAA-MM-DD | |

## `registros/` (bitácoras de finca)
Ver `datos/registros/_PLANTILLA-registro.md` y `datos/esquema/registros-sqlite.md`
para el modelo relacional (finca → lote → labores/aplicaciones/cosechas/monitoreo).
