// Abspiel- und Render-Kern.
// Jedes Bild ist eine reine Funktion der Zeit t: window.renderFrame(t) zeichnet genau
// den Zustand zum Zeitpunkt t, ohne sich etwas zwischen Bildern zu merken. So sind
// Vorschau im Browser und bildgenauer Export (tools/render.py) identisch.
import { SZENEN, standardSzene, LEKTIONEN } from './szenen.js';
import { werkzeuge, FARBEN, sanft } from './zeichnen.js';

const W = 1920, H = 1080;
const params = new URLSearchParams(location.search);
const RENDER = params.has('render');
const leinwand = document.getElementById('leinwand');
const ctx = leinwand.getContext('2d');
const g = werkzeuge(ctx, W, H);
const opt = {
  regie: RENDER ? params.has('regie') : true,
  untertitel: params.has('untertitel'),
};

let tl = null;

function einheitBei(t) {
  const es = tl.einheiten;
  let lo = 0, hi = es.length - 1;
  while (lo < hi) {
    const mid = (lo + hi + 1) >> 1;
    if (es[mid].start <= t) lo = mid; else hi = mid - 1;
  }
  return lo;
}

const norm = (s) => s.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '');

// Zeitangaben für eine Szene: alles in lokaler Zeit (Sekunden ab Beginn der Einheit)
function zeitInfo(e, t, index) {
  const lt = t - e.start;
  const dauer = e.ende - e.start;
  const wortZeit = (muster, nr = 1) => {
    const m = norm(muster);
    let gefunden = 0;
    for (const w of e.woerter) {
      if (norm(w.w).includes(m) && ++gefunden === nr) return w.start - e.start;
    }
    console.warn(`${e.id}: Wort „${muster}“ nicht gefunden`);
    return 0;
  };
  return {
    t, lt, dauer, e, index,
    p: Math.min(1, Math.max(0, lt / dauer)),
    sprechende: e.sprechende - e.start,
    // Fortschritt 0..1 ab lokaler Zeit `ab` über `d` Sekunden
    ab: (ab, d = 0.8) => Math.min(1, Math.max(0, (lt - ab) / d)),
    // lokale Zeit, zu der ein Wort gesprochen wird (n-tes Vorkommen)
    wort: wortZeit,
    // Fortschritt ab einem gesprochenen Wort
    abWort: (muster, d = 0.8, versatz = 0, nr = 1) =>
      Math.min(1, Math.max(0, (lt - wortZeit(muster, nr) - versatz) / d)),
    vorher: index > 0 ? tl.einheiten[index - 1] : null,
    nachher: index + 1 < tl.einheiten.length ? tl.einheiten[index + 1] : null,
  };
}

function untertitel(e, t) {
  const woerter = e.woerter;
  ctx.save();
  ctx.font = '30px Georgia, serif';
  ctx.textBaseline = 'alphabetic';
  // Satz um das aktuelle Wort herum
  let i = woerter.findIndex((w) => w.ende > t);
  if (i < 0) i = woerter.length - 1;
  let a = i, b = i;
  while (a > 0 && !/[.?!:]$/.test(woerter[a - 1].w)) a--;
  while (b < woerter.length - 1 && !/[.?!:]$/.test(woerter[b].w)) b++;
  const teile = woerter.slice(a, b + 1);
  const breite = teile.reduce((s, w) => s + ctx.measureText(w.w + ' ').width, 0);
  let x = (W - Math.min(breite, 1700)) / 2, y = H - 60;
  ctx.fillStyle = 'rgba(244,239,228,.85)';
  ctx.fillRect(0, H - 110, W, 110);
  for (const w of teile) {
    const m = ctx.measureText(w.w + ' ').width;
    if (x + m > W - 110) { x = 110; y += 38; }
    ctx.fillStyle = w.start <= t ? FARBEN.tinte : FARBEN.leise;
    ctx.fillText(w.w, x, y);
    x += m;
  }
  ctx.restore();
}

function regieZeile(e, t) {
  ctx.save();
  ctx.font = '20px ui-monospace, monospace';
  ctx.fillStyle = 'rgba(138,127,106,.9)';
  ctx.textAlign = 'right';
  ctx.fillText(`${e.id} · ${e.tag} · ${t.toFixed(2)} s`, W - 30, 40);
  ctx.restore();
}

// Überblendung zwischen Einheiten: beide Szenen in Puffer zeichnen und mischen
const BLENDE = 0.5;
const puffer = [0, 1].map(() => {
  const c = document.createElement('canvas');
  c.width = W; c.height = H;
  return { c, g: werkzeuge(c.getContext('2d'), W, H) };
});

function szeneZeichnen(gg, i, t) {
  const e = tl.einheiten[i];
  gg.papier();
  (SZENEN[e.id] || standardSzene)(gg, zeitInfo(e, t, i), { regie: opt.regie, szenen: tl.szenen });
}

function kapitel(e, t) {
  const sz = tl.szenen.find((s) => s.nr === e.szene);
  if (!sz || sz.nr === 0 || sz.nr === 8) return;
  const ein = Math.min(1, Math.max(0, (t - sz.start - 0.3) / 1.0));
  const aus = Math.min(1, Math.max(0, (sz.ende - t) / 0.6));
  g.text(sz.titel.toUpperCase(), 80, 70,
    { groesse: 26, farbe: FARBEN.leise, alpha: 0.85 * ein * aus, familie: 'Georgia, serif' });
}

