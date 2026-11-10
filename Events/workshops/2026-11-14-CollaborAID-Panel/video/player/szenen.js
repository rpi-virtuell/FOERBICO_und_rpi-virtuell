// Szenen je Sinneinheit. Eine Szene ist eine Funktion (g, z, o):
//   g  – Zeichenwerkzeuge (zeichnen.js)
//   z  – Zeit: z.lt (Sekunden seit Beginn der Einheit), z.dauer, z.p (0..1), z.t (global),
//        z.ab(sek, dauer) und z.abWort('wort', dauer, versatz) liefern Fortschritt 0..1,
//        z.wort('wort') die lokale Sprechzeit, z.e die Einheit aus timeline.json
//   o  – Optionen: o.regie (Regiehinweise zeigen), o.szenen (Szenentitel)
// Einheiten ohne eigene Szene zeigen die Standardszene.
import { FARBEN, aus, sanft, mix, klemme, zufall } from './zeichnen.js';
import {
  W, H, CX, CY, STERN, LAB, sendemast, sendernetz, stern, pulsfeld, PULS_PERIODE, labor, inseln,
  INSELN, protokollnetz, PROTO_PKT, schluessel, kreise, KREISE, material, MOTIVE,
} from './motive.js';

// ---------- Bausteine ----------

// Kurzformen der Lektionen für die mitlaufende Leiste (player.js)
export const LEKTIONEN = {
  E09: 'Plattform', E14: 'Rhythmus', E17: 'Begegnung', E24: 'ohne Spitze',
  E28: 'eigener Raum', E34: 'Standards', E38: 'Sichtbarkeit',
};

function lernsatzText(g, z, y = H / 2) {
  const e = z.e;
  const groesse = 76, breite = 1600;
  const zeilen = g.umbruch(e.lernsatz, breite, groesse).length;
  const oben = y - ((zeilen - 1) * groesse * 1.35) / 2 - groesse - 30;
  const nr = Object.keys(LEKTIONEN).indexOf(e.id) + 1;
  if (nr) g.text(`Lektion ${nr} von ${Object.keys(LEKTIONEN).length}`, W / 2, oben - 28,
    { groesse: 28, align: 'center', farbe: FARBEN.akzent, alpha: z.ab(0, 0.8) });
  g.linie(W / 2 - 60, oben, W / 2 + 60, oben, sanft(z.ab(0.2, 0.8)), { farbe: FARBEN.orange, breite: 5 });
  g.absatz(e.lernsatz, W / 2, y, { groesse, p: z.ab(0.5, 2.2), breite });
}

// Lernsatz mit kleinem Motiv darüber
const mitMotiv = (motiv, s = 0.42) => (g, z) => {
  g.mit(aus(z.ab(0, 1.2)), () => g.mini(W / 2, 300, s, () => motiv(g, z)));
  lernsatzText(g, z, 760);
};

function kasten(g, text, x, y, p, o = {}) {
  if (p <= 0) return;
  const groesse = o.groesse ?? 34;
  const b = g.breite(text, groesse, o) + 44;
  g.mit(aus(p), () => {
    g.rechteck(x - b / 2, y - groesse * 0.95, b, groesse * 1.45, 10, 1,
      { breite: 2, farbe: o.rahmen ?? FARBEN.leise, fuellung: FARBEN.papier, fuellAlpha: 0.93 });
    g.text(text, x, y + groesse * 0.1, { groesse, align: 'center', farbe: o.farbe ?? FARBEN.tinte, gewicht: o.gewicht });
  });
}

const formatZahl = (n) => Math.round(n).toLocaleString('de-DE');

// Puls nur für zwei Schläge ab lokaler Zeit `ab`, danach ruhig (blinkt sonst zu sehr)
const zweiSchlaege = (z, ab) => (z.lt < ab ? 0 : klemme(1 - (z.lt - ab - 2 * PULS_PERIODE) / 0.8));

export function standardSzene(g, z, o) {
  const e = z.e;
  if (e.lernsatz) return lernsatzText(g, z);
  if (o.regie) g.absatz(e.bild, W / 2, H / 2, { groesse: 38, kursiv: true, farbe: FARBEN.leise, breite: 1400 });
}

// ---------- Szene 0 · Die Frage ----------

function E01(g, z) {
  g.kreis(CX, CY, 10, aus(z.ab(0.4, 1.2)), { breite: 3 });
  g.punkt(CX, CY, 10 * aus(z.ab(1.2, 0.6)));
}

function E02(g, z) {
  g.punkt(CX, CY, 10);
  const r = zufall(42);
  const namen = ['Institut', 'Landeskirche', 'Bistum', 'Hochschule', 'Schule', 'Ehrenamt'];
  const zeiten = ['institute', 'landeskirchen', 'bistümer', 'hochschulen', 'schulen', 'ehrenamtliche'].map((w) => z.wort(w));
  for (let i = 0; i < 36; i++) {
    const winkel = r() * Math.PI * 2;
    const abstand = 160 + r() * 380;
    const x = CX + Math.cos(winkel) * abstand * 1.5;
    const y = CY + Math.sin(winkel) * abstand * 0.85;
    const q = aus(z.ab(zeiten[i % 6] + r() * 0.4, 0.5));
    g.punkt(x, y, (5 + r() * 4) * q, { alpha: q });
    if (i < 6) g.text(namen[i], x, y - 22, { groesse: 30, farbe: FARBEN.leise, align: 'center', alpha: q });
  }
  // „eigene Leitung, eigenes Budget, eigene Logik“: jeder Punkt bekommt einen Ring
  const ringe = z.abWort('Leitung', 2.5);
  const r2 = zufall(42);
  for (let i = 0; i < 36; i++) {
    const winkel = r2() * Math.PI * 2, abstand = 160 + r2() * 380;
    r2(); r2();
    g.kreis(CX + Math.cos(winkel) * abstand * 1.5, CY + Math.sin(winkel) * abstand * 0.85, 18,
      klemme(ringe * 1.5 - (i / 36) * 0.5), { breite: 1.5, alpha: 0.45, farbe: FARBEN.leise });
  }
}

