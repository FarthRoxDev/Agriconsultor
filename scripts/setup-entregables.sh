#!/usr/bin/env bash
# setup-entregables.sh — instala la cadena de generación de entregables de Agriconsultor
# (presentaciones, documentos y PDFs/libros) de forma idempotente. Seguro de re-ejecutar:
# salta lo que ya está instalado. Pensado para Claude Code (local y en la web) y para
# clones nuevos del repo. Ver entregables/README.md.
#
# Uso:  bash scripts/setup-entregables.sh [--quiet]
set -uo pipefail

QUIET="${1:-}"
log(){ [ "$QUIET" = "--quiet" ] || echo "[setup-entregables] $*"; }
have(){ command -v "$1" >/dev/null 2>&1; }

# Versiones fijadas (actualizar cuando se quiera subir de versión)
PANDOC_VER="3.12"
TYPST_VER="0.15.1"
QUARTO_VER="1.11.5"
BIN="/usr/local/bin"
ARCH="$(uname -m)"

ok=0; fail=0
mark(){ if [ "$1" = ok ]; then ok=$((ok+1)); else fail=$((fail+1)); fi; }

# --- 1) Python: python-pptx (.pptx), python-docx (.docx) ---
if have python3; then
  if python3 -c "import pptx, docx" 2>/dev/null; then
    log "python-pptx + python-docx ya presentes"; mark ok
  else
    log "instalando python-pptx + python-docx"
    python3 -m pip install -q python-pptx python-docx && mark ok || { log "FALLO pip"; mark fail; }
  fi
else log "python3 no disponible — omito Python"; mark fail; fi

# --- 2) Node: pptxgenjs + marp-cli (locales a entregables/) ---
if have npm; then
  if [ -d entregables ]; then
    if [ ! -d entregables/node_modules ]; then
      log "npm install en entregables/"
      ( cd entregables && npm install --no-audit --no-fund >/dev/null 2>&1 ) && mark ok || { log "FALLO npm"; mark fail; }
    else log "node_modules de entregables ya presente"; mark ok; fi
  else log "carpeta entregables/ ausente — omito npm"; fi
else log "npm no disponible — omito Node"; mark fail; fi

# --- 3) pandoc (conversor universal) ---
if have pandoc; then log "pandoc ya presente ($(pandoc -v|head -1))"; mark ok
elif [ "$ARCH" = "x86_64" ]; then
  log "descargando pandoc $PANDOC_VER"
  if curl -fsSL --max-time 180 -o /tmp/pandoc.tgz \
      "https://github.com/jgm/pandoc/releases/download/${PANDOC_VER}/pandoc-${PANDOC_VER}-linux-amd64.tar.gz"; then
    tar xzf /tmp/pandoc.tgz -C /tmp && cp "/tmp/pandoc-${PANDOC_VER}/bin/pandoc" "$BIN/" && mark ok || mark fail
  else log "FALLO descarga pandoc (red/proxy)"; mark fail; fi
else log "arch $ARCH no soportada por este script para pandoc"; mark fail; fi

# --- 4) typst (maquetación y motor PDF de pandoc) ---
if have typst; then log "typst ya presente ($(typst --version))"; mark ok
elif [ "$ARCH" = "x86_64" ]; then
  log "descargando typst $TYPST_VER"
  if curl -fsSL --max-time 180 -o /tmp/typst.txz \
      "https://github.com/typst/typst/releases/download/v${TYPST_VER}/typst-x86_64-unknown-linux-musl.tar.xz"; then
    tar xf /tmp/typst.txz -C /tmp && cp /tmp/typst-x86_64-unknown-linux-musl/typst "$BIN/" && mark ok || mark fail
  else log "FALLO descarga typst"; mark fail; fi
else log "arch $ARCH no soportada para typst"; mark fail; fi

# --- 5) quarto (una fuente -> libro, slides y PDF) ---
if have quarto; then log "quarto ya presente ($(quarto --version))"; mark ok
elif [ "$ARCH" = "x86_64" ]; then
  log "descargando quarto $QUARTO_VER"
  if curl -fsSL --max-time 240 -o /tmp/quarto.tgz \
      "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VER}/quarto-${QUARTO_VER}-linux-amd64.tar.gz"; then
    mkdir -p /opt/quarto && tar xzf /tmp/quarto.tgz -C /opt/quarto --strip-components=1 \
      && ln -sf /opt/quarto/bin/quarto "$BIN/quarto" && mark ok || mark fail
  else log "FALLO descarga quarto"; mark fail; fi
else log "arch $ARCH no soportada para quarto"; mark fail; fi

log "listo: $ok componentes OK, $fail con problemas."
[ "$fail" -eq 0 ]
