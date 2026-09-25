# Herramientas de cálculo (paquete `agroconsultor`)

Funciones puras y deterministas para cálculo agronómico auditable. El núcleo **no
tiene dependencias** fuera de la biblioteca estándar de Python; `pytest` es solo para
pruebas.

## Uso
```bash
cd herramientas
python3 -m pip install -r requirements.txt   # solo para tests
python3 -m pytest -q                         # correr los tests

python3 -c "from agroconsultor import indices_vegetacion as iv; print(iv.ndvi(nir=0.45, red=0.08))"
```

## Módulos
| Módulo | Qué calcula |
|---|---|
| `indices_vegetacion` | NDVI, GNDVI, NDRE, SAVI, EVI, NDWI, NDMI, GCI e interpretación |
| `grados_dia` | Grados-día (GDD), acumulado y día de llegada a una etapa |
| `riego_et` | ETc = ETo·Kc, requerimiento neto/bruto de riego, lámina→volumen |
| `densidad_siembra` | Densidad por marco, plantas totales, semilla requerida |
| `fertilizacion` | Requerimiento de nutrientes por balance; fuente comercial |
| `economia` | Costo, ingreso, margen, relación B/C, punto de equilibrio |
| `util_unidades` | Conversiones SI y agronómicas frecuentes |

## Regla de oro
Toda función documenta sus **unidades** en el docstring. Los **coeficientes** propios
de cada cultivo (Kc, extracción, densidad, Tbase…) **no** están incrustados en el
código: viven en `datos/parametros/` con su fuente, para no inducir números
inventados (ver `CLAUDE.md`). El motor calcula; los datos aportan los números.

## Cómo agregar una herramienta
1. Crear el módulo en `agroconsultor/` con funciones puras y docstring de unidades.
2. Agregar tests en `tests/`.
3. Si necesita coeficientes, leerlos de `datos/` (no hardcodear valores de cultivo).
4. Registrar la fórmula y su fuente en el docstring o en la ficha que la use.