function E03(g, z) {
  g.linie(CX, 200, CX, 900, aus(z.ab(0.2, 1.4)), { breite: 1.5, alpha: 0.25, farbe: FARBEN.leise });
  const pm = z.abWort('Rundfunk', 2.2, -0.4);
  g.mini(560, 540, 0.85, () => sendemast(g, CX, 960, 620, pm, z.t, { wellen: z.abWort('ausgestrahlt', 1.2), reichweite: 360 }));
  g.text('Rundfunk', 560, 960, { groesse: 36, align: 'center', alpha: aus(pm), farbe: FARBEN.leise });
  const pn = z.abWort('Netz', 2.2, -0.3);
  sendernetz(g, pn, z.t, { dx: -40, wellen: z.abWort('senden', 1.2) });
  g.text('Netz', 1410, 960, { groesse: 36, align: 'center', alpha: aus(pn), farbe: FARBEN.leise });
}

function E04(g, z) {
  const frage = 'Wer hat hier das Sagen?';
  const b = g.breite(frage, 78);
  g.schreiben(frage, CX, 440, z.ab(0.2, 1.8), { groesse: 78, align: 'center' });
  g.linie(CX - b / 2 - 20, 415, CX + b / 2 + 20, 412, sanft(z.abWort('Organigramm', 0.7)), { farbe: FARBEN.akzent, breite: 5 });
  g.schreiben('Was hält uns zusammen?', CX, 640, z.abWort('sondern', 1.8, -0.1), { groesse: 78, align: 'center' });
}

// ---------- Szene 1 · rpi-virtuell: die Plattform ----------

function E05(g, z) {
  const kreisP = aus(z.ab(0.3, 1.4));
  stern(g, { kreis: kreisP, beschriftung: 'rpi-virtuell', speichen: z.abWort('finden', 3, -0.3) });
  g.text('2002', STERN.cx, STERN.cy + 52, { groesse: 30, align: 'center', farbe: FARBEN.leise, alpha: z.abWort('2002', 0.8) });
  const rein = z.abWort('Vorläufer', 0.9) * (1 - z.abWort('finden', 1.2, -0.6));
  g.mit(rein, () => {
    const x = STERN.cx - 520, y = STERN.cy;
    g.kreis(x, y, 52, aus(z.abWort('Vorläufer', 1)), { breite: 3 });
    g.text('reliweb.de', x, y + 8, { groesse: 22, align: 'center' });
    g.text('1999', x, y + 90, { groesse: 30, align: 'center', farbe: FARBEN.leise, alpha: z.abWort('1999', 0.8) });
    g.linie(x + 62, y, STERN.cx - STERN.R - 16, y, sanft(z.abWort('1999', 1.2)), { breite: 2, strich: [10, 10], farbe: FARBEN.leise });
  });
  kasten(g, 'über 25 Jahre', 1600, 220, z.abWort('fünfundzwanzig', 0.8), { groesse: 34 });
}

function E06(g, z) {
  stern(g, { beschriftung: 'rpi-virtuell', speichen: 1, etiketten: z.abWort('Lizenzen', 2.8, -0.2) });
  kasten(g, 'offene Lizenzen seit 2011', 1580, 200, z.abWort('2011', 0.8), { groesse: 30 });
  g.kreis(STERN.cx, STERN.cy, STERN.R + 30, sanft(z.abWort('Pionieren', 1.4)), { breite: 4, farbe: FARBEN.akzent });
  kasten(g, 'OER-Pionier', STERN.cx, STERN.cy + STERN.aussen + 70, z.abWort('Pionieren', 0.8, 0.6), { groesse: 30, rahmen: FARBEN.akzent });
}

const BALKEN = { x: 460, y: 600, b: 1000, h: 80 };

function befragungsBalken(g, p29, p70, alpha = 1) {
  const { x, y, b, h } = BALKEN;
  g.mit(alpha, () => {
    g.rechteck(x, y, b, h, 8, 1, { breite: 2.5 });
    if (p29 > 0) {
      g.rechteck(x + 6, y + 6, (b * 0.29 - 12) * sanft(p29), h - 12, 5, 1,
        { breite: 0.1, farbe: FARBEN.akzent, fuellung: FARBEN.akzent, fuellAlpha: 0.9 });
      g.text('29 % selbst eingestellt', x, y - 26, { groesse: 30, alpha: p29, farbe: FARBEN.akzent });
    }
    if (p70 > 0) {
      const x0 = x + b * 0.30;
      g.rechteck(x0, y + 6, (b * 0.70 - 6) * sanft(p70), h - 12, 5, 1,
        { breite: 0.1, farbe: FARBEN.hell, fuellung: FARBEN.hell, fuellAlpha: 0.9 });
      g.text('70 % noch nie', x + b, y - 26, { groesse: 30, alpha: p70, align: 'right', farbe: FARBEN.leise });
    }
  });
}

function E07(g, z) {
  g.mit(0.15, () => stern(g, { speichen: 1 }));
  const zahl = sanft(z.abWort('fünfzehnhundert', 1.6, -0.3));
  if (zahl > 0) {
    g.text(formatZahl(1462 * zahl), CX, 380, { groesse: 130, align: 'center' });
    g.text('Befragte, 2013', CX, 440, { groesse: 30, align: 'center', farbe: FARBEN.leise, alpha: zahl });
  }
  befragungsBalken(g, z.abWort('dreißig', 1), z.abWort('siebzig', 1));
}

function E08(g, z) {
  g.mit(0.15, () => stern(g, { speichen: 1 }));
  g.schreiben('Warum nicht?', CX, 360, z.ab(0, 1.0), { groesse: 72, align: 'center', kursiv: true });
  befragungsBalken(g, 1, 1);
  ['Knowhow', 'Zeit', 'Gelegenheit'].forEach((w, k) => {
    const q = z.abWort(w, 1.1, 0);
    if (q <= 0) return;
    const x = BALKEN.x + BALKEN.b * (0.45 + k * 0.2);
    const y = mix(BALKEN.y + 50, 820 + (k % 2) * 40, aus(q));
    g.ctx.save();
    g.ctx.translate(x, y);
    g.ctx.rotate((k - 1) * 0.08 * aus(q));
    g.text(w, 0, 0, { groesse: 44, align: 'center', alpha: klemme(q * 3), farbe: FARBEN.leise });
    g.ctx.restore();
  });
}

