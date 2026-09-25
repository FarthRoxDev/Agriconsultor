"""Requerimiento de fertilizante por balance de nutrientes.

Enfoque de balance (simplificado):

    Dosis(nutriente) = ( Extracción - Aporte del suelo ) / Eficiencia de uso

- Extracción: nutriente que el cultivo remueve para el rendimiento meta
  (kg nutriente / t producto  ×  t/ha meta). De datos/parametros/ y la ficha del cultivo.
- Aporte del suelo: estimado del análisis de suelo (requiere factor de conversión de
  ppm/meq a kg/ha según profundidad y densidad aparente). Aquí se recibe ya en kg/ha,
  o se calcula con `disponible_suelo_kg_ha`.
- Eficiencia de uso del nutriente (0–1): pérdidas por lixiviación, volatilización,
  fijación. Depende de fuente, suelo y manejo.

Nutrientes expresados como N, P₂O₅, K₂O (convención comercial). Para pasar a elemento:
P = P₂O₅ * 0.4364 ; K = K₂O * 0.8301 (y viceversa con el inverso).

IMPORTANTE (CLAUDE.md): esto es el MOTOR de cálculo. Los coeficientes de extracción,
eficiencia y los factores de suelo deben venir de datos/parametros/ con su fuente. No
hay valores por defecto de cultivo aquí a propósito, para no inducir números inventados.
"""
from __future__ import annotations

from dataclasses import dataclass

# Factores de conversión óxido <-> elemento
P2O5_A_P = 0.4364
P_A_P2O5 = 1 / P2O5_A_P
K2O_A_K = 0.8301
K_A_K2O = 1 / K2O_A_K


@dataclass
class Nutriente:
    """Balance de un nutriente (todo en kg/ha)."""
    nombre: str
    extraccion_kg_ha: float      # removido por el rendimiento meta
    aporte_suelo_kg_ha: float    # disponible del suelo (de análisis)
    eficiencia: float            # 0–1

    def dosis_kg_ha(self) -> float:
        """Dosis a aplicar (kg/ha del nutriente). No negativa."""
        if not 0 < self.eficiencia <= 1:
            raise ValueError(f"{self.nombre}: eficiencia debe estar en (0, 1].")
        deficit = self.extraccion_kg_ha - self.aporte_suelo_kg_ha
        return max(0.0, deficit / self.eficiencia)


def extraccion_por_rendimiento(extraccion_por_t: float, rendimiento_t_ha: float) -> float:
    """Extracción (kg/ha) = (kg nutriente / t producto) * (t/ha meta)."""
    if extraccion_por_t < 0 or rendimiento_t_ha < 0:
        raise ValueError("Valores no negativos requeridos.")
    return extraccion_por_t * rendimiento_t_ha


def disponible_suelo_kg_ha(valor_analisis: float, factor_kg_ha_por_unidad: float) -> float:
    """Convierte un valor de análisis de suelo a kg/ha disponibles.

    factor_kg_ha_por_unidad depende de la unidad del análisis (ppm, meq/100g, mg/L),
    la profundidad muestreada y la densidad aparente. Debe venir de la ficha de suelos
    (conocimiento/suelos/) con su justificación. No se asume aquí.
    """
    return valor_analisis * factor_kg_ha_por_unidad


def dosis_fuente_comercial(dosis_nutriente_kg_ha: float, riqueza_pct: float) -> float:
    """kg/ha de producto comercial = dosis del nutriente / (riqueza/100).

    riqueza_pct: % del nutriente en la fuente (p. ej. urea 46% N; KCl 60% K₂O).
    """
    if not 0 < riqueza_pct <= 100:
        raise ValueError("La riqueza debe estar en (0, 100] %.")
    return dosis_nutriente_kg_ha / (riqueza_pct / 100.0)
