# Papa — *Solanum tuberosum* L.

- **Slug:** `papa` · **Familia:** Solanaceae · **Tipo:** hortaliza (tubérculo)
- **Estado de la ficha:** **revisada internamente** con fuente primaria INTA 2016 · **pendiente de validación por agrónomo**
- **Última actualización:** 2026-09-29 · **Autor(es):** Agriconsultor

> **Fuente primaria:** Avilés Chaves, J. & Piedra Naranjo, R. (2016). *Manual del
> cultivo de papa en Costa Rica: Solanum tuberosum L.* INTA/PRIICA, San José, 94 pp.
> ISBN 978-9968-586-11-5. https://hdl.handle.net/11324/3145 (consultado 2026-09-29).
> Revisores técnicos del manual: J. Brenes Madriz (ITCR), I. Serrano (MAG). Las cifras
> citan la página del manual. Datos de terceros dentro del manual conservan su cita
> original (p. ej. MAG 2016, FAO 2008). Lo no hallado se marca `[NO ENCONTRADO]`.

## 1. Identidad y usos
- **Nombre científico:** *Solanum tuberosum* L. (Solanaceae). Planta anual herbácea;
  el tubérculo es un tallo modificado de reserva (p. 9-10).
- **Importancia en CR:** cultivo de pequeños y medianos productores; parte de la
  canasta básica. Consumo per cápita 17,42 kg/año (2002) → 20,84 kg/año (2012)
  (PIMA, Gutiérrez 2014, cit. en manual p. 7). | dato | manual INTA 2016 p.7 | 2026-09-29 | alto.
- **Zona productora:** provincia de **Cartago ≈ 2 800 ha**, seguida por **Zarcero
  ≈ 300 ha** (MAG 2016, cit. p. 8). Principales cantones: **Alvarado (35 %, el mayor)**,
  Oreamuno, Zarcero, Cartago, Goicoechea, Naranjo y Dota (MAG 2016, p. 10-11).
- **Sustitución de importaciones:** el país importa ~18 000 t/año de papa prefrita
  congelada (fuga de divisas ≈ ₡1 326 millones) y 1 902 t de papa fresca en 2015
  (MAG 2016, cit. p. 8) — contexto de mercado, no dato agronómico.

## 2. Requerimientos de sitio
Aptitud del suelo/clima según el manual (Cuadro de aptitud, p. 45), con óptimos:

| Parámetro | Óptimo (Clase I) | Tolerable (Clases II–III) | Fuente |
|---|---|---|---|
| Altitud | 2 300–2 600 msnm | 2 000–2 299 (II); 1 500–2 001 (III) | INTA 2016 p.45 |
| Temperatura | 15–25 °C (crecimiento y tuberización) | Cartago: 7–25 °C | INTA 2016 p.46-47 |
| Precipitación en el ciclo | 400–800 mm bien distribuidos | (Cartago 1 400–2 600 mm/año) | INTA 2016 p.46-47 |
| pH del suelo | 5,0–7,0 | | INTA 2016 p.40 |
| Textura | Franco (F, FA, FL) | Fa, FAL, FAa (II); aF (III); arenosos: no apto | INTA 2016 p.45 |
| Drenaje | Bueno | Moderado (II) / moder. lento (III) | INTA 2016 p.45 |
| Profundidad efectiva | > 40 cm | 30–40 (II); 20–31 (III) | INTA 2016 p.45 |
| Humedad relativa | ≈ 80 % | | INTA 2016 p.25 |

> ⟨inferencia⟩ Las zonas altas de Cartago (Tierra Blanca, Llano Grande, Cot, Pacayas,
> Oreamuno) caen en Clase I–II por altitud y clima, coherente con que concentren la
> producción nacional (p. 8-11).

## 3. Fenología y estacionalidad
Etapas del ciclo (p. 49-50): reposo/dormancia (semanas a 2–3 meses) → brotación
(dominancia apical) → crecimiento vegetativo → **inicio de tuberización (coincide con
inicio de floración)** → llenado de tubérculos → maduración (follaje amarillea y muere).

- **Duración del ciclo según variedad** (p. 12-20): corto **70–90 días** (Única),
  **90–100 días** (Floresta), intermedio **100–110 días** (Kamuk, Maleke ~110),
  largo **≥ 120 días** (Idiafrit, Yema de huevo). | dato | INTA 2016 | alto.
- **Temperatura base (T base) para grados-día:** `[NO ENCONTRADO]` en el manual
  (registrar de fuente citable; literatura FAO usa ~7 °C, verificar antes de usar en
  `herramientas/grados_dia.py`).
- **Estacionalidad Cartago:** la siembra de secano se asocia a régimen del Valle
  Central (época seca vs. lluviosa); Granola se cita como apta en Tierra Blanca "en
  época de verano" (p. 15). Ventanas de siembra/cosecha por mes: `[POR COMPLETAR]`
  (confirmar con MAG/Comisión Nacional de la Papa y con el agrónomo).