const E09 = (g, z) => {
  const m = z.abWort('Sender', 0.7) * (1 - z.abWort('empfangen', 0.9, 0.5));
  g.mit(aus(z.ab(0, 1.2)), () => g.mini(W / 2, 300, 0.42, () => {
    g.mit(1 - 0.85 * m, () => stern(g, { speichen: 1, beschriftung: 'rpi-virtuell', fluss: z.t }));
    g.mit(m, () => sendemast(g, CX, 980, 760, 1, z.t, { reichweite: 520 }));
  }));
  lernsatzText(g, z, 760);
};

function E10(g, z) {
  const q = sanft(z.ab(0.3, 1.8));
  const sx = mix(STERN.cx, 560, q), s = mix(1, 0.7, q);
  g.mini(sx, CY + mix(0, 20 * 0.7, q), s, () => stern(g, { speichen: 1, beschriftung: 'rpi-virtuell' }));
  const ziele = [
    { name: 'OERcamp', unter: 'seit 2012', x: 1380, y: 360, r: 120, wort: 'OERcamp' },
    { name: 'Open-Reli', unter: '2013 · mit einer Hochschule in Österreich', x: 1460, y: 760, r: 110, wort: 'Open-Reli' },
  ];
  ziele.forEach((k, j) => {
    const pk = z.abWort(k.wort, 1.4, -0.4);
    g.kreis(k.x, k.y, k.r, aus(pk), { breite: 3, strich: [14, 10] });
    g.text(k.name, k.x, k.y + 10, { groesse: 34, align: 'center', alpha: pk });
    g.text(k.unter, k.x, k.y + k.r + 44, { groesse: 30, align: 'center', alpha: pk, farbe: FARBEN.leise });
    for (let i = 0; i < 4; i++) {
      const a = (-0.5 + j) * 0.9 + (i - 1.5) * 0.18;
      const von = [sx + Math.cos(a) * STERN.aussen * s, CY + 14 + Math.sin(a) * STERN.aussen * s];
      const zu = [k.x + (i - 1.5) * 34, k.y + 50 + (i % 2) * 18];
      const w = sanft(z.abWort(k.wort, 2.0, -0.2 + i * 0.25));
      if (w > 0) g.punkt(mix(von[0], zu[0], w), mix(von[1], zu[1], w), 8, { farbe: FARBEN.orange });
    }
  });
}

// ---------- Szene 2 · #relichat: der Puls ----------

function E11(g, z) {
  const q = sanft(z.abWort('Karl', 1.4, -0.3));
  pulsfeld(g, z.t, { erscheinen: z.abWort('relichat', 2.5, 0.3), puls: zweiSchlaege(z, z.wort('relichat') + 0.8) });
  const y = mix(560, 170, q), gr = mix(170, 70, q);
  g.mit(1, () => {
    if (q > 0.05) g.rechteck(CX - 230 * mix(1.6, 1, q), y - gr * 0.85, 460 * mix(1.6, 1, q), gr * 1.15, 14, 1, { breite: 0.1, farbe: FARBEN.papier, fuellung: FARBEN.papier, fuellAlpha: 0.9 * q });
    g.schreiben('#relichat', CX, y, z.abWort('relichat', 1.4, -0.3), { groesse: gr, align: 'center' });
  });
  g.text('2017', CX, y + 50, { groesse: 30, align: 'center', farbe: FARBEN.leise, alpha: z.abWort('2017', 0.8) * (1 - q) });
  kasten(g, 'initiiert von Karl Peböck', CX, 980, z.abWort('Karl', 0.8, 0.3), { groesse: 30 });
}

function relichatKopf(g) {
  g.rechteck(CX - 230, 110, 460, 82, 14, 1, { breite: 0.1, farbe: FARBEN.papier, fuellung: FARBEN.papier, fuellAlpha: 0.9 });
  g.text('#relichat', CX, 170, { groesse: 70, align: 'center' });
}

function E12(g, z) {
  pulsfeld(g, z.t, { puls: zweiSchlaege(z, z.wort('Mittwoch') - 0.2) });
  relichatKopf(g);
  kasten(g, 'Mittwoch · 20 Uhr', CX, 270, z.abWort('Mittwoch', 0.8), { groesse: 40, rahmen: FARBEN.akzent });
  const n150 = sanft(z.abWort('hundertfünfzig', 1.4, -0.2));
  kasten(g, `${formatZahl(150 * n150)}+ Abende`, 560, 990, n150 ? 1 : 0, { groesse: 36 });
  const nT = sanft(z.abWort('Million', 1.6, -0.3));
  kasten(g, `${formatZahl(500000 * nT)} Tweets`, 1360, 990, nT ? 1 : 0, { groesse: 36 });
}

function E13(g, z) {
  const wellen = z.abWort('Sender', 1.2, -0.2) * mix(1, 0.35, z.abWort('Sender', 1.5, 3));
  pulsfeld(g, z.t, { wellen, puls: 0 });
  relichatKopf(g);
  kasten(g, 'ohne Anmeldung', 560, 990, z.abWort('anmelden', 0.8), { groesse: 32 });
  kasten(g, 'ohne einladende Institution', 1360, 990, z.abWort('Institution', 0.8), { groesse: 32 });
  kasten(g, 'Sender und Empfänger zugleich', CX, 270, z.abWort('Empfänger', 0.8), { groesse: 36, rahmen: FARBEN.akzent });
}

const E14 = mitMotiv((g, z) => pulsfeld(g, z.t, { puls: zweiSchlaege(z, 0.6) }));

// ---------- Szene 3 · relicamps: die Begegnung ----------

function E15(g, z) {
  const grp = z.abWort('Begegnungen', 2.8, -0.2, 2);
  pulsfeld(g, z.t, { gruppiert: grp, puls: 0 });
  kasten(g, '2019 · Saarbrücken', CX, 160, z.abWort('Saarbrücken', 0.8), { groesse: 40, rahmen: FARBEN.akzent });
  kasten(g, 'rund 40 Menschen · DE · AT · CH', CX, 250, z.abWort('vierzig', 0.8), { groesse: 30 });
  kasten(g, 'geplant auf Twitter, ehrenamtlich', CX, 990, z.abWort('Twitter', 0.8), { groesse: 30 });
}

