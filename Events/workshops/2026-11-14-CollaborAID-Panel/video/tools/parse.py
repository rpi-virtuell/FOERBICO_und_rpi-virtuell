#!/usr/bin/env python3
"""Zerlegt sprechtext.md in Sinneinheiten.

Ausgabe:
  build/beats.json   – Szenen und Sinneinheiten mit Bildregie und Sprechtext
  build/lesetext.html – Lesevorlage für die Aufnahme (großer Text, eine Einheit pro Block)

Aufruf: python3 tools/parse.py [pfad/zu/sprechtext.md] [--nur E19,E21,E22]
  --nur erzeugt zusätzlich build/nachaufnahme.html mit nur diesen Einheiten
"""
import html
import json
import re
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent.parent
ARGS = [a for a in sys.argv[1:] if not a.startswith("--nur")]
NUR = next((a.split("=", 1)[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]
            for a in sys.argv[1:] if a.startswith("--nur")), None)
if NUR:
    ARGS = [a for a in ARGS if a != NUR]
QUELLE = Path(ARGS[0]) if ARGS else HIER.parent / "sprechtext.md"
BUILD = HIER / "build"

PRUEFEN = re.compile(r"\s*\[PRÜFEN:[^\]]*\]")
EINHEIT = re.compile(r"^###\s+(E\d+)\s*·\s*(\S+)")
SZENE = re.compile(r"^##\s+Szene\s+(\d+)\s*·\s*(.+)$")
LERNSATZ = re.compile(r"Lernsatz:\s*„([^“]+)“")


def zerlegen(text: str) -> dict:
    zeilen = text.splitlines()
    # Sprechteil: nach dem ersten '---' bis zum nächsten '---'
    try:
        start = zeilen.index("---") + 1
        ende = zeilen.index("---", start)
    except ValueError:
        sys.exit("Erwarte den Sprechteil zwischen zwei Zeilen '---'.")

    szenen, einheiten = [], []
    szene = None
    aktuell = None

    def abschliessen():
        if aktuell is None:
            return
        sprech = " ".join(" ".join(aktuell["_text"]).split())
        sprech = PRUEFEN.sub("", sprech).strip()
        bild = " ".join(" ".join(aktuell["_bild"]).split())
        lern = LERNSATZ.search(bild)
        einheiten.append({
            "id": aktuell["id"],
            "tag": aktuell["tag"],
            "szene": aktuell["szene"],
            "bild": bild,
            "lernsatz": lern.group(1) if lern else None,
            "text": sprech,
            "woerter": len(sprech.split()),
        })

    for zeile in zeilen[start:ende]:
        if m := SZENE.match(zeile):
            abschliessen()
            aktuell = None
            szene = {"nr": int(m.group(1)), "titel": m.group(2).strip()}
            szenen.append(szene)
        elif m := EINHEIT.match(zeile):
            abschliessen()
            aktuell = {"id": m.group(1), "tag": m.group(2), "szene": szene["nr"] if szene else None,
                       "_bild": [], "_text": []}
        elif aktuell is not None:
            s = zeile.strip()
            if s.startswith(">"):
                inhalt = s.lstrip(">").strip()
                if inhalt.lower().startswith("bild:"):
                    inhalt = inhalt[5:].strip()
                aktuell["_bild"].append(inhalt)
            elif s:
                aktuell["_text"].append(s)
    abschliessen()

    ids = [e["id"] for e in einheiten]
    if len(ids) != len(set(ids)):
        sys.exit(f"Doppelte Einheiten-IDs: {ids}")
    leer = [e["id"] for e in einheiten if not e["text"]]
    if leer:
        sys.exit(f"Einheiten ohne Sprechtext: {leer}")
    return {"quelle": str(QUELLE.name), "szenen": szenen, "einheiten": einheiten}


def lesetext(daten: dict, nur: set | None = None) -> str:
    titel = {s["nr"]: s["titel"] for s in daten["szenen"]}
    bloecke, letzte = [], None
    for e in daten["einheiten"]:
        if nur and e["id"] not in nur:
            continue
        if e["szene"] != letzte:
            bloecke.append(f'<h2>Szene {e["szene"]} · {html.escape(titel.get(e["szene"], ""))}</h2>')
            letzte = e["szene"]
        bloecke.append(
            f'<section><span class="id">{e["id"]}</span><p>{html.escape(e["text"])}</p></section>'
        )
    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><title>Lesetext</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body {{ font: 34px/1.5 Georgia, serif; max-width: 34em; margin: 2em auto; padding: 0 1em;
         background: #f6f1e7; color: #222; }}
  h2 {{ font-size: 20px; color: #8a7f6a; text-transform: uppercase; letter-spacing: .08em;
        margin-top: 3em; }}
  section {{ margin: 0 0 1.6em; position: relative; }}
  .id {{ position: absolute; left: -3.2em; top: .5em; font: 16px monospace; color: #b0a58f; }}
  p {{ margin: 0; }}
  p::after {{ content: " ⏸"; color: #c9bfa9; font-size: .6em; }}
</style></head><body>
<p style="font-size:20px;color:#8a7f6a">Nach jedem Absatz kurz Luft holen (⏸ ≈ 1 Sekunde).
Bei einem Versprecher: den ganzen Absatz noch einmal sprechen. Das Skript nimmt die letzte Fassung.</p>
{chr(10).join(bloecke)}
</body></html>
"""


def main():
    daten = zerlegen(QUELLE.read_text(encoding="utf-8"))
    BUILD.mkdir(exist_ok=True)
    (BUILD / "beats.json").write_text(json.dumps(daten, ensure_ascii=False, indent=2), encoding="utf-8")
    (BUILD / "lesetext.html").write_text(lesetext(daten), encoding="utf-8")
    if NUR:
        ids = set(NUR.split(","))
        (BUILD / "nachaufnahme.html").write_text(lesetext(daten, ids), encoding="utf-8")
        print(f"Nachaufnahme-Vorlage: build/nachaufnahme.html ({len(ids)} Einheiten)")
    woerter = sum(e["woerter"] for e in daten["einheiten"])
    print(f"{len(daten['einheiten'])} Einheiten in {len(daten['szenen'])} Szenen, {woerter} Wörter "
          f"(≈ {woerter / 120:.1f} min bei 120 W/min)")


if __name__ == "__main__":
    main()
