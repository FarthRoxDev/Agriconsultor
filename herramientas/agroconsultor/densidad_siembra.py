"""Densidad de siembra, población y semilla/plantas requeridas.

Unidades: distancias en m; área en ha; densidad en plantas/ha.
1 ha = 10 000 m².
"""
from __future__ import annotations

M2_POR_HA = 10_000.0


def densidad_por_marco(dist_entre_hileras_m: float, dist_entre_plantas_m: float) -> float:
    """Densidad (plantas/ha) para marco rectangular = 10000 / (a * b)."""
    if dist_entre_hileras_m <= 0 or dist_entre_plantas_m <= 0:
        raise ValueError("Las distancias deben ser positivas.")
    return M2_POR_HA / (dist_entre_hileras_m * dist_entre_plantas_m)


def plantas_totales(densidad_plantas_ha: float, area_ha: float) -> float:
    """Plantas totales = densidad * área."""
    return densidad_plantas_ha * area_ha


def semilla_requerida_kg(densidad_plantas_ha: float, area_ha: float,
                         semillas_por_kg: float, germinacion: float = 1.0,
                         plantas_por_sitio: int = 1) -> float:
    """Semilla requerida (kg).

    Ajusta por germinación (0–1) y por semillas sembradas por sitio.
    semillas_por_kg: propio del cultivo/variedad (de datos/parametros/).
    """
    if not 0 < germinacion <= 1:
        raise ValueError("La germinación debe estar en (0, 1].")
    if semillas_por_kg <= 0 or plantas_por_sitio <= 0:
        raise ValueError("semillas_por_kg y plantas_por_sitio deben ser positivos.")
    sitios = plantas_totales(densidad_plantas_ha, area_ha)
    semillas = sitios * plantas_por_sitio / germinacion
    return semillas / semillas_por_kg


def poblacion_objetivo_a_marco(densidad_objetivo_plantas_ha: float,
                               dist_entre_hileras_m: float) -> float:
    """Dada una densidad objetivo y la distancia entre hileras, devuelve la distancia
    entre plantas (m) necesaria dentro de la hilera."""
    if densidad_objetivo_plantas_ha <= 0 or dist_entre_hileras_m <= 0:
        raise ValueError("Valores deben ser positivos.")
    area_por_planta = M2_POR_HA / densidad_objetivo_plantas_ha
    return area_por_planta / dist_entre_hileras_m