const ORTE = [
  { name: 'Saarbrücken', jahr: '2019', x: 1150, y: 700, wort: null },
  { name: 'Salzburg', jahr: '2021 · hybrid', x: 1700, y: 840, wort: 'Salzburg' },
  { name: 'Hildesheim', jahr: '2022 · hybrid', x: 1480, y: 300, wort: 'Hildesheim' },
];

function E16(g, z) {
  // Sessionwand
  const x0 = 170, y0 = 240, sp = 4, ze = 3, bw = 170, bh = 150, abst = 14;
  g.rechteck(x0 - 20, y0 - 60, sp * (bw + abst) + 26, ze * (bh + abst) + 80, 10, aus(z.ab(0.1, 1.2)), { breite: 2.5 });
  g.text('Sessions', x0, y0 - 18, { groesse: 28, farbe: FARBEN.leise, alpha: z.ab(0.5, 0.8) });
  const karten = z.abWort('schlagen', 4.5, -0.3);
  for (let i = 0; i < sp * ze; i++) {
    const q = aus(klemme(karten * sp * ze * 0.6 - i * 0.6));
    if (q <= 0) continue;
    const x = x0 + (i % sp) * (bw + abst), y = y0 + Math.floor(i / sp) * (bh + abst);
    g.mit(q, () => {
      g.rechteck(x, y + (1 - q) * -30, bw, bh, 6, 1, { breite: 2, fuellung: i % 3 === 0 ? '#efe2c8' : FARBEN.papier });
      for (let k = 0; k < 3; k++) g.linie(x + 20, y + 40 + k * 28, x + bw - (k === 2 ? 70 : 20), y + 40 + k * 28, 1, { breite: 2, alpha: 0.5 });
    });
  }
  // Orte
  ORTE.forEach((o, i) => {
    const q = o.wort ? z.abWort(o.wort, 1) : aus(z.ab(0.3, 1));
    if (i > 0) {
      const v = ORTE[i - 1];
      g.linie(v.x, v.y, o.x, o.y, sanft(q), { breite: 2, strich: [10, 10], farbe: FARBEN.leise });
    }
    g.kreis(o.x, o.y, 22, aus(q), { breite: 3, farbe: FARBEN.akzent });
    g.punkt(o.x, o.y, 8 * q, { farbe: FARBEN.akzent });
    g.text(o.name, o.x, o.y - 40, { groesse: 32, align: 'center', alpha: q });
    g.text(o.jahr, o.x, o.y + 58, { groesse: 30, align: 'center', alpha: q, farbe: FARBEN.leise });
  });
  kasten(g, '+ Camps online', 1420, 560, z.abWort('online', 0.8), { groesse: 28 });
}

const E17 = mitMotiv((g, z) => {
  const q = sanft(z.ab(0.8, 2.2));
  const xa = mix(500, 860, q), xb = mix(1420, 1060, q);
  g.punkt(xa, CY, 22);
  g.punkt(xb, CY, 22);
  const l = z.abWort('gegenübergesessen', 1.2);
  g.linie(xa + 30, CY, xb - 30, CY, l, { breite: 6 });
  const v = z.abWort('Vereinbarungen', 1.4);
  g.linie(xa + 30, CY - 30, xb - 30, CY - 30, v, { breite: 6, farbe: FARBEN.akzent });
  g.linie(xa + 30, CY + 30, xb - 30, CY + 30, v, { breite: 6, farbe: FARBEN.akzent });
});

// ---------- Szene 4 · relilab: das Labor ----------

function E18(g, z) {
  const ueber = z.abWort('Community', 2.2, -0.4);
  g.mit(1 - ueber, () => pulsfeld(g, z.t, { gruppiert: 1, puls: 0 }));
  labor(g, z.t, { p: ueber, umriss: z.abWort('relilab', 1.4, -0.4) });
  kasten(g, '2020 · Pandemie', CX, 150, z.abWort('2020', 0.8), { groesse: 40, rahmen: FARBEN.akzent });
  g.schreiben('relilab', CX, LAB.cy + LAB.ry + 80, z.abWort('relilab', 1.2, -0.2), { groesse: 56, align: 'center' });
}

const MERKMALE = [
  { w: 'offen', x: 420, y: 230 }, { w: 'kostenfrei', x: 1500, y: 230 },
  { w: 'online', x: 420, y: 880 }, { w: 'ohne Anmeldung', x: 1500, y: 880, wort: 'Anmeldung' },
];

function E19(g, z) {
  labor(g, z.t);
  g.text('relilab', CX, LAB.cy + LAB.ry + 80, { groesse: 56, align: 'center' });
  MERKMALE.forEach((m) => kasten(g, m.w, m.x, m.y, z.abWort(m.wort ?? m.w, 0.7), { groesse: 40 }));
  const ring = z.abWort('Bundesländern', 2.4, -0.3);
  g.kreis(LAB.cx, LAB.cy, 560, ring, { breite: 2, strich: [6, 12], farbe: FARBEN.akzent, alpha: 0.7 });
  kasten(g, 'Menschen aus verschiedenen Bundesländern und Religionen', CX, 1010, z.abWort('Religionen', 0.8), { groesse: 30 });
}

// Verzweigung „Weiterdenken“
const AESTE = (() => {
  const r = zufall(91);
  const aeste = [];
  const wachse = (x, y, winkel, laenge, tiefe, start) => {
    const x2 = x + Math.cos(winkel) * laenge, y2 = y + Math.sin(winkel) * laenge;
    aeste.push({ x, y, x2, y2, tiefe, start });
    if (tiefe < 4) {
      const n = tiefe === 0 ? 3 : 2;
      for (let k = 0; k < n; k++) {
        const w = winkel + (k - (n - 1) / 2) * (0.75 - tiefe * 0.08) + (r() - 0.5) * 0.25;
        wachse(x2, y2, w, laenge * (0.72 + r() * 0.12), tiefe + 1, start + 1);
      }
    }
  };
  wachse(620, 560, 0, 300, 0, 0);
  return aeste;
})();

