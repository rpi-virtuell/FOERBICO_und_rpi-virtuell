#!/usr/bin/env python3
"""Prüft Entwürfe für Forgejo (Nachweis-Issues), gitworkshop (Hub-Issues) und den
Erschließungs-Layer: keine Vornamen von Partnern, keine Projektsprache in Hub-Texten,
keine toten Issue-Verweise, keine abgeschnittenen nevent-Links, keine Entwürfe unter
Website/content. Aufruf: siehe README.md."""
import argparse
import json
import os
import re
import sys

NAMEN_DATEI = "~/.config/nachweis/namen.txt"
PROJEKTSPRACHE = re.compile(r"\bAP ?\d|\bM ?\d{1,2}\b|Meilenstein|Arbeitspaket|Förderkennzeichen|01PO23012")
ISSUE_NR = re.compile(r"#(\d{1,5})\b")
NEVENT = re.compile(r"nevent1[0-9a-z]*")
KOPF = re.compile(r"^(TITEL|MEILENSTEIN|LABELS?|ID|ZIEL):\s*(.*)$")


def lade_namen(pfad: str = NAMEN_DATEI):
    """Gibt (vornamen, erlaubte_vollnamen) zurück; Zeilen mit Leerzeichen sind Vollnamen."""
    p = os.path.expanduser(pfad)
    if not os.path.exists(p):
        sys.exit(f"Namensdatei fehlt: {p} (eine Zeile je Vorname; 'Vorname Nachname' = erlaubt)")
    vornamen, erlaubt = [], []
    for zeile in open(p, encoding="utf-8"):
        z = zeile.strip()
        if not z or z.startswith("#"):
            continue
        (erlaubt if " " in z else vornamen).append(z)
    return tuple(vornamen), tuple(erlaubt)


def find_namen(text: str, namen, erlaubt=()) -> list:
    for voll in erlaubt:
        text = text.replace(voll, " ")
    treffer = []
    for name in namen:
        treffer += [(m.start(), m.group(0)) for m in re.finditer(r"\b" + re.escape(name) + r"\w*", text)]
    return [t for _, t in sorted(treffer)]


def find_projektsprache(text: str) -> list:
    return [m.group(0) for m in PROJEKTSPRACHE.finditer(text)]


def find_tote_verweise(text: str, vorhandene) -> list:
    return [int(n) for n in ISSUE_NR.findall(text) if int(n) not in vorhandene]


def find_kurze_nevents(text: str) -> list:
    return [m.group(0) for m in NEVENT.finditer(text) if len(m.group(0)) < 67]


def pfad_erlaubt(pfad: str) -> bool:
    return "Website/content" not in pfad.replace("\\", "/")


def parse_entwurf(text: str) -> dict:
    e = {"titel": None, "meilenstein": None, "labels": [], "id": None, "body": ""}
    zeilen = text.splitlines()
    i = 0
    while i < len(zeilen):
        m = KOPF.match(zeilen[i])
        if not m:
            break
        k, v = m.group(1), m.group(2).strip()
        if k == "TITEL":
            e["titel"] = v
        elif k == "MEILENSTEIN":
            e["meilenstein"] = int(v)
        elif k in ("LABEL", "LABELS"):
            e["labels"] = [x.strip() for x in v.split(",") if x.strip()]
        elif k == "ID":
            e["id"] = v
        elif k == "ZIEL":
            e["titel"] = v
        i += 1
    while i < len(zeilen) and zeilen[i].strip() == "":
        i += 1
    e["body"] = "\n".join(zeilen[i:]).strip()
    return e


def entwuerfe(ordner: str):
    dateien = sorted(f for f in os.listdir(ordner) if f.endswith(".md") and not f.startswith("README"))
    return [(f, open(os.path.join(ordner, f), encoding="utf-8").read()) for f in dateien]


def pruefe(art: str, ordner: str, issues: str | None) -> list:
    befunde = []
    if art == "erschliessung" and not pfad_erlaubt(os.path.abspath(ordner)):
        return [f"{ordner}: pfad: Entwürfe dürfen nicht unter Website/content liegen"]
    vornamen, erlaubt = lade_namen()
    liste = entwuerfe(ordner)
    if not liste:
        return [f"{ordner}: leer: keine Entwürfe gefunden"]
    vorhandene = set()
    if issues:
        for zeile in open(issues, encoding="utf-8"):
            if zeile.strip():
                vorhandene.add(json.loads(zeile)["n"])
    for datei, text in liste:
        for n in find_namen(text, vornamen, erlaubt):
            befunde.append(f"{datei}: name: {n}")
        if art == "gitworkshop":
            for p in find_projektsprache(text):
                befunde.append(f"{datei}: projektsprache: {p}")
            e = parse_entwurf(text)
            if not e["titel"]:
                befunde.append(f"{datei}: kopf: TITEL/ZIEL fehlt")
        if art == "forgejo":
            e = parse_entwurf(text)
            if not e["titel"] or e["meilenstein"] is None or "Nachweis" not in e["labels"]:
                befunde.append(f"{datei}: kopf: TITEL, MEILENSTEIN oder Label Nachweis fehlt")
            if vorhandene:
                for n in find_tote_verweise(text, vorhandene):
                    befunde.append(f"{datei}: verweis: #{n} existiert nicht")
        for nv in find_kurze_nevents(text):
            befunde.append(f"{datei}: nevent: abgeschnitten {nv}")
    return befunde


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("art", choices=["forgejo", "gitworkshop", "erschliessung"])
    ap.add_argument("ordner")
    ap.add_argument("--issues", help="JSONL-Schnappschuss mit Feld n (Issue-Nummer)")
    a = ap.parse_args(argv)
    befunde = pruefe(a.art, a.ordner, a.issues)
    for b in befunde:
        print(b)
    print(f"{len(befunde)} Befunde" if befunde else "ohne Befund")
    return 1 if befunde else 0


if __name__ == "__main__":
    sys.exit(main())
