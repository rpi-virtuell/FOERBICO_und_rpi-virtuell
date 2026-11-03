# Nachweis-Werkzeug

Prüft und veröffentlicht die Texte, mit denen der Hub als Nachweis der Antragszusagen belegt wird: Nachweis-Issues in Forgejo (Projektsprache erlaubt), Hub-Issues auf gitworkshop (Hub-Sprache, keine Arbeitspakete, Meilensteine oder Förderkennzeichen) und die Entwürfe des Erschließungs-Layers. Gemeinsame Regel aller drei: keine Vornamen von Partnern in Dateien des offenen Repos. Die Namensliste liegt deshalb außerhalb des Repos in `~/.config/nachweis/namen.txt` (eine Zeile je Vorname; eine Zeile mit Leerzeichen ist ein erlaubter Vollname).

Aufrufe, jeweils aus der Repo-Wurzel:

```bash
python3 -I tools/nachweis/check.py forgejo Orga/nachweis-hub --issues Orga/nachweis-hub/issues-snapshot.jsonl
python3 -I tools/nachweis/check.py gitworkshop <ordner-mit-entwuerfen>
python3 -I tools/nachweis/check.py erschliessung Hub-Entwicklung/erschliessung-entwurf
python3 -I tools/nachweis/test_check.py
```

Exit 0 ohne Befund, Exit 1 mit einer Befundliste `datei: art: treffer`. Geprüft werden Namen (auch gebeugt), Projektsprache (nur gitworkshop), tote Issue-Verweise `#NNN` gegen den Schnappschuss (nur forgejo), abgeschnittene `nevent1…`-Links und der Pfad (erschliessung: nie unter `Website/content`).

Entwurfsformat: Kopfzeilen am Dateianfang, dann eine Leerzeile, dann der Text. Forgejo: `TITEL:`, `MEILENSTEIN: <id>`, `LABELS: Nachweis, …`. gitworkshop-Issue: `TITEL:`, `LABEL: a, b`. gitworkshop-Kommentar: `ZIEL:`, `ID: <event-id>`. Querverweise zwischen Nachweis-Entwürfen als `{{nachweis:<dateiname-ohne-md>}}`; `post.py` ersetzt sie nach dem Anlegen durch die Issue-URLs.

Die Tests laufen mit `python3 -I`, deshalb trägt jede Testdatei ihren Ordner selbst in den Suchpfad ein.
