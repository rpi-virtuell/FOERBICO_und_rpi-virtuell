# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["faster-whisper>=1.1", "numpy"]
# ///
"""Richtet eine Aufnahme auf den Sprechtext aus und schneidet sie automatisch.

1. Whisper erkennt die Aufnahme mit Zeitstempeln je Wort.
2. Jede Sinneinheit aus build/beats.json wird in der Erkennung gesucht. Gibt es eine
   Einheit mehrmals (Versprecher, neu angesetzt), gewinnt die vollständigste, bei
   Gleichstand die spätere Fassung.
3. Die gefundenen Abschnitte werden ohne Versprecher und mit festen Pausen
   aneinandergesetzt und auf -16 LUFS normalisiert.

Ausgabe:
  build/stimme.wav       – geschnittene, normalisierte Tonspur (48 kHz, mono)
  build/timeline.json    – Start/Ende jeder Einheit und jedes Wortes in stimme.wav
  build/transkript.json  – Rohes Whisper-Ergebnis (Zwischenspeicher, wird wiederverwendet)

Aufruf:
  uv run tools/align.py aufnahme/meine-aufnahme.wav [--modell small] [--neu]
"""
import argparse
import array
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
import wave
from difflib import SequenceMatcher
from pathlib import Path

HIER = Path(__file__).resolve().parent.parent
BUILD = HIER / "build"
RATE = 48000

PAUSE = 0.7          # Sekunden zwischen Einheiten
PAUSE_LERNSATZ = 1.6 # nach einem Lernsatz (Szenenende)
VORLAUF, NACHLAUF = 1.0, 2.5
RAND_VOR, RAND_NACH = 0.12, 0.35  # Luft um die erkannten Wortgrenzen
MIN_SCORE = 0.45


def norm(wort: str) -> str:
    w = unicodedata.normalize("NFC", wort.lower())
    w = w.replace("ß", "ss")
    return re.sub(r"[^\w]", "", w)


def tokens(text: str) -> list[str]:
    return [t for t in (norm(w) for w in text.split()) if t]


def transkribieren(audio: Path, modell: str, prompt: str) -> list[dict]:
    import numpy as np
    from faster_whisper import WhisperModel
    # Selbst dekodieren (16 kHz mono float), damit es nicht auf die PyAV-Version ankommt
    pcm = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(audio), "-ac", "1", "-ar", "16000",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    signal = np.frombuffer(pcm, dtype=np.float32)
    m = WhisperModel(modell, device="cpu", compute_type="int8")
    segmente, info = m.transcribe(signal, language="de", word_timestamps=True,
                                  initial_prompt=prompt, vad_filter=False, beam_size=5)
    woerter = []
    for seg in segmente:
        for w in seg.words or []:
            woerter.append({"w": w.word.strip(), "start": round(w.start, 3), "ende": round(w.end, 3)})
        print(f"\r  erkannt bis {seg.end:6.1f} s / {info.duration:.0f} s", end="", file=sys.stderr)
    print(file=sys.stderr)
    return woerter


