// Wiederkehrende Bildmotive: die Formen des Netzes.
// Jedes Motiv zeichnet sich im Vollbild (1920×1080); g.mini() verkleinert es bei Bedarf.
import { FARBEN, klemme, mix, sanft, aus, zufall } from './zeichnen.js';

export const W = 1920, H = 1080, CX = 960, CY = 540;

// ---------- Layout-Hilfen (einmal berechnet, deterministisch) ----------

export function streuung(startwert, n, x0, y0, x1, y1, abstand = 60, filter = () => true) {
  const r = zufall(startwert);
  const pkt = [];
  for (let versuch = 0; pkt.length < n && versuch < n * 400; versuch++) {
    const p = [mix(x0, x1, r()), mix(y0, y1, r())];
    if (filter(p) && pkt.every((q) => Math.hypot(q[0] - p[0], q[1] - p[1]) > abstand)) pkt.push(p);
  }
  return pkt;
}

export function nachbarKanten(pkt, k = 2, maxD = 400) {
  const kanten = new Set();
  pkt.forEach((p, i) => {
    pkt.map((q, j) => [j, Math.hypot(q[0] - p[0], q[1] - p[1])])
      .filter(([j, d]) => j !== i && d < maxD)
      .sort((a, b) => a[1] - b[1])
      .slice(0, k)
      .forEach(([j]) => kanten.add(i < j ? `${i}-${j}` : `${j}-${i}`));
  });
  return [...kanten].map((s) => s.split('-').map(Number));
}

const hash = (a, b = 0) => {
  let h = (a * 374761393 + b * 668265263) >>> 0;
  h = ((h ^ (h >>> 13)) * 1274126177) >>> 0;
  return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
};

// ---------- Sendemast ----------

export function sendemast(g, x, boden, hoehe, p, t, o = {}) {
  const spitze = [x, boden - hoehe];
  const halb = hoehe * 0.2;
  const fuss = aus(klemme(p * 1.4));
  g.linie(x - halb, boden, spitze[0], spitze[1], fuss, { breite: 4 });
  g.linie(x + halb, boden, spitze[0], spitze[1], fuss, { breite: 4 });
  for (let k = 1; k <= 4; k++) {
    const q = k / 5;
    const y = mix(boden, spitze[1], q);
    const b = halb * (1 - q);
    const pk = klemme(p * 1.4 - 0.3 - k * 0.08);
    g.linie(x - b, y, x + b, y, pk, { breite: 2 });
    if (k < 4) {
      const y2 = mix(boden, spitze[1], (k + 1) / 5);
      const b2 = halb * (1 - (k + 1) / 5);
      g.linie(x - b, y, x + b2, y2, pk, { breite: 1.5, alpha: 0.7 });
    }
  }
  g.punkt(spitze[0], spitze[1], 9 * aus(klemme(p * 2 - 1)), { farbe: o.farbe ?? FARBEN.akzent });
  const wa = (o.wellen ?? 1) * klemme(p * 2 - 1);
  if (wa > 0) {
    g.wellen(spitze[0], spitze[1], t, {
      periode: 1.4, anzahl: 4, maxR: o.reichweite ?? 300, alpha: 0.55 * wa, breite: 2.5,
      boegen: [[-0.3 * Math.PI, 0.3 * Math.PI], [0.7 * Math.PI, 1.3 * Math.PI]],
    });
  }
}

// ---------- Netz, in dem jeder sendet ----------

const NETZ_PKT = streuung(5, 15, 1180, 260, 1720, 820, 110);
const NETZ_KANTEN = nachbarKanten(NETZ_PKT, 2, 260);