function E20(g, z) {
  g.mit(0.12, () => labor(g, z.t));
  const pi = z.abWort('Impuls', 0.8);
  g.linie(380, 560, 600, 560, pi, { breite: 7, farbe: FARBEN.akzent });
  g.text('Impuls', 490, 520, { groesse: 34, align: 'center', alpha: pi });
  const pw = z.abWort('Weiterdenken', 3.5, -0.4);
  const unfertig = z.abWort('Unfertiges', 1.2);
  for (const a of AESTE) {
    const q = klemme(pw * 5 - a.start);
    const blatt = a.tiefe === 4;
    g.linie(a.x, a.y, a.x2, a.y2, q, {
      breite: Math.max(1.5, 5 - a.tiefe), alpha: 0.85,
      strich: blatt && unfertig > 0 ? [6, 10] : undefined, farbe: blatt && unfertig > 0 ? FARBEN.akzent : FARBEN.tinte,
    });
  }
  g.text('Weiterdenken', 1200, 920, { groesse: 34, align: 'center', alpha: pw });
  const vortrag = z.abWort('Vortrag', 0.8);
  g.text('60 Minuten Vortrag + 3 Fragen', CX, 180, { groesse: 34, align: 'center', alpha: vortrag * 0.8, farbe: FARBEN.leise });
  g.linie(CX - 260, 170, CX + 260, 168, z.abWort('Ende', 0.6), { farbe: FARBEN.akzent, breite: 4 });
  kasten(g, 'Unfertiges erwünscht', 1500, 1000, unfertig, { groesse: 28, rahmen: FARBEN.akzent });
}

function E21(g, z) {
  labor(g, z.t);
  const r = zufall(17);
  const raus = z.abWort('geteilt', 3, -1.4);
  for (let i = 0; i < 9; i++) {
    const a = (i / 9) * Math.PI * 2 + r() * 0.3;
    const q = sanft(klemme(raus * 1.6 - i * 0.07));
    if (q <= 0) continue;
    const x = mix(LAB.cx, LAB.cx + Math.cos(a) * 760, q), y = mix(LAB.cy, LAB.cy + Math.sin(a) * 360, q);
    material(g, x, y, 1.3, { alpha: klemme(q * 4) });
    if (i % 3 === 0) g.text('CC', x + 22, y - 30, { groesse: 18, gewicht: 700, farbe: FARBEN.akzent, alpha: klemme(q * 4) });
  }
  kasten(g, 'kostenlos geteilt', CX, 160, z.abWort('kostenlos', 0.8), { groesse: 32, rahmen: FARBEN.akzent });
  kasten(g, 'für alle, die nicht dabei waren', CX, 1010, z.abWort('alle', 0.8), { groesse: 30 });
}

function E22(g, z) {
  g.mit(0.1, () => labor(g, z.t));
  g.text('aus der Begleitforschung', CX, 300, { groesse: 30, align: 'center', farbe: FARBEN.leise, alpha: z.abWort('Begleitforschung', 0.8) });
  g.schreiben('„Kultur des Teilens“', CX, 470, z.abWort('Kultur', 1.6, -0.3), { groesse: 84, kursiv: true, align: 'center' });
  g.linie(CX - 90, 520, CX + 90, 520, sanft(z.abWort('Teilens', 0.8, 0.3)), { breite: 5, farbe: FARBEN.orange });
  g.absatz('„relilab ist das, was du daraus machst.“', CX, 680,
    { groesse: 62, kursiv: true, p: z.abWort('relilab', 2.4, -0.2), breite: 1500 });
}

const ZWEIGE = [
  { name: 'relilabBRU', wort: 'relilabBRU', x: 330, y: 210 },
  { name: 'relilab Junior', wort: 'Junior', x: 1590, y: 210 },
  { name: 'reliGlobal', wort: 'reliGlobal', x: 330, y: 880 },
  { name: 'RELImentar', wort: 'RELImentar', x: 1590, y: 880 },
];

function E23(g, z) {
  g.mini(CX, CY, 0.72, () => labor(g, z.t));
  ZWEIGE.forEach((zw) => {
    const q = z.abWort(zw.wort, 1.2, -0.3);
    const a = Math.atan2(zw.y - CY, zw.x - CX);
    const rand = [CX + Math.cos(a) * LAB.rx * 0.72, CY + 14 + Math.sin(a) * LAB.ry * 0.72];
    g.linie(...rand, zw.x, zw.y, sanft(q), { breite: 3 });
    g.kreis(zw.x, zw.y, 16, aus(klemme(q * 2 - 1)), { breite: 3, fuellen: true, farbe: FARBEN.akzent });
    g.text(zw.name, zw.x, zw.y + (zw.y < CY ? -36 : 56), { groesse: 34, align: 'center', alpha: klemme(q * 2 - 1) });
  });
}

const E24 = mitMotiv((g, z) => labor(g, z.t));

// ---------- Szene 5 · Der Bruch: Inseln ----------

function E25(g, z) {
  const riss = z.abWort('übernommen', 2.2, -0.2);
  pulsfeld(g, z.t, { kantenAlpha: (1 - riss) * 0.5, puls: 0, sichtbar: 1 - riss * 0.5 });
  const S = 150;
  const striche = [
    [CX - S * 0.35, CY - S, CX - S * 0.55, CY + S], [CX + S * 0.55, CY - S, CX + S * 0.35, CY + S],
    [CX - S, CY - S * 0.35, CX + S, CY - S * 0.35], [CX - S, CY + S * 0.35, CX + S, CY + S * 0.35],
  ];
  g.rechteck(CX - S * 1.4, CY - S * 1.4, S * 2.8, S * 2.8, 30, 1, { breite: 0.1, farbe: FARBEN.papier, fuellung: FARBEN.papier, fuellAlpha: 0.85 * (1 - riss) });
  striche.forEach(([x1, y1, x2, y2], i) => {
    const r = sanft(riss);
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    const dx = (mx - CX) * 1.8 * r + (i % 2 ? 40 : -40) * r, dy = (my - CY) * 1.8 * r + (i < 2 ? 60 : -30) * r;
    const rot = (i % 2 ? 0.4 : -0.3) * r;
    g.ctx.save();
    g.ctx.translate(mx + dx, my + dy);
    g.ctx.rotate(rot);
    g.linie(x1 - mx, y1 - my, x2 - mx, y2 - my, aus(z.ab(0.2 + i * 0.15, 0.8)), { breite: 14, alpha: 1 - r * 0.85 });
    g.ctx.restore();
  });
  const x = z.abWort('X', 1.0, -0.1);
  g.linie(CX - 90, CY - 90, CX + 90, CY + 90, x, { breite: 10 });
  g.linie(CX + 90, CY - 90, CX - 90, CY + 90, klemme(x * 2 - 1), { breite: 10 });
  kasten(g, '2022', CX, 170, z.abWort('2022', 0.8), { groesse: 40 });
  kasten(g, 'auch kein relicamp mehr', CX, 990, z.abWort('relicamp', 0.8), { groesse: 32 });
}

