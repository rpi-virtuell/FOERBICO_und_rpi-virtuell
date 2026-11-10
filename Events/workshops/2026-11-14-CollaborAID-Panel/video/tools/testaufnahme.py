#!/usr/bin/env python3
"""Erzeugt eine Testaufnahme mit der macOS-Stimme „Anna“, um die Pipeline ohne echte
Aufnahme durchzuprobieren. Simuliert dabei einen Versprecher mit Wiederholung (E07)
und eine zu lange Pause (nach E20).

Ausgabe: aufnahme/test-anna.wav
Aufruf:  python3 tools/testaufnahme.py
"""
import json
import subprocess
import tempfile
from pathlib import Path

HIER = Path(__file__).resolve().parent.parent
BEATS = json.loads((HIER / "build" / "beats.json").read_text(encoding="utf-8"))
ZIEL = HIER / "aufnahme" / "test-anna.wav"


def sprich(text: str, datei: Path):
    subprocess.run(["say", "-v", "Anna", "-r", "175", "-o", str(datei), "--file-format=WAVE", "--data-format=LEI16@24000", text],
                   check=True)


def stille(sek: float, datei: Path):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                    f"anullsrc=r=24000:cl=mono", "-t", str(sek), "-c:a", "pcm_s16le", str(datei)], check=True)


def main():
    ZIEL.parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        teile = []
        stille(1.5, tmp / "start.wav")
        teile.append(tmp / "start.wav")
        for i, e in enumerate(BEATS["einheiten"]):
            if e["id"] == "E07":  # Versprecher: halber Satz, abgebrochen, dann neu
                halb = " ".join(e["text"].split()[:7])
                sprich(halb + " ähm, nein.", tmp / f"{i:02d}a.wav")
                teile.append(tmp / f"{i:02d}a.wav")
                stille(0.8, tmp / f"{i:02d}p.wav")
                teile.append(tmp / f"{i:02d}p.wav")
            sprich(e["text"], tmp / f"{i:02d}.wav")
            teile.append(tmp / f"{i:02d}.wav")
            pause = 3.5 if e["id"] == "E20" else 1.0
            stille(pause, tmp / f"{i:02d}s.wav")
            teile.append(tmp / f"{i:02d}s.wav")
        liste = tmp / "liste.txt"
        liste.write_text("".join(f"file '{p}'\n" for p in teile))
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(liste),
                        "-ar", "24000", "-ac", "1", "-c:a", "pcm_s16le", str(ZIEL)], check=True)
    dauer = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                            str(ZIEL)], capture_output=True, text=True).stdout.strip()
    print(f"{ZIEL.relative_to(HIER)}: {float(dauer):.1f} s")


if __name__ == "__main__":
    main()