def kandidaten(u: list[str], t: list[str]) -> list[tuple[float, int, int]]:
    """Fenster in t, die der Einheit u ähneln: (score, start, ende_exkl)."""
    n = len(u)
    breite = n + max(2, n // 5)
    roh = []
    uset = set(u)
    for s in range(0, max(1, len(t) - 1)):
        fenster = t[s:s + breite]
        if not fenster or fenster[0] not in uset:
            continue
        sm = SequenceMatcher(None, u, fenster, autojunk=False)
        treffer = sum(b.size for b in sm.get_matching_blocks())
        if treffer == 0:
            continue
        score = treffer / n
        bloecke = [b for b in sm.get_matching_blocks() if b.size]
        roh.append((score, s + bloecke[0].b, s + bloecke[-1].b + bloecke[-1].size))
    # Nur lokale Bestwerte behalten
    roh.sort(key=lambda k: -k[0])
    gewaehlt = []
    for k in roh:
        if k[0] < MIN_SCORE:
            break
        if all(abs(k[1] - g[1]) > n // 2 for g in gewaehlt):
            gewaehlt.append(k)
        if len(gewaehlt) >= 8:
            break
    return gewaehlt


def zuordnen(einheiten: list[dict], t: list[str], ohne: set = frozenset(), auslassen: float = 1.0) -> list[tuple[int, int] | None]:
    """Dynamische Programmierung: je Einheit ein Fenster, monoton steigend."""
    # Einheiten in `ohne` werden hier nicht gesucht (kommen aus einer Nachaufnahme)
    kand = [[] if e["id"] in ohne else kandidaten(tokens(e["text"]), t) for e in einheiten]
    # Zustand: (summe, liste der wahlen) je mögliches Ende; einfache Variante über Einheiten
    best = {-1: (0.0, [])}  # letztes ende_exkl -> (summe, wahl)
    for i, ks in enumerate(kand):
        neu = {}
        for ende_alt, (summe, wahl) in best.items():
            # Einheit auslassen ist erlaubt, kostet aber
            key = ende_alt
            wert = summe - (0.0 if einheiten[i]["id"] in ohne else auslassen)
            if key not in neu or neu[key][0] < wert:
                neu[key] = (wert, wahl + [None])
            for score, s, e in ks:
                if s >= ende_alt:
                    # leichte Vorliebe für spätere Fassung bei Gleichstand
                    wert = summe + score + 1e-6 * s
                    if e not in neu or neu[e][0] < wert:
                        neu[e] = (wert, wahl + [(s, e)])
        # beschneiden: nur die besten 40 Zustände
        best = dict(sorted(neu.items(), key=lambda kv: -kv[1][0])[:40])
    return max(best.values(), key=lambda v: v[0])[1]


def woerter_zuordnen(einheit: dict, roh: list[dict], s: int, e: int) -> list[dict]:
    orig = einheit["text"].split()
    u = [norm(w) for w in orig]
    t = [norm(w["w"]) for w in roh[s:e]]
    zeiten: list[tuple[float, float] | None] = [None] * len(orig)
    for b in SequenceMatcher(None, u, t, autojunk=False).get_matching_blocks():
        for k in range(b.size):
            w = roh[s + b.b + k]
            zeiten[b.a + k] = (w["start"], w["ende"])
    # Lücken linear auffüllen
    anfang, schluss = roh[s]["start"], roh[e - 1]["ende"]
    i = 0
    while i < len(zeiten):
        if zeiten[i] is None:
            j = i
            while j < len(zeiten) and zeiten[j] is None:
                j += 1
            a = zeiten[i - 1][1] if i > 0 else anfang
            z = zeiten[j][0] if j < len(zeiten) else schluss
            schritt = max(0.0, z - a) / (j - i)
            for k in range(i, j):
                zeiten[k] = (a + (k - i) * schritt, a + (k - i + 1) * schritt)
            i = j
        else:
            i += 1
    return [{"w": w, "start": round(z[0], 3), "ende": round(z[1], 3)} for w, z in zip(orig, zeiten)]


def lesen_pcm(audio: Path, ziel: Path):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(audio), "-ac", "1", "-ar", str(RATE),
                    "-c:a", "pcm_s16le", str(ziel)], check=True)
    with wave.open(str(ziel)) as f:
        return array.array("h", f.readframes(f.getnframes()))


RAHMEN = 0.01  # 10 ms


