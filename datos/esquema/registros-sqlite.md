# Esquema SQLite de registros de finca (Fase 4)

Modelo relacional propuesto para las bitácoras. Fuente de verdad editable en CSV o
directamente en SQLite; el asistente lee/escribe aquí para "recordar" cada cultivo.

```sql
CREATE TABLE finca (
  id INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  canton TEXT, lat REAL, lon REAL, altitud_msnm REAL,
  notas TEXT
);

CREATE TABLE lote (
  id INTEGER PRIMARY KEY,
  finca_id INTEGER NOT NULL REFERENCES finca(id),
  nombre TEXT NOT NULL,
  area_ha REAL,
  cultivo_slug TEXT,           -- coincide con conocimiento/cultivos/<slug>
  variedad TEXT,
  sistema TEXT,                -- abierto/protegido/organico/convencional
  fecha_siembra TEXT,          -- ISO AAAA-MM-DD
  fecha_cosecha_estimada TEXT
);

CREATE TABLE analisis_suelo (
  id INTEGER PRIMARY KEY,
  lote_id INTEGER NOT NULL REFERENCES lote(id),
  fecha TEXT, laboratorio TEXT,
  ph REAL, mo_pct REAL, n TEXT, p TEXT, k TEXT, ca TEXT, mg TEXT, cic TEXT,
  archivo TEXT                 -- ruta al PDF/imagen del análisis
);

CREATE TABLE labor (
  id INTEGER PRIMARY KEY,
  lote_id INTEGER NOT NULL REFERENCES lote(id),
  fecha TEXT, tipo TEXT, detalle TEXT,
  insumo TEXT, dosis TEXT, costo REAL, responsable TEXT, notas TEXT
);

CREATE TABLE aplicacion (
  id INTEGER PRIMARY KEY,
  lote_id INTEGER NOT NULL REFERENCES lote(id),
  fecha TEXT, producto TEXT, ingrediente_activo TEXT, registro_sfe TEXT,
  dosis TEXT, objetivo TEXT, carencia_dias INTEGER, reingreso_horas INTEGER, notas TEXT
);

CREATE TABLE monitoreo (
  id INTEGER PRIMARY KEY,
  lote_id INTEGER NOT NULL REFERENCES lote(id),
  fecha TEXT, etapa TEXT, gdd_acum REAL,
  observacion TEXT, incidencia REAL, severidad REAL, umbral TEXT, decision TEXT
);

CREATE TABLE riego (
  id INTEGER PRIMARY KEY,
  lote_id INTEGER NOT NULL REFERENCES lote(id),
  fecha TEXT, lamina_mm REAL, metodo TEXT, eto REAL, kc REAL, notas TEXT
);

CREATE TABLE cosecha (
  id INTEGER PRIMARY KEY,
  lote_id INTEGER NOT NULL REFERENCES lote(id),
  fecha TEXT, cantidad REAL, unidad TEXT, categoria TEXT, destino TEXT,
  precio REAL, moneda TEXT, notas TEXT
);
```

Consultas típicas que habilitará el asistente (Fase 4): historial por lote, costo
acumulado del ciclo, calendario de labores pendientes, alertas de carencia (PHI)
antes de cosecha, y comparación de rendimiento entre ciclos/lotes.