function E26(g, z) {
  const namenP = ['Instagram', 'Newsletter', 'Chat', 'Webseite'].map((w) => z.abWort(w, 0.8));
  inseln(g, z.t, { p: z.abWort('verstreut', 2.8, -0.6), namenP });
}

function E27(g, z) {
  inseln(g, z.t, { verblassen: z.abWort('Netzwerkpflege', 5, -0.5) });
  kasten(g, 'Netzwerkpflege fehlt', CX, 575, z.abWort('Netzwerkpflege', 0.8), { groesse: 32 });
}

const E28 = mitMotiv((g, z) => {
  // Haus aus gestrichelten Linien, das verblasst
  const q = 1 - 0.6 * z.ab(4, 3);
  g.pfad([[660, 900], [660, 520], [960, 280], [1260, 520], [1260, 900], [660, 900]], aus(z.ab(0.5, 2)),
    { breite: 6, strich: [18, 14], alpha: q });
  g.rechteck(900, 700, 120, 200, 6, aus(z.ab(1.5, 1)), { breite: 5, strich: [12, 10], alpha: q });
});

// ---------- Szene 6 · reli-hub: Protokoll statt Plattform ----------

function E29(g, z) {
  const lp = z.abWort('Protokoll', 2.2, -0.4);
  inseln(g, z.t, { alpha: 0.6, namen: true, namenP: [0.6, 0.6, 0.6, 0.6] });
  g.linie(80, 575, 1840, 575, sanft(lp), { breite: 4, farbe: FARBEN.akzent });
  g.text('Protokoll', 110, 552, { groesse: 30, alpha: lp, farbe: FARBEN.akzent });
  const n = z.abWort('Nostr', 1.2, -0.2);
  kasten(g, 'Nostr', 1720, 575, n, { groesse: 36, rahmen: FARBEN.akzent, farbe: FARBEN.akzent });
  kasten(g, 'reli-hub  ·  Arbeitstitel', CX, 1010, z.abWort('reli-hub', 0.8), { groesse: 32 });
  INSELN.forEach((ins) => {
    const oben = ins.cy < 575;
    g.linie(ins.cx, oben ? ins.cy + 140 : ins.cy - 140, ins.cx, 575, sanft(n), { breite: 2.5, farbe: FARBEN.akzent, alpha: 0.8 });
  });
}

function E30(g, z) {
  const zielX = 1760, zielY = 560;
  protokollnetz(g, z.t, {
    p: aus(z.ab(0.2, 2.2)), schluessel: z.abWort('Schlüssel', 2.4, -0.6),
    umzug: { i: 9, x: zielX, y: zielY, q: z.abWort('verlässt', 2.0, 0) },
  });
  kasten(g, 'eigener Schlüssel', CX, 1010, z.abWort('Schlüssel', 0.8), { groesse: 30, rahmen: FARBEN.akzent });
  kasten(g, 'Identität und Inhalte ziehen mit', CX, 140, z.abWort('Identität', 0.8), { groesse: 30 });
}

const FENSTER = ['Materialpool', 'Fortbildungskalender', 'relilab', 'Institute', '+ eigene'];
const FENSTER_WORT = ['Materialpool', 'Fortbildungskalender', 'relilab', 'Institute', 'Partner'];

function E31(g, z) {
  const dr = z.abWort('Datenraum', 1.6, -0.4);
  g.rechteck(180, 760, 1560, 150, 18, aus(dr), { breite: 3, fuellung: '#e9dfca', fuellAlpha: 0.7 });
  g.text('gemeinsamer Datenraum', CX, 848, { groesse: 36, align: 'center', alpha: dr });
  FENSTER.forEach((name, i) => {
    const q = z.abWort(FENSTER_WORT[i], 1.0, -0.2);
    if (q <= 0) return;
    const cx = 260 + i * 350, w = 300, h = 210, y = 310;
    const extra = i === 4;
    g.mit(aus(q), () => {
      g.rechteck(cx - w / 2, y, w, h, 10, 1, { breite: 2.5, fuellung: FARBEN.papier, strich: extra ? [10, 8] : undefined });
      g.linie(cx - w / 2, y + 44, cx + w / 2, y + 44, 1, { breite: 2, alpha: 0.5, strich: extra ? [10, 8] : undefined });
      g.text(name, cx, y + 31, { groesse: name.length > 14 ? 21 : 25, align: 'center' });
      if (!extra) for (let k = 0; k < 3; k++) g.linie(cx - 110, y + 85 + k * 36, cx + (k === 2 ? 20 : 110), y + 85 + k * 36, 1, { breite: 2, alpha: 0.35 });
      g.linie(cx, y + h, cx, 760, sanft(q), { breite: 2, strich: [6, 8], farbe: FARBEN.akzent });
      const ph = (z.t * 0.6 + i * 0.21) % 1;
      g.punkt(cx, mix(760, y + h, ph), 6, { farbe: FARBEN.orange, alpha: Math.sin(ph * Math.PI) });
    });
  });
}

function etikett(g, x, y, s = 1, o = {}) {
  g.pfad([[x, y], [x + 46 * s, y], [x + 60 * s, y + 14 * s], [x + 46 * s, y + 28 * s], [x, y + 28 * s], [x, y]], 1,
    { breite: 2.5, farbe: FARBEN.akzent, alpha: o.alpha ?? 1 });
  g.punkt(x + 46 * s, y + 14 * s, 3.5 * s, { farbe: FARBEN.akzent, alpha: o.alpha ?? 1 });
}