export function sendernetz(g, p, t, o = {}) {
  const dx = o.dx ?? 0, dy = o.dy ?? 0;
  NETZ_KANTEN.forEach(([a, b], i) => {
    const pk = klemme(p * 1.6 - 0.4 - (i / NETZ_KANTEN.length) * 0.4);
    g.linie(NETZ_PKT[a][0] + dx, NETZ_PKT[a][1] + dy, NETZ_PKT[b][0] + dx, NETZ_PKT[b][1] + dy, pk,
      { breite: 2, alpha: 0.55 });
  });
  NETZ_PKT.forEach(([x, y], i) => {
    const pp = aus(klemme(p * 2 - (i / NETZ_PKT.length)));
    g.punkt(x + dx, y + dy, 8 * pp);
    if (o.wellen) g.wellen(x + dx, y + dy, t, { periode: 1.6, anzahl: 2, maxR: 46, alpha: 0.45 * o.wellen * pp, versatz: hash(i) });
  });
}

// ---------- Stern: rpi-virtuell als Plattform ----------

export const STERN = { cx: CX, cy: CY + 20, R: 105, n: 16, aussen: 390 };

export function stern(g, o = {}) {
  const { cx, cy, R, n, aussen } = STERN;
  const alpha = o.alpha ?? 1;
  const kreisP = o.kreis ?? 1;
  g.kreis(cx, cy, R * (o.radius ?? 1), kreisP, { breite: 4, alpha });
  if (o.beschriftung && kreisP > 0.5) {
    g.text(o.beschriftung, cx, cy + 12, { groesse: 34 * (o.radius ?? 1), align: 'center', alpha: alpha * klemme(kreisP * 2 - 1) });
  }
  for (let i = 0; i < n; i++) {
    const a = -Math.PI / 2 + (i * 2 * Math.PI) / n;
    const ps = aus(klemme((o.speichen ?? 0) * 1.5 - (i / n) * 0.5));
    if (ps <= 0) continue;
    const x0 = cx + Math.cos(a) * (R + 14), y0 = cy + Math.sin(a) * (R + 14);
    const x1 = cx + Math.cos(a) * aussen, y1 = cy + Math.sin(a) * aussen;
    g.linie(x0, y0, x1, y1, ps, { breite: 2.2, alpha: alpha * 0.8 });
    g.punkt(x1, y1, 7 * klemme(ps * 3 - 2), { alpha });
    const pe = aus(klemme((o.etiketten ?? 0) * 1.5 - (i / n) * 0.5));
    if (pe > 0 && i % 2 === 0) { // nicht alles ist offen lizenziert: nur ein Teil trägt CC
      const ex = mix(x0, x1, 0.62), ey = mix(y0, y1, 0.62);
      g.rechteck(ex - 22, ey - 13, 44, 26, 6, 1, { breite: 1.8, alpha: alpha * pe, fuellung: FARBEN.papier });
      g.text('CC', ex, ey + 6, { groesse: 15, align: 'center', alpha: alpha * pe, gewicht: 700, farbe: FARBEN.akzent });
    }
    if (o.fluss) {
      for (let k = 0; k < 2; k++) {
        const ph = (o.fluss * 0.45 + hash(i, k)) % 1;
        g.punkt(mix(x0, x1, ph), mix(y0, y1, ph), 5, { alpha: alpha * Math.sin(ph * Math.PI), farbe: FARBEN.orange });
      }
    }
  }
}

// ---------- Pulsfeld: #relichat ohne Mitte ----------

const PULS_PKT = streuung(11, 44, 160, 170, 1760, 930, 105);
const PULS_KANTEN = nachbarKanten(PULS_PKT, 3, 330);
const GRUPPEN = [[620, 420], [1300, 400], [960, 770]];
const PULS_GRUPPE = PULS_PKT.map(([x, y]) => {
  let best = 0;
  GRUPPEN.forEach(([gx, gy], k) => {
    if (Math.hypot(gx - x, gy - y) < Math.hypot(GRUPPEN[best][0] - x, GRUPPEN[best][1] - y)) best = k;
  });
  return best;
});

export const PULS_PERIODE = 2.2;

