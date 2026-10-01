# Guía de reunión con el agrónomo experto

> Objetivo de la reunión: convertir criterio agronómico tácito (lo que un buen
> agrónomo “sabe”) en reglas, parámetros y fuentes que el asistente pueda usar.
> No busques respuestas largas: busca **umbrales, rangos, reglas de decisión y
> nombres de fuentes/instituciones**. Graba (con permiso) y toma notas contra este
> guion. Todo lo que consigas se vuelca a `conocimiento/` y `datos/`.

## 0. Encuadre (2 min)
- Explicar qué es: un asistente que **cita, calcula y registra**, no que improvisa.
- Dejar claro el rol del experto: **validar criterio y señalar fuentes de confianza**,
  no redactar. Nosotros redactamos y le pedimos que corrija.

## 1. Alcance y prioridades (decisión clave)
- ¿Qué cultivos deberían ir **primero**? Ver lista propuesta en
  `docs/decisiones-pendientes.md` (§Cultivos). Pedirle que ordene por
  importancia/impacto y por dónde él puede aportar más.
- ¿El foco inmediato es **alimentación**, **agroexportación** o **floristería/
  follajes**? ¿Alguna finca o cliente real que sirva de caso piloto?
- ¿Hay un cultivo donde el criterio local difiere fuerte de la literatura
  internacional? (esos son los de mayor valor para capturar).

## 2. Fuentes de confianza (crítico para la regla de “cero datos inventados”)
- ¿Qué **fuentes** considera fiables y usa él en su práctica? (manuales MAG/INTA,
  guías del CIA-UCR, boletines, revistas, autores concretos).
- ¿Qué fuentes considera **poco fiables o desactualizadas** y deberíamos evitar?
- ¿Documentos/PDF/manuales que nos pueda **compartir directamente**?
- ¿A qué **instituciones/personas** acudir para dosis de agroquímicos, registro de
  productos (SFE), material vegetal certificado, análisis de suelos y foliares?

## 3. El ciclo de cultivo (marco que usaremos en cada monografía)
Para 1–2 cultivos de ejemplo, recorrer el ciclo y anotar **números**:
- **Sitio y suelo:** rangos de altitud, pH, textura y drenaje ideales; análisis
  mínimos antes de sembrar; cómo interpreta un análisis de suelo (qué mira primero).
- **Siembra:** época(s) por vertiente, densidad (plantas/ha), distancias, material
  vegetal recomendado y de dónde se consigue.
- **Nutrición:** extracción del cultivo (kg de N-P-K por t de producto), programa de
  fertilización por etapa, fuentes preferidas, uso de foliares y bioestimulantes.
- **Agua:** requerimiento hídrico, cuándo el riego es rentable, coeficientes de
  cultivo (Kc) si los maneja, señales de estrés.
- **Fenología/estacionalidad:** etapas y su duración (días o grados-día), ventana de
  cosecha, cómo cambia con altitud.
- **Sanidad (MIP):** 3–5 plagas/enfermedades clave por cultivo, **umbral de acción**,
  monitoreo, manejo (cultural → biológico → químico) y periodo de carencia.
- **Cosecha y poscosecha:** índices de cosecha, manejo, mermas típicas.
- **Rendimiento:** rango realista bueno/medio/malo (t/ha) en CR, no el del folleto.

## 4. Economía (para que el asistente calcule rentabilidad)
- Estructura de costos típica por ha (o los rubros que más pesan).
- Precios de referencia y **dónde consultarlos** (CNP, SEPSA, ferias, exportador).
- ¿Qué margen o umbral hace que un cultivo “valga la pena” frente a alternativas?

## 5. Cómo diagnostica (para codificar su lógica)
- Cuando un productor le describe un problema, ¿qué **preguntas hace primero**?
- ¿Qué confunde a la gente? (deficiencia vs. enfermedad, riego vs. sales, etc.)
- Un “árbol de decisión” mental para 1–2 problemas comunes (amarillamiento, poca
  producción, etc.). Esto se vuelve un protocolo en `conocimiento/protocolos/`.

## 6. Herramientas y datos que él ya usa
- ¿Usa hojas de cálculo, apps, imágenes satelitales/dron (NDVI/NDRE), estaciones
  meteorológicas, análisis de laboratorio? ¿Cuáles?
- ¿Qué cálculo repetitivo le quita tiempo y le gustaría automatizar? (candidatos #1
  para las herramientas Python).
- ¿Lleva registros de finca? ¿En qué formato? (define el esquema de `datos/registros/`).

## 7. Cierre
- Acordar **1 cultivo piloto** para completar de punta a punta como estándar de
  calidad.
- Pedir los documentos prometidos y permiso para citarlo/atribuir.
- Fijar cómo revisará y corregirá lo que produzcamos (cada monografía necesita su
  visto bueno).

---

### Plantilla rápida para tomar notas en la reunión

```
Cultivo: __________  Zona/altitud: __________
Sitio ideal (pH, textura, altitud): __________
Época de siembra (vertiente): __________   Densidad: ______ plantas/ha
Extracción NPK / programa fertilización: __________
Riego (cuándo rentable, Kc): __________
Fenología (etapas, días): __________
MIP (plaga | umbral | manejo | carencia): __________
Rendimiento realista (bueno/medio/malo t/ha): __________
Costos que más pesan / precio referencia: __________
Fuente(s) que él recomienda: __________
```