function E32(g, z) {
  const tags = z.abWort('Standards', 2, -0.2);
  for (let i = 0; i < 6; i++) {
    const x = 330 + i * 250, y = 400;
    material(g, x, y, 2.2, { alpha: aus(z.ab(0.2 + i * 0.12, 0.8)) });
    const q = aus(klemme(tags * 1.6 - i * 0.12));
    if (q > 0) etikett(g, x + 30, y - 78 - (1 - q) * 30, 1.2, { alpha: q });
  }
  const texte = ['einheitliche Metadaten', 'offene Lizenzen', 'gemeinsame Vokabulare'];
  const breiten = texte.map((s) => 80 + g.breite(s, 34));
  const luecke = 90;
  let x = (W - breiten.reduce((a, b) => a + b, 0) - luecke * 2) / 2;
  ['Metadaten', 'Lizenzen', 'Vokabulare'].forEach((w, k) => {
    const q = z.abWort(w, 0.8, -0.2);
    const x0 = x, y = 760;
    x += breiten[k] + luecke;
    if (q <= 0) return;
    g.mit(q, () => {
      etikett(g, x0, y - 22, 1);
      g.text(texte[k], x0 + 80, y, { groesse: 34 });
    });
  });
}

function E33(g, z) {
  g.mit(0.55, () => protokollnetz(g, z.t, { schluessel: 1 }));
  const q = sanft(z.abWort('zurück', 1.8, -0.3));
  const marke = (text, x, unter, wort) => {
    const gr = mix(110, 46, q);
    const y = mix(500, 380, q);
    g.rechteck(x - g.breite(text, gr) / 2 - 24, y - gr, g.breite(text, gr) + 48, gr * 1.35, 12, 1,
      { breite: 0.1, farbe: FARBEN.papier, fuellung: FARBEN.papier, fuellAlpha: 0.9 });
    g.text(text, x, y, { groesse: gr, align: 'center', alpha: mix(1, 0.75, q) });
    kasten(g, unter, x, 480, z.abWort(wort, 0.8, -0.1), { groesse: 28 });
  };
  marke('rpi-virtuell', 620, 'Material, Fortbildungen, Nachrichten', 'Nachrichten');
  marke('relilab', 1300, 'Lehrkräfte experimentieren', 'experimentieren');
  const gleich = z.abWort('nebeneinander', 1.2, -0.2);
  g.linie(420, 560, 1500, 560, sanft(gleich), { breite: 3, farbe: FARBEN.akzent });
  g.text('=', CX, 395, { groesse: 60, align: 'center', alpha: z.abWort('keines', 0.8), farbe: FARBEN.akzent });
}

const E34 = mitMotiv((g, z) => {
  protokollnetz(g, z.t, { schluessel: 1 });
  const v = z.abWort('Vokabulare', 1.2, -0.2, 1);
  PROTO_PKT.forEach(([x, y], i) => g.wellen(x, y, z.t, { periode: 2, anzahl: 1, maxR: 60, alpha: 0.5 * v, versatz: i * 0.07, farbe: FARBEN.akzent }));
});

// ---------- Szene 7 · Wer gehört wird ----------

function trichter(g, y0, alpha) {
  g.mit(alpha, () => {
    const pkt = [[520, y0], [1400, y0], [1010, y0 + 330], [1010, y0 + 470], [910, y0 + 470], [910, y0 + 330], [520, y0]];
    g.ctx.save();
    g.ctx.globalAlpha = 0.92 * g.deckkraft;
    g.ctx.fillStyle = FARBEN.tinte;
    g.ctx.beginPath();
    pkt.forEach((q, i) => (i ? g.ctx.lineTo(...q) : g.ctx.moveTo(...q)));
    g.ctx.fill();
    g.ctx.restore();
  });
}

function E35(g, z) {
  pulsfeld(g, z.t, { wellen: 1.6, puls: 0 });
  const t = sanft(z.abWort('gehört', 1.8, -0.3));
  trichter(g, mix(-560, 60, t), t);
  kasten(g, 'Wer wird gehört?', CX, 700, z.abWort('gehört', 0.8, 0.6), { groesse: 44, rahmen: FARBEN.akzent });
}

function E36(g, z) {
  const weg = z.abWort('Konzern', 1.4, -0.2);
  g.mit(1 - weg, () => pulsfeld(g, z.t, { wellen: 1.6, puls: 0 }));
  trichter(g, 60 - weg * 120, 1 - weg);
  kreise(g, z.t, { p: z.abWort('Community', 2.2, -0.4), material: z.abWort('geteilt', 3, -0.4), verbindungen: z.abWort('Menschen', 2, -0.2) });
  const red = z.abWort('Redaktionskreis', 1.2, -0.2);
  const k = KREISE[2];
  g.kreis(k.cx, k.cy, k.r - 22, red, { breite: 2, strich: [6, 8], farbe: FARBEN.tinte });
  kasten(g, 'Auswahl des Redaktionskreises', k.cx, k.cy + k.r + 50, z.abWort('Auswahl', 0.8), { groesse: 30 });
  kasten(g, 'gefunden über Menschen, denen man vertraut', CX, 1010, z.abWort('vertraut', 0.8), { groesse: 30, rahmen: FARBEN.akzent });
}

const SPUREN = [
  { w: 'teilen', text: 'geteilt' }, { w: 'Sammlung', text: 'gesammelt' }, { w: 'weiterbearbeiten', text: 'weiterbearbeitet' },
];

function E37(g, z) {
  const hoch = sanft(z.abWort('Klassiker', 2.2, -0.3));
  const karten = [{ x: 620, jahr: '2014', titel: 'Klassiker' }, { x: 1300, jahr: 'neu', titel: 'gerade in Arbeit' }];
  const nachvollziehbar = z.abWort('öffentlich', 1);
  karten.forEach((k, j) => {
    const y = mix(700, 470, hoch);
    SPUREN.forEach((s, i) => {
      const q = z.abWort(s.w, 0.9, j * 0.25);
      if (q <= 0) return;
      const a = -Math.PI / 2 + (i - 1) * 0.95 + (j ? 0.25 : -0.25);
      const px = k.x + Math.cos(a) * 250, py = y + Math.sin(a) * 210;
      g.linie(k.x + Math.cos(a) * 80, y + Math.sin(a) * 90, px, py, aus(q), { breite: 2, alpha: 0.6, farbe: FARBEN.akzent });
      g.punkt(px, py, 13 * aus(q), { farbe: FARBEN.akzent });
      g.text(s.text, px, py + (py < y ? -24 : 40), { groesse: 30, align: 'center', alpha: q * mix(0.6, 1, nachvollziehbar) });
    });
    material(g, k.x, y, 2.6, { alpha: aus(z.ab(0.2 + j * 0.3, 0.8)) });
    g.text(k.jahr, k.x, y + 110, { groesse: 30, align: 'center', farbe: FARBEN.leise, alpha: aus(z.ab(0.4 + j * 0.3, 0.8)) });
    g.text(k.titel, k.x, y + 150, { groesse: 30, align: 'center', farbe: FARBEN.leise, alpha: z.abWort('Klassiker', 0.8, j * 1.2) });
  });
  kasten(g, 'öffentlich und nachvollziehbar', CX, 1010, nachvollziehbar, { groesse: 30, rahmen: FARBEN.akzent });
}