## 4. Establecimiento
- **Material vegetal:** tubérculo-semilla; el país maneja categorías desde prebásica
  (vitroplantas, microtubérculos) hasta semilla comercial (p. 30-38). Usar **semilla
  de calidad/certificada** es una recomendación transversal de manejo sanitario.
- **Distancias de siembra (p. 51):** **0,80–1,0 m entre surcos** y **25–30 cm entre
  tubérculos** (para Floresta, surcos 80–90 cm; p. 15). | dato | INTA 2016 | alto.
- **Densidad:** ⟨inferencia⟩ ≈ 37 000–50 000 plantas/ha según el arreglo (calculada con
  `herramientas/densidad_siembra.py` a partir de las distancias anteriores; el manual da
  distancias, no densidad).
- **Aporca:** alta y en el momento preciso; también es medida de manejo de tizón (p. 53).

## 5. Nutrición y fertilización
**Absorción total de nutrientes del cultivo** (Cuadro p. 52), y remoción en cosecha:

| | N | P | K | Ca | Mg | Fe | Cu | Zn | Mn |
|---|---|---|---|---|---|---|---|---|---|
| Absorción total (kg/ha) | 267 | 16 | 222 | 29 | 25 | 2192 g | 78 g | 133 g | 656 g |
| Remoción en cosecha (kg/ha) | 128 | 11 | 116 | 6 | 6 | 442 g | 26 g | 51 g | 60 g |

Fuente: INTA 2016 p.52. ⟨inferencia⟩ P y K aparecen como elemento (no como óxido);
confirmar y convertir con `util_unidades` antes de traducir a fórmulas comerciales.
El manual no declara el rendimiento base de esta absorción → la **extracción por
tonelada** queda `[NO ENCONTRADO]` (no dividir sin la base de rendimiento).

**Dosis recomendadas (p. 52):**
- General: **270 kg/ha N, 130 kg/ha P, 385 kg/ha K** (unidades según el manual). | dato | INTA 2016 p.52 | alto.
- Variedad Durán, verano: **220 N, 260 P₂O₅, 260 K₂O (kg/ha)**. | dato | INTA 2016 p.52 | alto.
- **Momento/forma:** al fondo del surco, o 8–10 días después de sembrar (tapar y
  aplicar) (p. 52).
- **Encalado:** ajustar según análisis de suelo (andisoles de Cartago tienden a ácidos;
  ver `conocimiento/suelos/` y CIA-UCR) — `[POR COMPLETAR]` con dato local.

> Para un plan por lote usar la skill `plan-fertilizacion` y `fertilizacion.py`,
> partiendo de la absorción citada, el análisis de suelo y la eficiencia de uso.

## 6. Agua y riego
- Requerimiento del ciclo (secano): **400–800 mm** bien distribuidos, críticos en
  formación de tubérculos (INTA 2016 p.46). | dato | alto.
- **Kc por etapa (FAO-56):** `[NO ENCONTRADO]` en el manual → tomar de FAO-56 (Allen
  et al. 1998) citándolo, y volcar a `datos/parametros/coeficientes_kc.csv`; luego
  calcular ETc con `riego_et.py`.

## 7. Manejo sanitario (MIP)
> ⚠️ **Seguridad y legalidad (CLAUDE.md §4):** el manual de 2016 menciona ingredientes
> activos que **hoy están restringidos o prohibidos en Costa Rica** (p. ej. endosulfán,
> aldicarb, forato/phorate, metamidofos). **No se transcriben como recomendación.**
> Antes de recomendar cualquier producto o dosis, **verificar el registro SFE vigente**,
> el ingrediente activo permitido y el **periodo de carencia (PHI)**. Aquí se resume el
> criterio de manejo (cultural → biológico → químico) y los umbrales de monitoreo, que
> son la parte accionable y segura.

**Tizón tardío (*Phytophthora infestans*)** — enfermedad #1 en zona fría y húmeda (p.56):
- **Favorecen:** días frescos/nublados, lluvia frecuente, 15–25 °C.
- **Síntomas:** manchas acuosas pardo-rojizas que ennegrecen y cubren hoja/tallo; micelio
  blanco en el envés; puede llegar al tubérculo.
- **Manejo cultural:** eliminar fuentes de inóculo (tubérculos/aporcos de cosecha
  anterior), rotación con no-solanáceas, buen drenaje, semilla sana, densidad adecuada,
  aporca alta y oportuna, fertilización según análisis.
- **Resistencia varietal:** usar variedades con resistencia de campo (Única > Floresta;
  Durán, Kamuk, Pasquí, Yema de huevo tolerantes) (p. 14-20).
- **Químico (categorías, sin dosis):** protectores preventivos (p. ej. cimoxanil+mancozeb,
  dimetomorf+mancozeb) y sistémicos (metalaxil, propamocarb, fosetil-Al) — **verificar SFE
  y carencia**. Ficha detallada en `conocimiento/plagas-enfermedades/tizon-tardio-papa.md`.

