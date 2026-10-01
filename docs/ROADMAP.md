# ROADMAP — Agriconsultor

Construcción por fases. Cada fase deja algo usable. Marcar el avance aquí.

## Fase 1 — Cimientos  ✅ (en curso, esta sesión)
- [x] Estructura de carpetas y `CLAUDE.md` (carta de operación).
- [x] Metodología y arquitectura documentadas.
- [x] Plantillas: monografía de cultivo, registro de finca, esquema de datos.
- [x] Herramientas base funcionales: índices de vegetación, grados-día, ET/riego,
      utilidades de unidades (con tests).
- [x] Esquema de datos y CSV semilla (parámetros, estacionalidad, Kc).
- [x] Prompt maestro de traspaso (`docs/PROMPT-MAESTRO.md`).
- [ ] Validación de supuestos con el usuario/agrónomo (`decisiones-pendientes.md`).

## Fase 2 — Contenido agronómico
- [~] **Cultivo piloto: papa** — monografía completada de punta a punta con fuente
      primaria INTA 2016 (`conocimiento/cultivos/papa/papa.md`), ficha MIP de tizón
      tardío y datos volcados a `datos/parametros/`. **Pendiente:** validación del
      agrónomo, Kc (FAO-56), T base, costos y verificación SFE de agroquímicos.
- [ ] Completar cultivos prioritarios (ver `decisiones-pendientes.md` §Cultivos).
- [ ] Protocolos de decisión: diagnóstico general, plan de fertilización, plan de
      riego, MIP, interpretación de análisis de suelo/foliar.
- [ ] Fichas de suelos (andisoles, ultisoles, inceptisoles de CR) y clima
      (zonas agroclimáticas, ETo, régimen por vertiente).
- [ ] Poblar `datos/parametros/` con coeficientes citados.

## Fase 3 — Cálculo agronómico guiado por datos
- [ ] `fertilizacion.py`: dosis por balance (extracción − suelo)/eficiencia, leyendo
      coeficientes de `datos/`.
- [ ] `economia.py`: costo/ingreso/margen y umbral de rentabilidad por cultivo.
- [ ] `densidad_siembra.py`: población, arreglos, semilla requerida.
- [ ] Cobertura de tests y validación con casos reales del agrónomo.

## Fase 4 — Registros de finca (bases de datos del usuario)
- [ ] Esquema SQLite de fincas/lotes/labores/aplicaciones/cosechas/monitoreo.
- [ ] Importar/exportar CSV; generación de informes por lote y por ciclo.
- [ ] Consultas: historial, costos acumulados, calendario de labores.

## Fase 5 — Teledetección operativa
- [ ] Módulo opcional para índices desde imágenes reales (Sentinel-2/Landsat, dron).
- [ ] Integración con Google Earth Engine / STAC / rasterio (aislada, opcional).
- [ ] Series temporales de NDVI/NDRE por lote y alertas.

## Fase 6 — Distribución
- [ ] Empaquetar como servidor MCP para usar desde otros clientes.
- [ ] Documentar instalación y actualización del conocimiento.

## Principios que no cambian entre fases
- Cero datos inventados; todo con fuente y fecha.
- Todo cálculo auditable, con test cuando es determinista.
- El agrónomo valida el conocimiento antes de marcarlo "validado".
