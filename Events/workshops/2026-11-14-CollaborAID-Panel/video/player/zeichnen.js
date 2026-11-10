// Zeichenwerkzeuge im Stil „Tusche auf Papier“.
// Alle Funktionen sind zustandslos: Fortschritt p (0..1) bestimmt, wie weit etwas gezeichnet ist.

export const FARBEN = {
  papier: '#f4efe4',
  tinte: '#1f1d1a',
  leise: '#8a7f6a',
  akzent: '#203A8F', // FOERBICO-/Comenius-Blau (auch für Text, Kontrast auf Papier ≈ 9:1)
  orange: '#FFA500', // FOERBICO-Orange: nur Flächen, Punkte, Linien – nie für Text
  hell: '#d9cfbb',
};

export const SCHRIFT = 'Georgia, "Iowan Old Style", "Times New Roman", serif';

export const klemme = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const mix = (a, b, p) => a + (b - a) * p;
export const sanft = (p) => (p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2);
export const aus = (p) => 1 - Math.pow(1 - p, 3);

// Deterministischer Zufall (gleicher Startwert → gleiche Folge)
export function zufall(startwert) {
  let s = startwert >>> 0 || 1;
  return () => {
    s ^= s << 13; s ^= s >>> 17; s ^= s << 5;
    return ((s >>> 0) % 100000) / 100000;
  };
}

let kornCache = null;

