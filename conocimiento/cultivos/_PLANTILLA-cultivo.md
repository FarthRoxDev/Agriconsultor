# [Nombre común CR] — *[Género especie]*

> Plantilla maestra de monografía de cultivo. **Copiar** este archivo a
> `conocimiento/cultivos/<slug>/<slug>.md` y completar. Toda cifra sigue el formato
> de hallazgo del `CLAUDE.md`. Lo no encontrado se marca `[NO ENCONTRADO]` con su
> registro en `fuentes/logs/`. La inferencia del asistente se marca `⟨inferencia⟩`.

- **Slug:** `<slug>` · **Familia:** ___ · **Tipo:** grano / hortaliza / raíz / frutal / forraje / follaje / flor de corte / ornamental
- **Estado de la ficha:** borrador / revisada por agrónomo (fecha) / validada
- **Última actualización:** AAAA-MM-DD · **Autor(es):** ___

## 1. Identidad y usos
- Nombre científico, sinónimos, nombres comunes CR.
- Uso principal en CR (mercado interno, agroexportación, floristería, forraje).
- Variedades/materiales usados en CR y su origen (dónde se consigue semilla/planta).

## 2. Requerimientos de sitio
| Parámetro | Rango óptimo | Rango tolerable | Fuente |
|---|---|---|---|
| Altitud (msnm) | | | |
| Temperatura media (°C) | | | |
| Precipitación (mm/año) | | | |
| pH del suelo | | | |
| Textura / drenaje | | | |
| Zonas de vida / cantones aptos en CR | | | |

## 3. Fenología y estacionalidad
- Etapas fenológicas y su duración (días y/o **grados-día**, T base = ___ °C).
- Ventanas de **siembra** y **cosecha** por vertiente (Pacífico / Caribe).
- Sensibilidad a fotoperiodo, altitud, heladas.
- → Volcar a `datos/parametros/fenologia_estacionalidad.csv`.

## 4. Establecimiento
- Preparación de suelo, propagación (semilla/vegetativa/vivero).
- **Densidad** (plantas/ha) y distancias de siembra. → `cultivos_parametros.csv`.
- Manejo inicial (trasplante, sombra, tutoreo si aplica).

## 5. Nutrición y fertilización
- **Extracción** de nutrientes (kg de N, P₂O₅, K₂O, Ca, Mg, S por t de producto).
- Programa de fertilización por etapa (dosis, fuente, momento).
- Diagnóstico foliar (rangos de suficiencia) y síntomas de deficiencia.
- Enmiendas/encalado según análisis de suelo.
- → Coeficientes a `datos/parametros/` para uso por `herramientas/…/fertilizacion.py`.

## 6. Agua y riego
- Requerimiento hídrico (mm/ciclo), **Kc** por etapa. → `coeficientes_kc.csv`.
- ¿Cuándo el riego es rentable en CR? Señales de estrés hídrico.

## 7. Manejo sanitario (MIP)
Por cada plaga/enfermedad clave, enlazar a ficha en
`conocimiento/plagas-enfermedades/` y resumir:

| Plaga/enfermedad | Agente | Umbral de acción | Monitoreo | Manejo (cultural→bio→químico) | Carencia (PHI) | Fuente |
|---|---|---|---|---|---|---|

> Toda recomendación química: verificar **registro SFE** e ingrediente activo
> permitido en CR antes de escribir dosis.

## 8. Cosecha y poscosecha
- Índice(s) de cosecha, método, época.
- Manejo poscosecha, mermas típicas, normas de calidad/exportación si aplica.

## 9. Rendimiento
- Rango realista en CR: bueno / medio / malo (t/ha o unidades de mercado).
- Factores que más limitan el rendimiento en la práctica.

## 10. Economía
- Rubros de costo que más pesan (por ha o por ciclo).
- Precio(s) de referencia con fuente y fecha (CNP, SEPSA, exportador…).
- Umbral de rentabilidad ⟨inferencia si se estima⟩.

## 11. Vacíos de información
- Lista de `[NO ENCONTRADO]` y preguntas abiertas para el agrónomo.

## 12. Fuentes
- Referencias (además de las citadas arriba). BibTeX en `fuentes/refs/<slug>.bib`.
