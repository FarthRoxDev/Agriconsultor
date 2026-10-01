"""Grados-día de crecimiento (GDD) — tiempo térmico para fenología.

El desarrollo de muchos cultivos se predice mejor por acumulación de calor que por
días de calendario. GDD diario = max(0, (Tmax' + Tmin') / 2 - Tbase), con Tmax'/Tmin'
recortadas a un techo (Tupper) opcional.

Unidades: temperaturas en °C; GDD en °C·día.
La Tbase y (si aplica) Tupper dependen del cultivo → tomarlas de la ficha del cultivo
y de datos/parametros/, no adivinarlas.
"""
from __future__ import annotations

from typing import Iterable, Optional


def gdd_dia(tmax: float, tmin: float, tbase: float,
            tupper: Optional[float] = None, metodo: str = "simple") -> float:
    """Grados-día de UN día.

    metodo:
      - "simple": GDD = max(0, (Tmax+Tmin)/2 - Tbase). Si tupper, recorta la media a tupper.
      - "recorte": recorta Tmax y Tmin al rango [Tbase, Tupper] ANTES de promediar
        (método del horizontal cutoff, común en manuales de fenología).
    """
    if tmin > tmax:
        raise ValueError("Tmin no puede ser mayor que Tmax.")
    if metodo == "simple":
        media = (tmax + tmin) / 2.0
        if tupper is not None:
            media = min(media, tupper)
        return max(0.0, media - tbase)
    if metodo == "recorte":
        hi, lo = tmax, tmin
        if tupper is not None:
            hi = min(hi, tupper)
            lo = min(lo, tupper)
        hi = max(hi, tbase)
        lo = max(lo, tbase)
        return max(0.0, (hi + lo) / 2.0 - tbase)
    raise ValueError(f"Método desconocido: {metodo!r} (usar 'simple' o 'recorte').")


def gdd_acumulado(temperaturas: Iterable[tuple[float, float]], tbase: float,
                  tupper: Optional[float] = None, metodo: str = "simple") -> float:
    """GDD acumulado sobre una serie de días.

    temperaturas: iterable de tuplas (Tmax, Tmin) por día.
    Devuelve la suma de GDD diarios (°C·día).
    """
    return sum(gdd_dia(tmax, tmin, tbase, tupper, metodo) for tmax, tmin in temperaturas)


def dias_a_etapa(temperaturas: Iterable[tuple[float, float]], tbase: float,
                 gdd_objetivo: float, tupper: Optional[float] = None,
                 metodo: str = "simple") -> Optional[int]:
    """Día (1-indexado) en que el GDD acumulado alcanza gdd_objetivo.

    Útil para estimar cuándo se llega a una etapa fenológica dado un pronóstico o
    serie histórica de temperaturas. Devuelve None si no se alcanza en la serie.
    """
    acum = 0.0
    for i, (tmax, tmin) in enumerate(temperaturas, start=1):
        acum += gdd_dia(tmax, tmin, tbase, tupper, metodo)
        if acum >= gdd_objetivo:
            return i
    return None
