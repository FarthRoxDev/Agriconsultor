"""Tests de las herramientas deterministas. Ejecutar: python -m pytest desde herramientas/."""
import math

import pytest

from agroconsultor import (
    indices_vegetacion as iv,
    grados_dia as gd,
    riego_et as ret,
    densidad_siembra as ds,
    fertilizacion as fe,
    economia as ec,
    util_unidades as uu,
)


# --- índices de vegetación ---
def test_ndvi_basico():
    assert iv.ndvi(nir=0.5, red=0.1) == pytest.approx((0.5 - 0.1) / (0.5 + 0.1))

def test_ndvi_rango():
    assert -1 <= iv.ndvi(nir=0.1, red=0.5) <= 1

def test_savi_l_cero_igual_ndvi():
    # Con L=0, SAVI se reduce a NDVI.
    assert iv.savi(0.5, 0.1, l=0.0) == pytest.approx(iv.ndvi(0.5, 0.1))

def test_indice_division_cero():
    with pytest.raises(ValueError):
        iv.ndvi(nir=0.0, red=0.0)

def test_interpretar_ndvi():
    assert "Suelo" in iv.interpretar_ndvi(0.1) or "escasa" in iv.interpretar_ndvi(0.1)


# --- grados-día ---
def test_gdd_dia_simple():
    # media 25, base 10 -> 15
    assert gd.gdd_dia(tmax=30, tmin=20, tbase=10) == pytest.approx(15.0)

def test_gdd_no_negativo():
    assert gd.gdd_dia(tmax=8, tmin=4, tbase=10) == 0.0

def test_gdd_tupper_recorta():
    # media 27 recortada a 26
    assert gd.gdd_dia(tmax=34, tmin=20, tbase=10, tupper=26) == pytest.approx(16.0)

def test_gdd_acumulado_y_dias():
    serie = [(30, 20)] * 4  # 15 GDD/día
    assert gd.gdd_acumulado(serie, tbase=10) == pytest.approx(60.0)
    assert gd.dias_a_etapa(serie, tbase=10, gdd_objetivo=45) == 3

def test_gdd_tmin_mayor_tmax():
    with pytest.raises(ValueError):
        gd.gdd_dia(tmax=10, tmin=20, tbase=5)


# --- riego / ET ---
def test_etc():
    assert ret.etc(eto=5.0, kc=1.1) == pytest.approx(5.5)

def test_requerimiento_neto_no_negativo():
    assert ret.requerimiento_neto_riego(etc_mm=30, precip_efectiva_mm=40) == 0.0

def test_requerimiento_bruto():
    assert ret.requerimiento_bruto_riego(req_neto_mm=45, eficiencia=0.9) == pytest.approx(50.0)

def test_lamina_a_volumen():
    assert ret.lamina_a_volumen(lamina_mm=10, area_ha=2) == pytest.approx(200.0)


# --- densidad ---
def test_densidad_marco():
    # 0.9 x 0.2 m -> 10000/0.18 ≈ 55555.6 plantas/ha
    assert ds.densidad_por_marco(0.9, 0.2) == pytest.approx(10000 / 0.18)

def test_semilla_requerida():
    # 1 ha, densidad 50000, 1 semilla/sitio, germinación 100%, 20000 semillas/kg -> 2.5 kg
    kg = ds.semilla_requerida_kg(densidad_plantas_ha=50000, area_ha=1,
                                 semillas_por_kg=20000, germinacion=1.0)
    assert kg == pytest.approx(2.5)

def test_marco_desde_poblacion():
    d = ds.poblacion_objetivo_a_marco(densidad_objetivo_plantas_ha=55555.56,
                                      dist_entre_hileras_m=0.9)
    assert d == pytest.approx(0.2, rel=1e-3)


# --- fertilización ---
def test_extraccion_y_dosis():
    ext = fe.extraccion_por_rendimiento(extraccion_por_t=25, rendimiento_t_ha=6)  # 150
    n = fe.Nutriente("N", extraccion_kg_ha=ext, aporte_suelo_kg_ha=30, eficiencia=0.6)
    assert n.dosis_kg_ha() == pytest.approx((150 - 30) / 0.6)  # 200

def test_dosis_no_negativa():
    n = fe.Nutriente("N", extraccion_kg_ha=20, aporte_suelo_kg_ha=50, eficiencia=0.6)
    assert n.dosis_kg_ha() == 0.0

def test_dosis_fuente_comercial():
    # 92 kg N / (46/100) = 200 kg urea
    assert fe.dosis_fuente_comercial(92, riqueza_pct=46) == pytest.approx(200.0)

def test_conversion_oxido():
    assert fe.P2O5_A_P == pytest.approx(0.4364)


# --- economía ---
def test_margen_y_relaciones():
    p = ec.Presupuesto(costos={"insumos": 1000, "labor": 500}, rendimiento=100, precio_unitario=20)
    assert p.costo_total() == 1500
    assert p.ingreso_bruto() == 2000
    assert p.margen_bruto() == 500
    assert p.relacion_beneficio_costo() == pytest.approx(2000 / 1500)
    assert p.rendimiento_equilibrio() == pytest.approx(75.0)
    assert p.precio_equilibrio() == pytest.approx(15.0)


# --- unidades ---
def test_unidades():
    assert uu.mm_a_m3_ha(10) == 100.0
    assert uu.kg_ha_a_g_planta(kg_ha=50, plantas_ha=50000) == pytest.approx(1.0)
    assert uu.c_a_f(100) == 212.0
    assert uu.convertir_moneda(10, tipo_cambio=520) == 5200.0
