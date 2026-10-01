"""Utilidades de unidades (SI) y conversiones agronómicas frecuentes.

El asistente debe trabajar en SI (CLAUDE.md). Estas ayudas evitan errores comunes.
"""
from __future__ import annotations

# Área
HA_A_M2 = 10_000.0
MZ_A_HA = 0.6989      # 1 manzana (CR) ≈ 0.6989 ha (10 000 varas²) ⟨verificar uso local⟩


def ha_a_m2(ha: float) -> float:
    return ha * HA_A_M2


def m2_a_ha(m2: float) -> float:
    return m2 / HA_A_M2


def manzana_a_ha(mz: float) -> float:
    """Manzana costarricense a hectárea. Confirmar la definición usada en la región."""
    return mz * MZ_A_HA


# Rendimiento / dosis
def kg_ha_a_g_planta(kg_ha: float, plantas_ha: float) -> float:
    """Convierte una dosis en kg/ha a g/planta dada la densidad."""
    if plantas_ha <= 0:
        raise ValueError("plantas_ha debe ser > 0.")
    return (kg_ha * 1000.0) / plantas_ha


def g_planta_a_kg_ha(g_planta: float, plantas_ha: float) -> float:
    return (g_planta * plantas_ha) / 1000.0


# Lámina de agua
def mm_a_m3_ha(mm: float) -> float:
    """1 mm de lámina sobre 1 ha = 10 m³."""
    return mm * 10.0


# Temperatura
def c_a_f(c: float) -> float:
    return c * 9 / 5 + 32


def f_a_c(f: float) -> float:
    return (f - 32) * 5 / 9


# Nutrientes óxido <-> elemento (duplicado útil; fuente en fertilizacion.py)
def p2o5_a_p(p2o5: float) -> float:
    return p2o5 * 0.4364


def k2o_a_k(k2o: float) -> float:
    return k2o * 0.8301


def convertir_moneda(monto: float, tipo_cambio: float) -> float:
    """Convierte usando un tipo de cambio explícito (p. ej. ₡/USD del BCCR).

    monto * tipo_cambio. El llamador DEBE registrar la fecha y fuente del tipo de
    cambio junto al resultado (CLAUDE.md).
    """
    if tipo_cambio <= 0:
        raise ValueError("El tipo de cambio debe ser > 0.")
    return monto * tipo_cambio
