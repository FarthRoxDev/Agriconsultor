"""Índices de vegetación a partir de reflectancias.

Todas las funciones reciben **reflectancia** por banda (valor 0–1, adimensional) y
devuelven el índice adimensional. Sirven tanto para un pixel como para promedios de
lote. No dependen de la fuente de la imagen (Sentinel-2, Landsat, dron multiespectral):
el usuario debe pasar la banda correcta según su sensor.

Bandas típicas (Sentinel-2):
    blue  (azul)      B2  ~490 nm
    green (verde)     B3  ~560 nm
    red   (rojo)      B4  ~665 nm
    red_edge (borde rojo) B5 ~705 nm (también B6/B7)
    nir   (infrarrojo cercano) B8 ~842 nm  /  B8A ~865 nm

Referencias de las fórmulas:
    NDVI  — Rouse et al. (1974)
    GNDVI — Gitelson et al. (1996)
    NDRE  — Barnes et al. (2000)
    SAVI  — Huete (1988)
    EVI   — Huete et al. (2002)
    NDWI  — Gao (1996)  (humedad de la vegetación, usa SWIR)
    NDMI  — Wilson & Sader (2002)
Verificar y citar la fuente exacta en la ficha que use estos valores (CLAUDE.md).
"""
from __future__ import annotations

_EPS = 1e-9  # evita división por cero cuando ambas bandas son ~0


def _norm_diff(a: float, b: float) -> float:
    """Diferencia normalizada (a - b) / (a + b)."""
    denom = a + b
    if abs(denom) < _EPS:
        raise ValueError("Suma de bandas ~0: reflectancias inválidas para índice normalizado.")
    return (a - b) / denom


def ndvi(nir: float, red: float) -> float:
    """NDVI = (NIR - Rojo) / (NIR + Rojo). Vigor/biomasa verde. Rango [-1, 1]."""
    return _norm_diff(nir, red)


def gndvi(nir: float, green: float) -> float:
    """GNDVI = (NIR - Verde) / (NIR + Verde). Sensible a clorofila/N. Rango [-1, 1]."""
    return _norm_diff(nir, green)


def ndre(nir: float, red_edge: float) -> float:
    """NDRE = (NIR - BordeRojo) / (NIR + BordeRojo).

    Mejor que NDVI en dosel denso (se satura menos); útil para estado nitrogenado
    en etapas avanzadas. Rango [-1, 1].
    """
    return _norm_diff(nir, red_edge)


def savi(nir: float, red: float, l: float = 0.5) -> float:
    """SAVI = ((NIR - Rojo) / (NIR + Rojo + L)) * (1 + L).

    Ajusta el efecto del suelo desnudo. L: factor de suelo (0 dosel muy denso,
    1 suelo muy expuesto; 0.5 es el valor genérico de Huete 1988).
    """
    denom = nir + red + l
    if abs(denom) < _EPS:
        raise ValueError("Denominador ~0 en SAVI.")
    return ((nir - red) / denom) * (1 + l)


def evi(nir: float, red: float, blue: float,
        g: float = 2.5, c1: float = 6.0, c2: float = 7.5, l: float = 1.0) -> float:
    """EVI = G * (NIR - Rojo) / (NIR + C1*Rojo - C2*Azul + L).

    Índice de vegetación mejorado (Huete et al. 2002): reduce influencia de suelo y
    atmósfera, se satura menos en biomasa alta. Coeficientes por defecto de MODIS/S2.
    """
    denom = nir + c1 * red - c2 * blue + l
    if abs(denom) < _EPS:
        raise ValueError("Denominador ~0 en EVI.")
    return g * (nir - red) / denom


def ndwi_gao(nir: float, swir: float) -> float:
    """NDWI (Gao 1996) = (NIR - SWIR) / (NIR + SWIR). Contenido de agua del dosel."""
    return _norm_diff(nir, swir)


def ndmi(nir: float, swir1: float) -> float:
    """NDMI = (NIR - SWIR1) / (NIR + SWIR1). Humedad de la vegetación (Wilson & Sader 2002)."""
    return _norm_diff(nir, swir1)


def gci(nir: float, green: float) -> float:
    """Green Chlorophyll Index = (NIR / Verde) - 1 (Gitelson et al. 2003)."""
    if abs(green) < _EPS:
        raise ValueError("Verde ~0 en GCI.")
    return (nir / green) - 1.0


def interpretar_ndvi(valor: float) -> str:
    """Interpretación cualitativa GENÉRICA de NDVI. ⟨inferencia⟩ — no sustituye
    umbrales calibrados por cultivo/etapa (esos van en la ficha del cultivo)."""
    if valor < 0:
        return "Agua, nube o superficie no vegetada."
    if valor < 0.2:
        return "Suelo desnudo o vegetación muy escasa/senescente."
    if valor < 0.4:
        return "Vegetación rala o cultivo en etapa temprana."
    if valor < 0.6:
        return "Vegetación moderada; dosel en desarrollo."
    if valor < 0.8:
        return "Vegetación vigorosa; buena cobertura de dosel."
    return "Dosel muy denso y vigoroso (posible saturación del NDVI)."
