"""Evapotranspiración del cultivo y balance hídrico simple (enfoque FAO-56).

ETc = ETo * Kc
  ETo : evapotranspiración de referencia (mm/día), del dato climático (IMN, estación,
        o cálculo Penman-Monteith aparte). Aquí se toma como entrada.
  Kc  : coeficiente de cultivo por etapa (adimensional), de datos/parametros/coeficientes_kc.csv.

Referencia: Allen et al. (1998), FAO Irrigation and Drainage Paper 56.
Unidades: ETo y ETc en mm/día; lámina en mm; volumen en m³ (1 mm sobre 1 ha = 10 m³).
"""
from __future__ import annotations

from typing import Iterable


def etc(eto: float, kc: float) -> float:
    """ETc (mm/día) = ETo * Kc."""
    if eto < 0 or kc < 0:
        raise ValueError("ETo y Kc deben ser no negativos.")
    return eto * kc


def etc_periodo(eto_diaria: Iterable[float], kc: float) -> float:
    """ETc acumulada (mm) en un periodo con Kc constante y una serie de ETo diaria."""
    return sum(etc(e, kc) for e in eto_diaria)


def requerimiento_neto_riego(etc_mm: float, precip_efectiva_mm: float) -> float:
    """Requerimiento neto de riego (mm) = ETc - Precipitación efectiva (no negativo)."""
    return max(0.0, etc_mm - precip_efectiva_mm)


def requerimiento_bruto_riego(req_neto_mm: float, eficiencia: float) -> float:
    """Requerimiento bruto (mm) = neto / eficiencia del sistema.

    eficiencia (0–1): goteo ~0.9, aspersión ~0.75, gravedad ~0.5-0.6 ⟨referencial⟩.
    """
    if not 0 < eficiencia <= 1:
        raise ValueError("La eficiencia debe estar en (0, 1].")
    return req_neto_mm / eficiencia


def lamina_a_volumen(lamina_mm: float, area_ha: float) -> float:
    """Convierte lámina (mm) sobre un área (ha) a volumen (m³). 1 mm·ha = 10 m³."""
    return lamina_mm * area_ha * 10.0


def precip_efectiva_usda(precip_mm: float) -> float:
    """Precipitación efectiva mensual (mm) — método simplificado USDA-SCS.

    Pe = P*(125 - 0.2*P)/125  si P < 250 mm ; Pe = 125 + 0.1*P  si P >= 250 mm.
    Es una aproximación mensual; para decisiones finas usar balance diario. ⟨referencial⟩
    """
    if precip_mm < 0:
        raise ValueError("La precipitación no puede ser negativa.")
    if precip_mm < 250:
        return precip_mm * (125 - 0.2 * precip_mm) / 125.0
    return 125 + 0.1 * precip_mm
