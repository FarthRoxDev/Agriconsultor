// presentacion-pptxgenjs.js — genera un .pptx data-driven con PptxGenJS.
// Uso:  cd entregables && node plantillas/presentacion-pptxgenjs.js
// Salida: entregables/salidas/presentacion-pptxgenjs.pptx
// Regla CLAUDE.md: toda cifra conserva su fuente (ver objeto FUENTE).

const path = require("path");
const fs = require("fs");
const PptxGenJS = require("pptxgenjs");

// --- Datos (idealmente leídos de ../../datos/; aquí embebidos con su fuente) ---
const FUENTE = "MAG 2016, cit. en INTA 2016 (Manual del cultivo de papa en CR), p. 11";
const rendimientoPorCanton = [
  { canton: "Cartago", tHa: 25.5 },
  { canton: "Alvarado", tHa: 25.2 },
  { canton: "Zarcero", tHa: 23.8 },
  { canton: "Turrialba", tHa: 23.8 },
  { canton: "Naranjo", tHa: 23.6 },
  { canton: "El Guarco", tHa: 23.1 },
  { canton: "Oreamuno", tHa: 22.3 },
  { canton: "Dota", tHa: 21.5 },
];

const pptx = new PptxGenJS();
pptx.author = "Agriconsultor";
pptx.title = "Papa en Costa Rica — rendimiento por cantón";

// Portada
let s1 = pptx.addSlide();
s1.addText("Papa en Costa Rica", { x: 0.5, y: 1.6, w: 9, h: 1, fontSize: 36, bold: true });
s1.addText("Rendimiento por cantón — Agriconsultor", { x: 0.5, y: 2.6, w: 9, h: 0.6, fontSize: 18, color: "555555" });

// Gráfico de barras data-driven
let s2 = pptx.addSlide();
s2.addText("Rendimiento por cantón (t/ha)", { x: 0.5, y: 0.3, w: 9, h: 0.6, fontSize: 24, bold: true });
s2.addChart(pptx.ChartType.bar, [{
  name: "t/ha",
  labels: rendimientoPorCanton.map(r => r.canton),
  values: rendimientoPorCanton.map(r => r.tHa),
}], { x: 0.5, y: 1.0, w: 9, h: 4.2, showValue: true, barDir: "col" });
s2.addText(`Fuente: ${FUENTE}`, { x: 0.5, y: 5.3, w: 9, h: 0.4, fontSize: 10, italic: true, color: "777777" });

const outDir = path.join(__dirname, "..", "salidas");
fs.mkdirSync(outDir, { recursive: true });
const out = path.join(outDir, "presentacion-pptxgenjs.pptx");
pptx.writeFile({ fileName: out }).then(() => console.log("OK ->", out));