export function werkzeuge(ctx, W, H) {
  // Papierstruktur einmal vorberechnen (für alle Puffer gemeinsam)
  const korn = kornCache ?? document.createElement('canvas');
  const neu = !kornCache;
  kornCache = korn;
  if (neu) {
    korn.width = W; korn.height = H;
    const k = korn.getContext('2d');
    k.fillStyle = FARBEN.papier;
    k.fillRect(0, 0, W, H);
    const r = zufall(7);
    for (let i = 0; i < 9000; i++) {
      k.fillStyle = `rgba(90,70,40,${0.025 + r() * 0.035})`;
      k.fillRect(r() * W, r() * H, 1 + r() * 2, 1 + r() * 2);
    }
    const v = k.createRadialGradient(W / 2, H / 2, H * 0.35, W / 2, H / 2, H * 0.95);
    v.addColorStop(0, 'rgba(0,0,0,0)');
    v.addColorStop(1, 'rgba(80,60,30,0.10)');
    k.fillStyle = v;
    k.fillRect(0, 0, W, H);
  }

  function stift(o = {}) {
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.lineWidth = (o.breite ?? 3) * g.faktor;
    if (o.strich) ctx.setLineDash(o.strich.map((v) => v * g.faktor));
    ctx.strokeStyle = o.farbe ?? FARBEN.tinte;
    ctx.fillStyle = o.farbe ?? FARBEN.tinte;
    ctx.globalAlpha = (o.alpha ?? 1) * g.deckkraft;
  }

  const g = {
    ctx, W, H, FARBEN,
    faktor: 1, // Strichstärken-Faktor (für verkleinerte Motive)
    deckkraft: 1, // gemeinsame Deckkraft für alles, was in g.mit() gezeichnet wird

    mit(alpha, fn) {
      if (alpha <= 0) return;
      const alt = g.deckkraft;
      g.deckkraft = alt * alpha;
      try { fn(); } finally { g.deckkraft = alt; }
    },

    breite(s, groesse = 48, o = {}) {
      ctx.save();
      ctx.font = g.schrift(groesse, o);
      const b = ctx.measureText(s).width;
      ctx.restore();
      return b;
    },

    // Zeichnet fn() als verkleinertes Vollbild-Motiv, zentriert bei (cx, cy)
    mini(cx, cy, s, fn) {
      ctx.save();
      ctx.translate(cx, cy);
      ctx.scale(s, s);
      ctx.translate(-W / 2, -H / 2);
      const alt = g.faktor;
      g.faktor = 0.75 / s;
      try { fn(); } finally { g.faktor = alt; ctx.restore(); }
    },

    // Abgerundetes Rechteck, Umriss zeichnet sich mit p
    rechteck(x, y, w, h, r = 12, p = 1, o = {}) {
      if (p <= 0) return;
      const pkt = [];
      const ecke = (cx, cy, a0) => {
        for (let k = 0; k <= 6; k++) {
          const a = a0 + (k / 6) * (Math.PI / 2);
          pkt.push([cx + Math.cos(a) * r, cy + Math.sin(a) * r]);
        }
      };
      pkt.push([x + r, y]);
      ecke(x + w - r, y + r, -Math.PI / 2);
      ecke(x + w - r, y + h - r, 0);
      ecke(x + r, y + h - r, Math.PI / 2);
      ecke(x + r, y + r, Math.PI);
      pkt.push([x + r, y]);
      if (o.fuellung && p >= 1) {
        ctx.save();
        ctx.globalAlpha = (o.fuellAlpha ?? 1) * (o.alpha ?? 1) * g.deckkraft;
        ctx.fillStyle = o.fuellung;
        ctx.beginPath();
        pkt.forEach((q, i) => (i ? ctx.lineTo(...q) : ctx.moveTo(...q)));
        ctx.fill();
        ctx.restore();
      }
      g.pfad(pkt, p, o);
    },

    // Wellen, die periodisch von (x, y) ausgehen; t ist die globale Zeit
    wellen(x, y, t, o = {}) {
      const periode = o.periode ?? 1.8, anzahl = o.anzahl ?? 3, maxR = o.maxR ?? 70;
      for (let k = 0; k < anzahl; k++) {
        const ph = ((t / periode) + k / anzahl + (o.versatz ?? 0)) % 1;
        const a = (1 - ph) * (o.alpha ?? 0.6);
        if (o.boegen) {
          for (const [a0, a1] of o.boegen) g.kreis(x, y, 8 + ph * maxR, 1, { ...o, alpha: a, start: a0, ende: a1 });
        } else {
          g.kreis(x, y, 4 + ph * maxR, 1, { breite: o.breite ?? 2, farbe: o.farbe, alpha: a });
        }
      }
    },

    papier() {
      ctx.globalAlpha = 1;
      ctx.drawImage(korn, 0, 0);
    },

    linie(x1, y1, x2, y2, p = 1, o = {}) {
      if (p <= 0) return;
      ctx.save(); stift(o);
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(mix(x1, x2, p), mix(y1, y2, p));
      ctx.stroke();
      ctx.restore();
    },

    // Linienzug, der sich mit p entlang seiner Länge zeichnet
    pfad(punkte, p = 1, o = {}) {
      if (p <= 0 || punkte.length < 2) return;
      const laengen = [0];
      for (let i = 1; i < punkte.length; i++) {
        laengen.push(laengen[i - 1] + Math.hypot(punkte[i][0] - punkte[i - 1][0], punkte[i][1] - punkte[i - 1][1]));
      }
      const ziel = laengen.at(-1) * klemme(p);
      ctx.save(); stift(o);
      ctx.beginPath();
      ctx.moveTo(...punkte[0]);
      for (let i = 1; i < punkte.length; i++) {
        if (laengen[i] <= ziel) { ctx.lineTo(...punkte[i]); continue; }
        const q = (ziel - laengen[i - 1]) / (laengen[i] - laengen[i - 1]);
        ctx.lineTo(mix(punkte[i - 1][0], punkte[i][0], q), mix(punkte[i - 1][1], punkte[i][1], q));
        break;
      }
      ctx.stroke();
      ctx.restore();
    },

    kreis(x, y, r, p = 1, o = {}) {
      if (p <= 0) return;
      ctx.save(); stift(o);
      ctx.beginPath();
      const start = o.start ?? -Math.PI / 2;
      const ende = o.ende ?? start + Math.PI * 2;
      ctx.arc(x, y, r, start, start + (ende - start) * klemme(p));
      if (o.fuellen) ctx.fill(); else ctx.stroke();
      ctx.restore();
    },

    punkt(x, y, r = 8, o = {}) {
      if ((o.alpha ?? 1) <= 0 || r <= 0) return;
      ctx.save(); stift(o);
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    },

    schrift(groesse = 48, o = {}) {
      return `${o.kursiv ? 'italic ' : ''}${o.gewicht ?? 400} ${groesse}px ${o.familie ?? SCHRIFT}`;
    },

    text(s, x, y, o = {}) {
      if ((o.alpha ?? 1) <= 0) return;
      ctx.save();
      ctx.font = g.schrift(o.groesse, o);
      ctx.fillStyle = o.farbe ?? FARBEN.tinte;
      ctx.globalAlpha = (o.alpha ?? 1) * g.deckkraft;
      ctx.textAlign = o.align ?? 'left';
      ctx.textBaseline = o.basis ?? 'alphabetic';
      ctx.fillText(s, x, y);
      ctx.restore();
    },

    // Text, der sich Zeichen für Zeichen hinschreibt (weiches Einblenden)
    schreiben(s, x, y, p, o = {}) {
      if (p <= 0) return;
      ctx.save();
      ctx.font = g.schrift(o.groesse, o);
      const gesamt = ctx.measureText(s).width;
      let cx = o.align === 'center' ? x - gesamt / 2 : o.align === 'right' ? x - gesamt : x;
      const n = s.length, weich = 4;
      const pos = p * (n + weich);
      ctx.fillStyle = o.farbe ?? FARBEN.tinte;
      ctx.textBaseline = o.basis ?? 'alphabetic';
      for (let i = 0; i < n; i++) {
        const a = klemme((pos - i) / weich);
        const ch = s[i];
        if (a > 0) {
          ctx.globalAlpha = a * (o.alpha ?? 1) * g.deckkraft;
          ctx.fillText(ch, cx, y);
        }
        cx += ctx.measureText(ch).width;
      }
      ctx.restore();
    },

    umbruch(s, maxBreite, groesse = 40, o = {}) {
      ctx.save();
      ctx.font = g.schrift(groesse, o);
      const zeilen = [];
      let zeile = '';
      for (const w of s.split(/\s+/)) {
        const test = zeile ? zeile + ' ' + w : w;
        if (ctx.measureText(test).width > maxBreite && zeile) { zeilen.push(zeile); zeile = w; }
        else zeile = test;
      }
      if (zeile) zeilen.push(zeile);
      ctx.restore();
      return zeilen;
    },

    // Mehrzeiliger Text, mittig um y, optional zeilenweise hingeschrieben
    absatz(s, x, y, o = {}) {
      const groesse = o.groesse ?? 44;
      const zeilen = g.umbruch(s, o.breite ?? 1300, groesse, o);
      const hoehe = groesse * (o.zeilenabstand ?? 1.35);
      const y0 = y - ((zeilen.length - 1) * hoehe) / 2;
      zeilen.forEach((z, i) => {
        const p = o.p === undefined ? 1 : klemme(o.p * zeilen.length - i);
        g.schreiben(z, x, y0 + i * hoehe, p, { ...o, align: o.align ?? 'center' });
      });
    },
  };
  return g;
}
