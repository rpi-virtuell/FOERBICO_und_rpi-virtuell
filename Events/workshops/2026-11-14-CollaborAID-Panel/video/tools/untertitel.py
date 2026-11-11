#!/usr/bin/env python3
"""Erzeugt aus build/timeline.json Untertitel (WebVTT) und eine Kapitelliste.

Die Untertitel nehmen den Wortlaut aus dem Sprechtext und die Zeiten aus der
Ausrichtung. Lange Sätze werden an Satzzeichen geteilt (höchstens zwei Zeilen à 42 Zeichen).

Ausgabe (im Ordner ../veroeffentlichung/):
  untertitel.de.vtt  – für Vimeo, YouTube, Moodle …
  untertitel.de.srt  – dieselben Untertitel als SubRip, z. B. für Schnittprogramme
  kapitel.txt        – Zeitmarken je Szene, z. B. für die Videobeschreibung

Aufruf: python3 tools/untertitel.py
"""
import json
import re
from pathlib import Path

HIER = Path(__file__).resolve().parent.parent
ZIEL = HIER.parent / "veroeffentlichung"
MAX = 84  # Zeichen pro Untertitel (zwei Zeilen)


def zeit(s: float) -> str:
    h, rest = divmod(max(0.0, s), 3600)
    m, sek = divmod(rest, 60)
    return f"{int(h):02d}:{int(m):02d}:{sek:06.3f}"


def kurz(s: float) -> str:
    m, sek = divmod(int(s), 60)
    return f"{m}:{sek:02d}"


def stuecke(woerter: list[dict]) -> list[list[dict]]:
    """Wörter zu Untertiteln bündeln: an Satzenden, bei Überlänge an Kommas."""
    saetze, aktuell = [], []
    for w in woerter:
        aktuell.append(w)
        if re.search(r"[.?!:]$", w["w"]):
            saetze.append(aktuell)
            aktuell = []
    if aktuell:
        saetze.append(aktuell)
    ergebnis = []
    for satz in saetze:
        while len(" ".join(w["w"] for w in satz)) > MAX:
            schnitt = 0
            for i, w in enumerate(satz[:-1]):
                if len(" ".join(x["w"] for x in satz[: i + 1])) > MAX:
                    break
                if w["w"].endswith(",") or i > len(satz) // 2 and not schnitt:
                    schnitt = i + 1
            schnitt = schnitt or len(satz) // 2
            ergebnis.append(satz[:schnitt])
            satz = satz[schnitt:]
        ergebnis.append(satz)
    return ergebnis


def umbruch(text: str) -> str:
    if len(text) <= 42:
        return text
    mitte = len(text) // 2
    links, rechts = text.rfind(" ", 0, mitte + 1), text.find(" ", mitte)
    pos = links if rechts < 0 or (links >= 0 and mitte - links <= rechts - mitte) else rechts
    return text[:pos] + "\n" + text[pos + 1:]


def main():
    tl = json.loads((HIER / "build" / "timeline.json").read_text(encoding="utf-8"))
    ZIEL.mkdir(exist_ok=True)
    cues = []
    for e in tl["einheiten"]:
        for st in stuecke(e["woerter"]):
            cues.append([st[0]["start"], st[-1]["ende"] + 0.25, " ".join(w["w"] for w in st)])
    for a, b in zip(cues, cues[1:]):  # keine Überlappung
        a[1] = min(a[1], b[0] - 0.04)
    vtt = ["WEBVTT", ""]
    for k, (a, b, text) in enumerate(cues, 1):
        vtt += [str(k), f"{zeit(a)} --> {zeit(b)}", umbruch(text), ""]
    (ZIEL / "untertitel.de.vtt").write_text("\n".join(vtt), encoding="utf-8")
    srt = []
    for k, (a, b, text) in enumerate(cues, 1):
        srt += [str(k), f"{zeit(a).replace('.', ',')} --> {zeit(b).replace('.', ',')}", umbruch(text), ""]
    (ZIEL / "untertitel.de.srt").write_text("\n".join(srt), encoding="utf-8")

    kapitel = [f"{kurz(0 if sz['nr'] == 0 else sz['start'])} {sz['titel']}" for sz in tl["szenen"]]
    (ZIEL / "kapitel.txt").write_text("\n".join(kapitel) + "\n", encoding="utf-8")
    print(f"{len(cues)} Untertitel, {len(kapitel)} Kapitel, Dauer {kurz(tl['dauer'])}")


if __name__ == "__main__":
    main()
