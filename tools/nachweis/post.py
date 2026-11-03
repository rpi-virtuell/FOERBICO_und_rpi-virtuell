#!/usr/bin/env python3
"""Legt die Nachweis-Issues aus Orga/nachweis-hub in Forgejo an und verknüpft sie.

  python3 -I tools/nachweis/post.py --dry          zeigt die Aufrufe
  python3 -I tools/nachweis/post.py --run          legt Label und Issues an, schreibt ergebnis.json
  python3 -I tools/nachweis/post.py --verknuepfe   ersetzt Platzhalter durch URLs, kommentiert bestehende Issues
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check  # noqa: E402

API = "https://git.rpi-virtuell.de/api/v1"
REPO = "Comenius-Institut/FOERBICO_und_rpi-virtuell"
ISSUE_URL = f"https://git.rpi-virtuell.de/{REPO}/issues/"
LABEL_NAME = "Nachweis"
LABEL_FARBE = "#1B3892"
ORDNER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Orga", "nachweis-hub")
ERGEBNIS = os.path.join(ORDNER, "ergebnis.json")
PLATZHALTER = re.compile(r"\{\{nachweis:([0-9a-z-]+)\}\}")

# bestehende Issues → Entwurf, in dem sie Beleg sind
BELEGE = {844: "04-ap-4-5", 845: "01-ap-3-2-3-3", 843: "03-ap-4-3-4-4", 842: "11-ap-9-2",
          199: "01-ap-3-2-3-3", 696: "09-ap-6-3", 700: "01-ap-3-2-3-3", 789: "13-ap-9-5", 276: "10-ap-9-1"}
MEILENSTEIN_NACHTRAG = {789: 16}
SCHLIESSEN = {276: ("Die Bedarfserhebung läuft über die gitworkshop-Fäden, die Rückmeldungen der "
                    "Zwischenfazit-Tagung und Beobachtungen; Beleg im Nachweis-Issue {url}.")}
KOMMENTAR = "Dieses Issue ist Beleg im Nachweis-Issue {url} (Hub als Nachweis der Antragszusagen)."


def label_id(name, labels):
    for l in labels:
        if l.get("name") == name:
            return l["id"]
    return None


def ersetze_verweise(body, mapping):
    def ersatz(m):
        return mapping.get(m.group(1), m.group(0))
    return PLATZHALTER.sub(ersatz, body)


def zu_ueberspringen(datei, ergebnis):
    return datei in ergebnis and "number" in ergebnis[datei]


class Forgejo:
    def __init__(self, dry):
        self.dry = dry
        self.h = {"Content-Type": "application/json"}
        if not dry:
            self.h["Authorization"] = "token " + open(os.path.expanduser("~/.config/forgejo/token.txt")).read().strip()

    def call(self, methode, pfad, body=None):
        url = f"{API}/repos/{REPO}{pfad}"
        daten = json.dumps(body).encode() if body is not None else None
        if self.dry:
            print(f"  [dry] {methode} {url}" + (f" ({len(daten)} Bytes)" if daten else ""))
            return {"number": 0, "html_url": ISSUE_URL + "0", "id": 0}
        req = urllib.request.Request(url, data=daten, headers=self.h, method=methode)
        try:
            with urllib.request.urlopen(req) as r:
                return json.loads(r.read().decode(), strict=False)
        except urllib.error.HTTPError as e:
            print("FEHLER", e.code, e.read().decode()[:300])
            raise

    def labels(self):
        if self.dry:
            return []
        return self.call("GET", "/labels?limit=100")


def lade_ergebnis():
    return json.load(open(ERGEBNIS, encoding="utf-8")) if os.path.exists(ERGEBNIS) else {}


def speichere_ergebnis(e):
    json.dump(e, open(ERGEBNIS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def entwuerfe():
    for datei, text in check.entwuerfe(ORDNER):
        if datei.endswith(".md") and "-ap-" in datei:
            yield datei[:-3], check.parse_entwurf(text)


def anlegen(fg, ergebnis):
    labels = fg.labels()
    nid = label_id(LABEL_NAME, labels)
    if nid is None:
        j = fg.call("POST", "/labels", {"name": LABEL_NAME, "color": LABEL_FARBE,
                                        "description": "Nachweis der Antragszusagen je Meilenstein"})
        nid = j["id"]
        labels = labels + [{"id": nid, "name": LABEL_NAME}]
    for datei, e in entwuerfe():
        if zu_ueberspringen(datei, ergebnis):
            print(f"  übersprungen {datei} (#{ergebnis[datei]['number']})")
            continue
        ids = []
        for name in e["labels"]:
            lid = label_id(name, labels)
            if lid is None and not fg.dry:
                print(f"  Warnung: Label {name!r} unbekannt, ausgelassen ({datei})")
            elif lid is not None:
                ids.append(lid)
        j = fg.call("POST", "/issues", {"title": e["titel"], "body": e["body"],
                                        "milestone": e["meilenstein"], "labels": ids})
        ergebnis[datei] = {"number": j["number"], "url": j.get("html_url") or ISSUE_URL + str(j["number"])}
        print(f"  #{j['number']}  {e['titel'][:90]}")
        if not fg.dry:
            speichere_ergebnis(ergebnis)
    return ergebnis


def verknuepfen(fg, ergebnis):
    mapping = {d: v["url"] for d, v in ergebnis.items() if "url" in v}
    offen = []
    for datei, e in entwuerfe():
        if datei not in mapping:
            print(f"  fehlt in ergebnis.json: {datei}")
            continue
        body = ersetze_verweise(e["body"], mapping)
        offen += PLATZHALTER.findall(body)
        if ergebnis[datei].get("gepatcht"):
            continue
        fg.call("PATCH", f"/issues/{ergebnis[datei]['number']}", {"body": body})
        ergebnis[datei]["gepatcht"] = True
    print(f"  {sum(1 for v in ergebnis.values() if v.get('gepatcht'))} Bodies gepatcht; unaufgelöst: {sorted(set(offen)) or 'keine'}")
    kommentare = ergebnis.setdefault("_kommentare", {})
    for nr, datei in BELEGE.items():
        if str(nr) in kommentare or datei not in mapping:
            continue
        url = mapping[datei]
        if nr in SCHLIESSEN:
            fg.call("POST", f"/issues/{nr}/comments", {"body": SCHLIESSEN[nr].format(url=url)})
            fg.call("PATCH", f"/issues/{nr}", {"state": "closed"})
        else:
            fg.call("POST", f"/issues/{nr}/comments", {"body": KOMMENTAR.format(url=url)})
        if nr in MEILENSTEIN_NACHTRAG:
            fg.call("PATCH", f"/issues/{nr}", {"milestone": MEILENSTEIN_NACHTRAG[nr]})
        kommentare[str(nr)] = datei
    print(f"  {len(kommentare)} Kommentare, {len(MEILENSTEIN_NACHTRAG)} Meilenstein gesetzt, {len(SCHLIESSEN)} Issue geschlossen")
    if not fg.dry:
        speichere_ergebnis(ergebnis)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry", action="store_true")
    g.add_argument("--run", action="store_true")
    g.add_argument("--verknuepfe", action="store_true")
    a = ap.parse_args(argv)
    ergebnis = lade_ergebnis()
    if a.verknuepfe:
        verknuepfen(Forgejo(False), ergebnis)
    else:
        anlegen(Forgejo(a.dry), ergebnis)
    return 0


if __name__ == "__main__":
    sys.exit(main())
