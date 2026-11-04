#!/usr/bin/env python3
"""Ersetzt Platzhalter in einem Issue- oder Kommentar-Entwurf durch URLs und IDs.

  python3 -I ersetze-platzhalter.py <entwurf.md> <tabellen.json>

tabellen.json: {"issue": {"01": "<url>"}, "r3": {"06": "<url>"}, "r2": {"09": "<url>"},
                "r3id": {"06": "<event-id>"}, "r2id": {"09": "<event-id>"}}
Schreibt <entwurf>.fertig.md; unaufgelöste Platzhalter werden gemeldet, Exit 1."""
import json
import re
import sys

MUSTER = re.compile(r"\{\{(issue|r3|r2|r3id|r2id):([0-9]{2})\}\}")


def ersetze(text: str, tabellen: dict):
    offen = []

    def ersatz(m):
        wert = tabellen.get(m.group(1), {}).get(m.group(2))
        if wert is None:
            offen.append(m.group(0))
            return m.group(0)
        return wert
    return MUSTER.sub(ersatz, text), offen


def main(argv):
    if len(argv) != 3:
        sys.exit(__doc__)
    text = open(argv[1], encoding="utf-8").read()
    tabellen = json.load(open(argv[2], encoding="utf-8"))
    neu, offen = ersetze(text, tabellen)
    ziel = argv[1][:-3] + ".fertig.md"
    open(ziel, "w", encoding="utf-8").write(neu)
    print(ziel, "| unaufgelöst:", offen or "keine")
    return 1 if offen else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
