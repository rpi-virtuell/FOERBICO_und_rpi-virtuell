# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["faster-whisper>=1.1", "numpy"]
# ///
"""Prüft die geschnittene Tonspur: build/stimme.wav wird neu erkannt und je Einheit
mit dem Sprechtext verglichen. Gemeldet werden fehlende Anfangs- oder Endwörter
(abgeschnitten?) und zusätzliche Wörter (Versprecher, doppelte Passagen).

Aufruf: uv run tools/pruefen.py [--modell medium]
"""
import argparse
import json
import re
import subprocess
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel

HIER = Path(__file__).resolve().parent.parent
BUILD = HIER / "build"


def norm(w: str) -> str:
    return re.sub(r"[^\w]", "", unicodedata.normalize("NFC", w.lower()).replace("ß", "ss"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modell", default="medium")
    args = ap.parse_args()
    tl = json.loads((BUILD / "timeline.json").read_text(encoding="utf-8"))
    pcm = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(BUILD / tl["audio"]), "-ac", "1", "-ar", "16000",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    m = WhisperModel(args.modell, device="cpu", compute_type="int8")
    prompt = "relichat, relilab, relicamp, rpi-virtuell, reliweb, Nostr, reli-hub, OERcamp, Open-Reli."
    seg, _ = m.transcribe(np.frombuffer(pcm, np.float32), language="de", word_timestamps=True,
                          initial_prompt=prompt, vad_filter=False)
    woerter = [w for s in seg for w in (s.words or [])]
    auffaellig = 0
    for e in tl["einheiten"]:
        mitte = [w for w in woerter if e["start"] - 0.1 <= (w.start + w.end) / 2 <= e["ende"]]
        erk = [norm(w.word) for w in mitte]
        soll = [norm(w) for w in e["text"].split()]
        sm = SequenceMatcher(None, soll, erk, autojunk=False)
        treffer = sum(b.size for b in sm.get_matching_blocks())
        hinweise = []
        bloecke = [b for b in sm.get_matching_blocks() if b.size]
        if bloecke and bloecke[0].a > 1:
            hinweise.append(f"Anfang fehlt? ({' '.join(e['text'].split()[:bloecke[0].a])})")
        if bloecke and bloecke[-1].a + bloecke[-1].size < len(soll) - 1:
            hinweise.append(f"Ende fehlt? ({' '.join(e['text'].split()[bloecke[-1].a + bloecke[-1].size:])})")
        if len(erk) - treffer > max(4, len(soll) * 0.35):
            hinweise.append(f"{len(erk) - treffer} Wörter zusätzlich")
        if hinweise:
            auffaellig += 1
            print(f"{e['id']} ({treffer}/{len(soll)}): " + "; ".join(hinweise))
            print("   gehört:", " ".join(w.word.strip() for w in mitte))
    print(f"{auffaellig} von {len(tl['einheiten'])} Einheiten auffällig")


if __name__ == "__main__":
    main()