function E38(g, z) {
  const auf = sanft(z.abWort('offen', 1.6, -0.2));
  const bx = CX - 230, by = 160, bw = 460, bh = 280;
  const r = zufall(8);
  g.mit(aus(z.ab(0, 1)), () => {
    // Menschen und ihre Verbindungen im Inneren
    const leute = Array.from({ length: 7 }, () => [bx + 50 + r() * (bw - 100), by + 50 + r() * (bh - 100)]);
    leute.forEach((p, i) => {
      if (i) g.linie(...leute[i - 1], ...p, 1, { breite: 2, alpha: 0.6 });
      g.punkt(...p, 10, { farbe: FARBEN.akzent });
    });
    g.rechteck(bx, by, bw, bh, 12, 1, { breite: 3, fuellung: FARBEN.tinte, fuellAlpha: 1 - auf });
    g.text('Algorithmus', CX, by + bh / 2 + 14, { groesse: 40, align: 'center', farbe: FARBEN.papier, alpha: 1 - auf });
    // Deckel klappt auf
    g.ctx.save();
    g.ctx.translate(bx, by);
    g.ctx.rotate(-0.5 * auf);
    g.linie(0, 0, bw, 0, 1, { breite: 5, alpha: auf });
    g.ctx.restore();
  });
  lernsatzText(g, z, 760);
}

// ---------- Szene 8 · Was trägt ----------

const SPUR = [
  ['Sendemast', 'Rundfunk'], ['Stern', 'rpi-virtuell · 2002'], ['Puls', '#relichat · 2017'], ['Gruppen', 'relicamps · 2019'],
  ['Labor', 'relilab · 2020'], ['Inseln', 'verstreut · 2022'], ['Protokoll', 'Nostr'], ['Kreise', 'reli-hub · 2027'],
];

function E39(g, z) {
  SPUR.forEach(([motiv, label], i) => {
    const q = aus(z.ab(0.2 + i * 0.45, 0.9));
    if (q <= 0) return;
    const cx = 270 + (i % 4) * 460, cy = i < 4 ? 330 : 730;
    g.mit(q, () => {
      g.rechteck(cx - 205, cy - 120, 410, 240, 10, 1, { breite: 1.5, alpha: 0.35 });
      g.mini(cx, cy, 0.2, () => MOTIVE[motiv](g, z.t));
      g.text(label, cx, cy + 165, { groesse: 30, align: 'center', farbe: FARBEN.leise });
    });
  });
}

function E40(g, z) {
  [['Offenheit', 'einsteigen, ohne zu fragen'], ['Standards', 'Beiträge passen zusammen'], ['Vertrauen', 'Begegnung, von Standards getragen']]
    .forEach(([w, unter], k) => {
      const x = 380 + k * 580;
      const q = z.abWort(w, 1.4, -0.3);
      g.schreiben(w, x, 520, q, { groesse: 78, align: 'center' });
      g.linie(x - 120, 560, x + 120, 560, sanft(klemme(q * 2 - 1)), { breite: 4, farbe: FARBEN.akzent });
      g.text(unter, x, 620, { groesse: 28, align: 'center', farbe: FARBEN.leise, alpha: z.abWort(w, 0.8, 1.6) });
    });
}

function E41(g, z) {
  protokollnetz(g, z.t, { schluessel: 1, alpha: 0.85 });
  const neu = [1830, 300];
  const q = z.abWort('lebendig', 1.2, -0.2);
  g.punkt(...neu, 14 * aus(q), { farbe: FARBEN.orange });
  const nah = PROTO_PKT.map((p) => [Math.hypot(p[0] - neu[0], p[1] - neu[1]), p]).sort((a, b) => a[0] - b[0]).slice(0, 2);
  nah.forEach(([, p], i) => g.linie(...neu, ...p, sanft(z.abWort('Menschen', 1.4, i * 0.3)), { breite: 3, farbe: FARBEN.akzent }));
  kasten(g, 'Strukturen anbieten', CX, 1010, z.abWort('anbieten', 0.8), { groesse: 30 });
}

function E42(g, z) {
  g.mit(0.25, () => kreise(g, z.t, { material: 1 }));
  g.rechteck(50, 50, W - 100, H - 100, 22, sanft(z.ab(0.2, 2.5)), { breite: 3, farbe: FARBEN.akzent, alpha: 0.8 });
  g.schreiben('reli-hub', CX, 450, z.abWort('reli-hub', 1.4, -0.3), { groesse: 150, align: 'center' });
  g.linie(CX - 120, 492, CX + 120, 492, sanft(z.abWort('reli-hub', 0.8, 0.9)), { breite: 6, farbe: FARBEN.orange });
  g.text('Arbeitstitel', CX, 535, { groesse: 28, align: 'center', kursiv: true, farbe: FARBEN.leise, alpha: z.abWort('reli-hub', 0.8, 1.0) });
  kasten(g, 'Start: Februar 2027', CX, 640, z.abWort('Februar', 0.9), { groesse: 44, rahmen: FARBEN.akzent, farbe: FARBEN.akzent });
  g.schreiben('Danke.', CX, 820, z.abWort('entsteht', 1.4, 0.8), { groesse: 70, align: 'center', kursiv: true });
}

export const SZENEN = {
  E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21,
  E22, E23, E24, E25, E26, E27, E28, E29, E30, E31, E32, E33, E34, E35, E36, E37, E38, E39, E40, E41, E42,
};