export function pulsfeld(g, t, o = {}) {
  const sichtbar = o.sichtbar ?? 1;
  const grp = sanft(o.gruppiert ?? 0);
  const puls = o.puls ?? 1;
  const nr = Math.floor(t / PULS_PERIODE);
  const ph = (t % PULS_PERIODE) / PULS_PERIODE;
  const hell = Math.exp(-ph * 5) * puls;
  const pos = PULS_PKT.map(([x, y], i) => {
    const [gx, gy] = GRUPPEN[PULS_GRUPPE[i]];
    return [mix(x, gx + (x - gx) * 0.3, grp), mix(y, gy + (y - gy) * 0.3, grp)];
  });
  PULS_KANTEN.forEach(([a, b], i) => {
    const gleich = PULS_GRUPPE[a] === PULS_GRUPPE[b];
    const flacker = hash(nr, i) < 0.45 ? hell : 0;
    const fest = gleich ? grp : 0;
    const al = Math.max(flacker * 0.7, fest * 0.75) * sichtbar * (o.kantenAlpha ?? 1);
    if (al > 0.01) {
      g.linie(...pos[a], ...pos[b], 1, { breite: mix(1.5, 3.5, fest), alpha: al });
    }
  });
  pos.forEach(([x, y], i) => {
    const erschein = aus(klemme((o.erscheinen ?? 1) * 1.6 - hash(i, 99) * 0.6));
    const a = sichtbar * erschein * (0.55 + 0.45 * hell);
    g.punkt(x, y, (6 + 3 * hell) * erschein, { alpha: a });
    if (o.wellen) g.wellen(x, y, t, { periode: 1.7, anzahl: 2, maxR: 40, alpha: 0.4 * o.wellen * erschein, versatz: hash(i, 3) });
  });
}

// ---------- Labor: dichtes Netz in lockerem Umriss ----------

const LAB = { cx: CX, cy: CY + 20, rx: 470, ry: 300 };
const imLab = ([x, y]) => ((x - LAB.cx) / (LAB.rx - 40)) ** 2 + ((y - LAB.cy) / (LAB.ry - 40)) ** 2 < 1;
export const LAB_PKT = streuung(23, 70, LAB.cx - LAB.rx, LAB.cy - LAB.ry, LAB.cx + LAB.rx, LAB.cy + LAB.ry, 52, imLab);
const LAB_KANTEN = nachbarKanten(LAB_PKT, 3, 170);
export const LAB_UMRISS = (() => {
  const r = zufall(31);
  const pkt = [];
  for (let k = 0; k <= 64; k++) {
    const a = (k / 64) * Math.PI * 2 - Math.PI / 2;
    const s = 1 + (r() - 0.5) * 0.05;
    pkt.push([LAB.cx + Math.cos(a) * LAB.rx * s, LAB.cy + Math.sin(a) * LAB.ry * s]);
  }
  pkt[64] = pkt[0];
  return pkt;
})();
export { LAB };

export function labor(g, t, o = {}) {
  const p = o.p ?? 1;
  const alpha = o.alpha ?? 1;
  g.pfad(LAB_UMRISS, o.umriss ?? 1, { breite: 3, alpha: alpha * 0.8, farbe: o.umrissFarbe ?? FARBEN.tinte });
  LAB_KANTEN.forEach(([a, b], i) => {
    const pk = klemme(p * 1.5 - hash(i, 5) * 0.5);
    g.linie(...LAB_PKT[a], ...LAB_PKT[b], pk, { breite: 1.8, alpha: alpha * 0.55 });
  });
  LAB_PKT.forEach(([x, y], i) => {
    const pp = aus(klemme(p * 1.6 - hash(i, 7) * 0.6));
    const puls = 0.5 + 0.5 * Math.sin(t * 1.3 + i);
    g.punkt(x, y, (5 + 1.5 * puls) * pp, { alpha: alpha * (o.punktAlpha ? o.punktAlpha(i) : 1) });
  });
}

// ---------- Inseln: zersplitterte Community ----------

