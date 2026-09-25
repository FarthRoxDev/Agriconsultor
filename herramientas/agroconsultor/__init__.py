"""agroconsultor — herramientas de cálculo agronómico auditable para Costa Rica.

Cada módulo expone funciones puras y deterministas. Regla de oro (ver CLAUDE.md):
todo cálculo debe poder mostrar fórmula, supuestos, unidades y origen de datos.
Las funciones documentan sus unidades en el docstring; no adivines unidades.

Módulos:
- indices_vegetacion : NDVI, GNDVI, NDRE, SAVI, EVI, NDWI... (teledetección)
- grados_dia         : tiempo térmico (GDD) para fenología
- riego_et           : evapotranspiración del cultivo (ETc = ETo * Kc) y balance hídrico
- densidad_siembra   : población, semilla requerida, arreglos espaciales
- fertilizacion      : requerimiento de nutrientes por balance
- economia           : costo, ingreso, margen y punto de equilibrio
- util_unidades      : conversiones y ayudas de unidades (SI)
"""

__version__ = "0.1.0"

__all__ = [
    "indices_vegetacion",
    "grados_dia",
    "riego_et",
    "densidad_siembra",
    "fertilizacion",
    "economia",
    "util_unidades",
]
