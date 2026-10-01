"""Economía básica de un cultivo: costo, ingreso, margen y punto de equilibrio.

Convención de moneda (CLAUDE.md): declarar siempre moneda y, si hay conversión,
tipo de cambio del BCCR con fecha. Estas funciones son agnósticas a la moneda; el
llamador mantiene la coherencia (todo en ₡ o todo en USD).
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Presupuesto:
    """Presupuesto por hectárea (o por lote; mantener consistente la base)."""
    costos: dict[str, float] = field(default_factory=dict)  # rubro -> monto
    rendimiento: float = 0.0        # unidades de producto por ha (kg, t, cajas, tallos…)
    precio_unitario: float = 0.0    # moneda por unidad de producto

    def costo_total(self) -> float:
        return sum(self.costos.values())

    def ingreso_bruto(self) -> float:
        return self.rendimiento * self.precio_unitario

    def margen_bruto(self) -> float:
        """Ingreso bruto - costo total."""
        return self.ingreso_bruto() - self.costo_total()

    def costo_unitario(self) -> float:
        """Costo por unidad de producto (costo total / rendimiento)."""
        if self.rendimiento <= 0:
            raise ValueError("Rendimiento debe ser > 0 para costo unitario.")
        return self.costo_total() / self.rendimiento

    def relacion_beneficio_costo(self) -> float:
        """Ingreso bruto / costo total (>1 indica ganancia)."""
        ct = self.costo_total()
        if ct <= 0:
            raise ValueError("Costo total debe ser > 0.")
        return self.ingreso_bruto() / ct

    def rendimiento_equilibrio(self) -> float:
        """Rendimiento (unidades/ha) para cubrir el costo al precio dado."""
        if self.precio_unitario <= 0:
            raise ValueError("Precio unitario debe ser > 0.")
        return self.costo_total() / self.precio_unitario

    def precio_equilibrio(self) -> float:
        """Precio por unidad para cubrir el costo al rendimiento dado."""
        if self.rendimiento <= 0:
            raise ValueError("Rendimiento debe ser > 0.")
        return self.costo_total() / self.rendimiento