export const INSELN = [
  { name: 'Instagram', cx: 500, cy: 360 },
  { name: 'Newsletter', cx: 1420, cy: 340 },
  { name: 'Chat', cx: 560, cy: 790 },
  { name: 'Webseite', cx: 1380, cy: 790 },
].map((ins, k) => {
  const r = zufall(50 + k);
  const umriss = [];
  for (let j = 0; j <= 40; j++) {
    const a = (j / 40) * Math.PI * 2;
    const s = 1 + Math.sin(a * 3 + k) * 0.06 + (r() - 0.5) * 0.04;
    umriss.push([ins.cx + Math.cos(a) * 200 * s, ins.cy + Math.sin(a) * 140 * s]);
  }
  umriss[40] = umriss[0];
  const pkt = streuung(60 + k, 9, ins.cx - 150, ins.cy - 95, ins.cx + 150, ins.cy + 95, 55);
  return { ...ins, umriss, pkt, kanten: nachbarKanten(pkt, 2, 150) };
});

export function inseln(g, t, o = {}) {
  INSELN.forEach((ins, k) => {
    const p = aus(klemme((o.p ?? 1) * 1.5 - k * 0.15));
    const a = (o.alpha ?? 1) * p;
    if (a <= 0) return;
    g.pfad(ins.umriss, p, { breite: 2.5, alpha: a * 0.7, farbe: FARBEN.leise });
    ins.kanten.forEach(([i, j]) => g.linie(...ins.pkt[i], ...ins.pkt[j], 1, { breite: 1.6, alpha: a * 0.5 }));
    ins.pkt.forEach(([x, y], i) => {
      const verblassen = o.verblassen ? klemme(1 - o.verblassen * 1.6 + hash(k, i) * 0.6) : 1;
      g.punkt(x, y, 6, { alpha: a * (0.2 + 0.8 * verblassen) });
    });
    if (o.namen !== false) {
      g.text(ins.name, ins.cx, ins.cy - 170, { groesse: 30, align: 'center', alpha: a * (o.namenP ? o.namenP[k] : 1), farbe: FARBEN.leise });
    }
  });
}

// ---------- Protokoll: Schlüssel und Verbindungen ohne Mitte ----------

export function schluessel(g, x, y, s = 1, o = {}) {
  g.kreis(x, y, 9 * s, 1, { breite: 2.5, alpha: o.alpha ?? 1, farbe: o.farbe ?? FARBEN.akzent });
  g.linie(x + 9 * s, y, x + 34 * s, y, 1, { breite: 2.5, alpha: o.alpha ?? 1, farbe: o.farbe ?? FARBEN.akzent });
  g.linie(x + 26 * s, y, x + 26 * s, y + 8 * s, 1, { breite: 2.5, alpha: o.alpha ?? 1, farbe: o.farbe ?? FARBEN.akzent });
  g.linie(x + 33 * s, y, x + 33 * s, y + 6 * s, 1, { breite: 2.5, alpha: o.alpha ?? 1, farbe: o.farbe ?? FARBEN.akzent });
}

export const PROTO_PKT = streuung(77, 22, 220, 220, 1700, 900, 190);
const PROTO_KANTEN = nachbarKanten(PROTO_PKT, 3, 420);

export function protokollnetz(g, t, o = {}) {
  const p = o.p ?? 1;
  // o.umzug = { i, x, y, q }: Knoten i zieht mit Fortschritt q an einen neuen Ort
  const pos = PROTO_PKT.map((pt, i) =>
    o.umzug && o.umzug.i === i ? [mix(pt[0], o.umzug.x, sanft(o.umzug.q)), mix(pt[1], o.umzug.y, sanft(o.umzug.q))] : pt);
  PROTO_KANTEN.forEach(([a, b], i) => {
    const pk = klemme((o.kanten ?? p) * 1.5 - hash(i, 9) * 0.5);
    const umz = o.umzug && (o.umzug.i === a || o.umzug.i === b);
    const al = umz ? Math.abs(1 - 2 * sanft(o.umzug.q)) : 1; // reißt beim Umzug kurz ab und verbindet neu
    g.linie(...pos[a], ...pos[b], pk, { breite: 2, alpha: 0.5 * al * (o.alpha ?? 1) });
  });
  pos.forEach(([x, y], i) => {
    const pp = aus(klemme(p * 1.6 - hash(i, 4) * 0.6));
    g.punkt(x, y, 8 * pp, { alpha: o.alpha ?? 1 });
    const ps = aus(klemme((o.schluessel ?? 0) * 1.6 - hash(i, 6) * 0.6));
    if (ps > 0) schluessel(g, x + 14, y - 20, 0.8, { alpha: ps * (o.alpha ?? 1) });
  });
}