def stimmhafte_rahmen(pcm: array.array):
    """Bool-Array je 10-ms-Rahmen: liegt dort Stimme über dem Grundrauschen?"""
    import numpy as np
    x = np.frombuffer(pcm.tobytes(), dtype=np.int16).astype(np.float32)
    n = int(RATE * RAHMEN)
    x = x[: len(x) // n * n].reshape(-1, n)
    rms = np.sqrt((x ** 2).mean(axis=1)) + 1e-6
    boden = np.percentile(rms, 10)
    schwelle = max(boden * 4, 32768 * 10 ** (-55 / 20))  # -55 dBFS: leise Endlaute bleiben drin
    return rms > schwelle


def sprachgrenzen(stimmhaft, von: float, bis: float, w_a: float, w_b: float) -> tuple[float, float]:
    i, j = int(von / RAHMEN), int(bis / RAHMEN)
    idx = [k for k in range(i, min(j, len(stimmhaft))) if stimmhaft[k]]
    if not idx:
        return w_a, w_b
    return idx[0] * RAHMEN, (idx[-1] + 1) * RAHMEN


def blende(stueck: array.array, ms: int = 12) -> array.array:
    n = min(len(stueck) // 2, RATE * ms // 1000)
    for k in range(n):
        f = k / n
        stueck[k] = int(stueck[k] * f)
        stueck[-1 - k] = int(stueck[-1 - k] * f)
    return stueck


PROMPT = "relichat, relilab, relicamp, rpi-virtuell, reliweb, Nostr, reli-hub, OERcamp, Open-Reli, Comenius-Institut."


class Quelle:
    """Eine Aufnahmedatei mit Transkript, PCM und Stimmerkennung."""

    def __init__(self, audio: Path, modell: str, neu: bool, tmp: Path):
        self.audio = audio
        self.name = audio.stem
        cache = BUILD / f"transkript-{self.name}.json"
        alt = BUILD / "transkript.json"  # Zwischenspeicher älterer Läufe
        roh = None
        for c in (cache, alt):
            if not neu and c.exists():
                d = json.loads(c.read_text())
                if d["audio"] == str(audio.resolve()):
                    roh = d["woerter"]
                    print(f"{audio.name}: Transkript aus Zwischenspeicher ({len(roh)} Wörter)")
                    break
        if roh is None:
            print(f"Transkribiere {audio.name} mit Whisper „{modell}“ …")
            roh = transkribieren(audio, modell, PROMPT)
            cache.write_text(json.dumps({"audio": str(audio.resolve()), "modell": modell, "woerter": roh},
                                        ensure_ascii=False, indent=1), encoding="utf-8")
        self.roh = roh
        self.t = [norm(w["w"]) for w in roh]
        self.pcm = lesen_pcm(audio, tmp / f"{self.name}.wav")
        self.laenge = len(self.pcm) / RATE
        self.stimmhaft = stimmhafte_rahmen(self.pcm)


def treffer_anteil(e: dict, q: Quelle, s: int, z: int) -> float:
    u = tokens(e["text"])
    return sum(b.size for b in SequenceMatcher(None, u, q.t[s:z], autojunk=False).get_matching_blocks()) / len(u)


def grenzen(q: Quelle, eintraege: list[tuple[dict, int, int]]) -> dict[str, tuple[float, float]]:
    """Schnittgrenzen (Sekunden in q) für Einheiten aus derselben Quelle, zeitlich geordnet."""
    eintraege = sorted(eintraege, key=lambda x: x[1])
    ergebnis = {}
    links = 0.0
    for i, (e, s, z) in enumerate(eintraege):
        # Whisper-Wortgrenzen sind ungenau (Wörter schlucken Pausen). Darum im Umfeld
        # nach tatsächlicher Stimme suchen, begrenzt durch die Nachbar-Einheiten.
        w_a, w_b = q.roh[s]["start"], q.roh[z - 1]["ende"]
        rechts, n_a = q.laenge, None
        if i + 1 < len(eintraege):
            n_a = q.roh[eintraege[i + 1][1]]["start"]
            rechts = max(w_b, (w_b + n_a) / 2) if n_a > w_b else w_b
        # Hat Whisper die ersten oder letzten Wörter der Einheit nicht erkannt, liegen sie
        # vor bzw. hinter dem gefundenen Fenster: dort weiter nach Stimme suchen.
        bloecke = [bl for bl in SequenceMatcher(None, tokens(e["text"]), q.t[s:z], autojunk=False)
                   .get_matching_blocks() if bl.size]
        vorn = bloecke[0].a if bloecke else 0
        hinten = len(tokens(e["text"])) - (bloecke[-1].a + bloecke[-1].size) if bloecke else 0
        if vorn or hinten:
            print(f"  {e['id']}: {vorn} Wort/Wörter vorn, {hinten} hinten nicht erkannt – suche weiter")
        if hinten and n_a is not None:
            rechts = max(rechts, min(n_a - 0.15, w_b + 0.5 + 0.6 * hinten))
        elif hinten:
            rechts = q.laenge
        a, b = sprachgrenzen(q.stimmhaft, max(links, w_a - 0.5 - 0.6 * vorn),
                             min(rechts, w_b + 0.5 + 0.6 * hinten), w_a, w_b)
        a = max(links, a - RAND_VOR)
        b = min(q.laenge, b + RAND_NACH)
        links = b
        ergebnis[e["id"]] = (a, b)
    return ergebnis


def stimmpegel(q: Quelle, abschnitte: list[tuple[float, float]]) -> float:
    """Mittlerer Pegel (dB) der Stimme in den gewählten Abschnitten."""
    import numpy as np
    x = np.frombuffer(q.pcm.tobytes(), dtype=np.int16).astype(np.float32)
    teile = [x[int(a * RATE):int(b * RATE)] for a, b in abschnitte]
    y = np.concatenate(teile) if teile else x
    n = int(RATE * RAHMEN)
    y = y[: len(y) // n * n].reshape(-1, n)
    rms = np.sqrt((y ** 2).mean(axis=1)) + 1e-6
    laut = rms[rms > np.percentile(rms, 50)]
    return float(20 * np.log10(np.median(laut) / 32768))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio", type=Path, help="Hauptaufnahme")
    ap.add_argument("--nach", type=Path, action="append", default=[],
                    help="Nachaufnahme mit einzelnen neu gesprochenen Einheiten (mehrfach möglich, spätere gewinnen)")
    ap.add_argument("--modell", default="small")
    ap.add_argument("--neu", action="store_true", help="Transkripte neu erzeugen")
    args = ap.parse_args()

    beats = json.loads((BUILD / "beats.json").read_text(encoding="utf-8"))
    einheiten = beats["einheiten"]

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        haupt = Quelle(args.audio, args.modell, args.neu, tmp)
        herkunft: dict[str, tuple[Quelle, int, int]] = {}

        # Nachaufnahmen: jede Einheit, die dort vollständig vorkommt, ersetzt die Hauptaufnahme
        for pfad in args.nach:
            q = Quelle(pfad, args.modell, args.neu, tmp)
            gefunden = []
            for e, w in zip(einheiten, zuordnen(einheiten, q.t, auslassen=0.0)):
                if w and treffer_anteil(e, q, *w) >= 0.75:
                    herkunft[e["id"]] = (q, *w)
                    gefunden.append(e["id"])
            print(f"{pfad.name}: ersetzt {', '.join(gefunden) or 'nichts'}")

        warnungen = []
        for e, w in zip(einheiten, zuordnen(einheiten, haupt.t, ohne=set(herkunft))):
            if e["id"] in herkunft:
                continue
            if w is None:
                warnungen.append(f"{e['id']}: nicht gefunden")
                continue
            if treffer_anteil(e, haupt, *w) < 0.75:
                warnungen.append(f"{e['id']}: nur {treffer_anteil(e, haupt, *w):.0%} der Wörter erkannt – bitte anhören")
            herkunft[e["id"]] = (haupt, *w)

        fehlen = [e["id"] for e in einheiten if e["id"] not in herkunft]
        if fehlen:
            print("\n".join(warnungen))
            sys.exit(f"Abbruch: Diese Einheiten fehlen in allen Aufnahmen: {', '.join(fehlen)}")

        # Schnittgrenzen je Quelle, Pegel der Nachaufnahmen an die Hauptaufnahme angleichen
        quellen = {id(q): q for q, _, _ in herkunft.values()}
        bereich: dict[str, tuple[float, float]] = {}
        for q in quellen.values():
            bereich.update(grenzen(q, [(e, s, z) for e in einheiten
                                       for (qq, s, z) in [herkunft[e["id"]]] if qq is q]))
        pegel = {k: stimmpegel(q, [bereich[e["id"]] for e in einheiten if herkunft[e["id"]][0] is q])
                 for k, q in quellen.items()}
        ziel = pegel[id(haupt)]

        aus = array.array("h", bytes(int(VORLAUF * RATE) * 2))
        timeline = []
        for e in einheiten:
            q, s, z = herkunft[e["id"]]
            a, b = bereich[e["id"]]
            stueck = q.pcm[int(a * RATE):int(b * RATE)]
            if q is not haupt:
                faktor = 10 ** ((ziel - pegel[id(q)]) / 20)
                stueck = array.array("h", (max(-32768, min(32767, int(v * faktor))) for v in stueck))
            versatz = len(aus) / RATE - a
            aus.extend(blende(stueck))
            woerter = [{**w, "start": round(w["start"] + versatz, 3), "ende": round(w["ende"] + versatz, 3)}
                       for w in woerter_zuordnen(e, q.roh, s, z)]
            ende = len(aus) / RATE
            pause = PAUSE_LERNSATZ if e["tag"] == "lernsatz" else PAUSE
            timeline.append({**{k: e[k] for k in ("id", "tag", "szene", "bild", "lernsatz", "text")},
                             "start": round(a + versatz, 3), "sprechende": round(ende, 3),
                             "aufnahme": q.name, "quelle": [round(a, 3), round(b, 3)], "woerter": woerter})
            aus.extend(bytes(int(pause * RATE) * 2))
        aus.extend(bytes(int(NACHLAUF * RATE) * 2))
        # Einheit endet, wenn die nächste beginnt
        for i, e in enumerate(timeline):
            e["ende"] = timeline[i + 1]["start"] if i + 1 < len(timeline) else round(len(aus) / RATE, 3)

        roh_wav = tmp / "geschnitten.wav"
        with wave.open(str(roh_wav), "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(RATE)
            f.writeframes(aus.tobytes())
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(roh_wav), "-af",
                        "highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(RATE), "-ac", "1",
                        str(BUILD / "stimme.wav")], check=True)
        laenge = sum(q.laenge for q in quellen.values())

    dauer = len(aus) / RATE
    szenen = []
    for sz in beats["szenen"]:
        teil = [e for e in timeline if e["szene"] == sz["nr"]]
        if teil:
            szenen.append({**sz, "start": teil[0]["start"], "ende": teil[-1]["ende"]})
    timeline[0]["start"] = 0.0  # erste Einheit ab Bild 1 (Vorlauf gehört ihr)
    (BUILD / "timeline.json").write_text(json.dumps(
        {"audio": "stimme.wav", "dauer": round(dauer, 3), "szenen": szenen, "einheiten": timeline},
        ensure_ascii=False, indent=1), encoding="utf-8")

    for k, q in quellen.items():
        if q is not haupt:
            print(f"  Pegel {q.name}: {pegel[k]:.1f} dB → an Hauptaufnahme ({ziel:.1f} dB) angeglichen")
    print(f"Aufnahmen {laenge:.1f} s → geschnitten {dauer:.1f} s ({dauer / 60:.1f} min), "
          f"{len(timeline)} Einheiten")
    for w in warnungen:
        print("  ⚠", w)


if __name__ == "__main__":
    main()