**Otras enfermedades (p. 56-69):** costra negra (*Rhizoctonia solani*), tizón temprano
(*Alternaria solani*), pudrición seca (*Fusarium* sp.), roña (*Spongospora subterranea*),
torbó (*Rosellinia* sp.); bacterianas: pie negro/pudrición blanda (*Erwinia*/*Pectobacterium
carotovorum*), marchitez bacteriana (*Ralstonia solanacearum*), sarna común
(*Streptomyces scabies*); virosis: PLRV, PVY, PVX, PVS, PMTV → base del manejo: **semilla
certificada libre de virus**, eliminación de plantas enfermas, higiene.

**Plagas insectiles (p. 70-78):**
- **Polillas de la papa** (*Tecia solanivora* — daña solo tubérculo; *Phthorimaea
  operculella* — tubérculo y follaje): **monitoreo con trampas de feromona (16 trampas/ha),
  muestreo semanal; umbral de acción 60–100 adultos/trampa/semana** (p. 74); cosecha
  oportuna. | dato de umbral | INTA 2016 p.74 | alto.
- Mosca minadora (*Liriomyza huidobrensis*): trampas amarillas + manejo; áfidos (*Myzus
  persicae*) vectores de virus; pulga saltona (*Epitrix* sp.); gusanos cortadores/alambre
  (*Agrotis* sp.); jobotos (*Phyllophaga* spp.) con entomopatógenos (*Beauveria bassiana*,
  *Metarhizium anisopliae*). *Bactericera cockerelli* **no reportada en CR** (vigilancia).
- **Nematodos (p. 78):** *Globodera pallida*, *Meloidogyne* sp., *Pratylenchus* sp. →
  semilla certificada libre, rotación (zanahoria, avena, brócoli, coliflor, arveja,
  cebolla), solarización, control biológico (*Paecilomyces lilacinus*, *Trichoderma*).

## 8. Cosecha y poscosecha
- **Índice de cosecha:** madurez fisiológica — **piel suberizada que no se desprende al
  frotar**; cosechar ~**3 semanas después de eliminar el follaje** (p. 86).
- **Manejo:** matar follaje al alcanzar madurez, cosecha manual (garabato) o mecánica,
  clasificar por calidad/destino, destruir residuos, almacenar tubérculos secos, limpios
  y sanos (p. 86).

## 9. Rendimiento
- **Promedio nacional: 25 t/ha** (Comisión Nacional de la Papa, MAG 2016, cit. p. 8).
- **Por cantón (t/ha, MAG 2016, p. 11):** Cartago 25,5 · Alvarado 25,2 · Zarcero 23,8 ·
  Turrialba 23,8 · Naranjo 23,6 · El Guarco 23,1 · Oreamuno 22,3 · Dota 21,5 · Paraíso
  17,9 · Coronado 16,9 · Goicoechea 16,7.
- **Potencial varietal con buena semilla y manejo:** Floresta ~40 t/ha; Única 45 t/ha;
  Durán y Kamuk hasta 50 t/ha; Idiafrit 40–45 t/ha (p. 14-20). | dato | INTA 2016 | alto.
- **Brecha:** ⟨inferencia⟩ el promedio nacional (25) está muy por debajo del potencial
  (40–50), señal de que semilla, sanidad (tizón) y nutrición limitan el rendimiento real.

## 10. Economía
- El manual incluye un capítulo de "Costos de producción" (Cap. 3, p. 87) pero **las
  cifras no se pudieron extraer** en esta consulta → `[POR COMPLETAR]` (revisar esa
  sección y complementar con SEPSA/CNP para precios ₡/kg y estructura de costos).
- Umbral de rentabilidad: `[POR COMPLETAR]` (calcular con `economia.py` una vez con costos).

## 11. Vacíos de información
- T base para grados-día; Kc FAO-56 por etapa; extracción por tonelada (falta base de
  rendimiento); ventanas de siembra/cosecha por mes; costos y precios; encalado local.
- **Registro SFE vigente y periodos de carencia** de los productos para tizón y polilla
  (crítico antes de cualquier recomendación química).
- Variedades vigentes hoy (el manual es de 2016; el INTA anunció nuevas liberaciones en
  2025 — buscar la publicación primaria).

## 12. Fuentes
- **Avilés Chaves, J. & Piedra Naranjo, R. (2016).** *Manual del cultivo de papa en Costa
  Rica: Solanum tuberosum L.* INTA/PRIICA. ISBN 978-9968-586-11-5.
  https://hdl.handle.net/11324/3145 — fuente primaria (consultado 2026-09-29).
- Fuentes citadas dentro del manual y usadas aquí: MAG (2016) / Comisión Nacional de la
  Papa; FAO (2008); PIMA/Gutiérrez (2014). Verificar las primarias al profundizar.
- BibTeX: `fuentes/refs/papa.bib` · Bitácora: `fuentes/logs/papa_busqueda_2026-09-29.md`.