// ---------- Kreise des Vertrauens: Communities, die auswählen ----------

export const KREISE = [
  { cx: 520, cy: 400, r: 150 }, { cx: 1000, cy: 300, r: 120 }, { cx: 1420, cy: 430, r: 160 },
  { cx: 760, cy: 760, r: 135 }, { cx: 1260, cy: 780, r: 125 },
];
const KREIS_KANTEN = [[0, 1], [1, 2], [0, 3], [3, 4], [2, 4], [1, 3]];

export function material(g, x, y, s = 1, o = {}) {
  const a = o.alpha ?? 1;
  if (a <= 0) return;
  g.rechteck(x - 22 * s, y - 28 * s, 44 * s, 56 * s, 5 * s, 1, { breite: 2, alpha: a, fuellung: FARBEN.papier, farbe: o.farbe });
  for (let k = 0; k < 3; k++) {
    g.linie(x - 13 * s, y - 14 * s + k * 12 * s, x + (k === 2 ? 4 : 13) * s, y - 14 * s + k * 12 * s, 1,
      { breite: 1.5, alpha: a * 0.6 });
  }
}

export function kreise(g, t, o = {}) {
  const p = o.p ?? 1;
  KREIS_KANTEN.forEach(([a, b], i) => {
    const A = KREISE[a], B = KREISE[b];
    const d = Math.hypot(B.cx - A.cx, B.cy - A.cy);
    const ux = (B.cx - A.cx) / d, uy = (B.cy - A.cy) / d;
    g.linie(A.cx + ux * A.r, A.cy + uy * A.r, B.cx - ux * B.r, B.cy - uy * B.r,
      klemme((o.verbindungen ?? p) * 1.4 - i * 0.08), { breite: 2, alpha: 0.5, strich: [8, 10] });
  });
  KREISE.forEach((k, i) => {
    const pk = aus(klemme(p * 1.5 - i * 0.12));
    g.kreis(k.cx, k.cy, k.r, pk, { breite: 3, farbe: FARBEN.akzent, alpha: 0.85 });
    // Materialien wandern in den Kreis hinein
    const pm = klemme((o.material ?? 0) * 1.3 - i * 0.06);
    for (let m = 0; m < 3; m++) {
      const a = hash(i, m) * Math.PI * 2;
      const von = [k.cx + Math.cos(a) * (k.r + 120), k.cy + Math.sin(a) * (k.r + 90)];
      const zu = [k.cx + (m - 1) * 52, k.cy + 10];
      const q = sanft(klemme(pm * 1.6 - m * 0.25));
      material(g, mix(von[0], zu[0], q), mix(von[1], zu[1], q), 0.75, { alpha: klemme(pm * 4 - m) });
    }
  });
}

// ---------- Vollständige Motive für Übersichten ----------

export const MOTIVE = {
  Sendemast: (g, t) => sendemast(g, CX, 900, 620, 1, t, { reichweite: 520 }),
  Stern: (g) => stern(g, { speichen: 1, beschriftung: 'rpi-virtuell' }),
  Puls: (g, t) => pulsfeld(g, t, { puls: 0.3 }),
  Gruppen: (g, t) => pulsfeld(g, t, { gruppiert: 1, puls: 0.3 }),
  Labor: (g, t) => labor(g, t),
  Inseln: (g, t) => inseln(g, t, { namen: false }),
  Protokoll: (g, t) => protokollnetz(g, t, { schluessel: 1 }),
  Kreise: (g, t) => kreise(g, t, { material: 1 }),
};