// Mitlaufende Leiste der Lektionen oben rechts: erreichte dunkel, aktuelle blau und
// unterstrichen, kommende blass. Erscheint mit der ersten Lektion, verschwindet zum Schlussbild.
function lektionsleiste(t) {
  const ids = Object.keys(LEKTIONEN);
  const einheit = (id) => tl.einheiten.find((e) => e.id === id);
  const starts = ids.map((id) => einheit(id)?.start ?? Infinity);
  const schluss = tl.einheiten.at(-1).start;
  const sicht = Math.min(1, Math.max(0, (t - starts[0]) / 0.8)) * Math.min(1, Math.max(0, (schluss - t) / 0.6));
  if (sicht <= 0) return;
  const aktuell = starts.filter((s) => s <= t).length - 1;
  const lu = einheit(ids[aktuell]);
  const imLernsatz = lu && t >= lu.start && t < lu.ende;
  const groesse = 22, luecke = 30;
  const texte = ids.map((id, k) => `${k + 1} ${LEKTIONEN[id]}`);
  const breiten = texte.map((s, k) => g.breite(s, groesse, { gewicht: k === aktuell ? 700 : 400 }));
  let x = 1860 - breiten.reduce((a, b) => a + b, 0) - luecke * (ids.length - 1);
  texte.forEach((s, k) => {
    const farbe = k === aktuell ? FARBEN.akzent : k < aktuell ? FARBEN.tinte : FARBEN.leise;
    const alpha = (k === aktuell ? 1 : k < aktuell ? 0.75 : 0.45) * sicht;
    g.text(s, x, 72, { groesse, farbe, alpha, gewicht: k === aktuell ? 700 : 400, familie: 'Georgia, serif' });
    if (k === aktuell && imLernsatz) {
      const q = Math.min(1, Math.max(0, (t - lu.start) / 0.8));
      g.linie(x, 84, x + breiten[k] * q, 84, 1, { breite: 4, farbe: FARBEN.orange, alpha: sicht });
    }
    x += breiten[k] + luecke;
  });
}

window.renderFrame = (t) => {
  const i = einheitBei(t);
  const e = tl.einheiten[i];
  const lt = t - e.start;
  if (i > 0 && lt < BLENDE) {
    szeneZeichnen(puffer[0].g, i - 1, t);
    szeneZeichnen(puffer[1].g, i, t);
    const f = sanft(lt / BLENDE);
    ctx.globalAlpha = 1;
    ctx.drawImage(puffer[0].c, 0, 0);
    ctx.globalAlpha = f;
    ctx.drawImage(puffer[1].c, 0, 0);
    ctx.globalAlpha = 1;
  } else {
    szeneZeichnen(g, i, t);
  }
  kapitel(e, t);
  lektionsleiste(t);
  if (opt.untertitel) untertitel(e, t);
  if (opt.regie) regieZeile(e, t);
};

window.bereit = (async () => {
  tl = await (await fetch('../build/timeline.json', { cache: 'no-store' })).json();
  await document.fonts.ready;
  window.DAUER = tl.dauer;
  return tl.dauer;
})();

// ---------- Vorschau-Bedienung ----------
if (RENDER) {
  document.body.classList.add('render');
} else {
  const ton = document.getElementById('ton');
  const knopf = document.getElementById('abspielen');
  const regler = document.getElementById('zeit');
  const anzeige = document.getElementById('anzeige');
  const liste = document.getElementById('einheiten');
  const fmt = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;

  window.bereit.then((dauer) => {
    ton.src = '../build/' + tl.audio;
    regler.max = dauer;
    for (const e of tl.einheiten) {
      const li = document.createElement('li');
      li.textContent = `${e.id} ${e.tag} (${fmt(e.start)})`;
      li.onclick = () => { ton.currentTime = e.start + 0.001; zeichne(); };
      liste.append(li);
    }
    zeichne();
  });

  let letzteEinheit = -1;
  function zeichne() {
    const t = ton.currentTime;
    window.renderFrame(t);
    regler.value = t;
    anzeige.textContent = `${fmt(t)} / ${fmt(tl.dauer)}`;
    const i = einheitBei(t);
    if (i !== letzteEinheit) {
      liste.children[letzteEinheit]?.classList.remove('aktiv');
      liste.children[i]?.classList.add('aktiv');
      letzteEinheit = i;
    }
  }
  function schleife() { zeichne(); if (!ton.paused) requestAnimationFrame(schleife); }
  const umschalten = () => (ton.paused ? ton.play() : ton.pause());
  ton.onplay = () => { knopf.textContent = '❚❚'; requestAnimationFrame(schleife); };
  ton.onpause = () => { knopf.textContent = '▶'; zeichne(); };
  knopf.onclick = umschalten;
  regler.oninput = () => { ton.currentTime = +regler.value; zeichne(); };
  document.getElementById('regie').onchange = (ev) => { opt.regie = ev.target.checked; zeichne(); };
  document.getElementById('untertitel').onchange = (ev) => { opt.untertitel = ev.target.checked; zeichne(); };
  addEventListener('keydown', (ev) => {
    if (ev.code === 'Space') { ev.preventDefault(); umschalten(); }
    if (ev.code === 'ArrowRight') { ton.currentTime += 5; zeichne(); }
    if (ev.code === 'ArrowLeft') { ton.currentTime -= 5; zeichne(); }
  });
}
