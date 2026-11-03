# Nachweis-Hub: Nachweis-Issues je Hub-Meilenstein

Entwürfe der Nachweis-Issues, mit denen der reli_hub als Realisierung der Antragszusagen belegt wird (Gesamtkonzeption `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md`, Abschnitt 6). Je Hub-Meilenstein ein offenes Issue mit Label `Nachweis`: Zusage im Wortlaut des Antrags, Ort im Hub, Checkliste, Belege, Abweichungen, Verweise. Meilensteine bleiben offen; die Nachweis-Issues sind die Kapitel des Abschlussberichts.

Format je Datei: Kopfzeilen `TITEL:`, `MEILENSTEIN: <Forgejo-ID>`, `LABELS: Nachweis, …`, Leerzeile, Text. Querverweise als `{{nachweis:<dateiname-ohne-md>}}`; `tools/nachweis/post.py` ersetzt sie nach dem Anlegen durch die Issue-URLs und trägt die Nummern in `ergebnis.json` ein.

| Datei | Meilenstein (ID) | Zeilen der Konzeption |
|---|---|---|
| 01-ap-3-2-3-3 | AP 3-2 + 3-3 Konzept und Einsatz Community-Hub (83) | 4.1, 4.2, 4.15, 4.18, 4.20 |
| 02-ap-4-2 | AP 4-2 Metadatenstandards (88) | 4.3 |
| 03-ap-4-3-4-4 | AP 4-3 + 4-4 Metadaten-Generator (90) | 4.4 |
| 04-ap-4-5 | AP 4-5 OER-Client (99) | 4.5 |
| 05-ap-4-6 | AP 4-6 Dezentrale OER-Kataloge (115) | 4.6 |
| 06-ap-4-7 | AP 4-7 Weitere Communities (101) | 4.7 |
| 07-ap-5-1 | AP 5-1 Bedarfe (89) | 4.8, 4.17 |
| 08-ap-5-2 | AP 5-2 Unterstützung (97) | 4.8 |
| 09-ap-6-3 | AP 6-3 ALPIKA-Institute (100) | 4.9 |
| 10-ap-9-1 | AP 9-1 Technische Bedarfe (87) | 4.17 |
| 11-ap-9-2 | AP 9-2 Technische Infrastruktur (8) | 4.11 |
| 12-ap-9-4 | AP 9-4 Materialpool-Metadaten (118) | 4.12 |
| 13-ap-9-5 | AP 9-5 Profildienst (16) | 4.10 |
| 14-ap-2-4 | AP 2-4 Community-Management (121) | 4.8, 4.10, 4.19 |
| 15-ap-3 | AP 3 Vernetzung + Kommunikation (7), Nachtrag zu M35 | 4.19, 4.16 |

Prüfung: `python3 -I tools/nachweis/check.py forgejo Orga/nachweis-hub --issues Orga/nachweis-hub/issues-snapshot.jsonl` (Schnappschuss der Issues vom 03.11.2026, 638 Einträge).

Stand: Entwürfe vom 03.11.2026, zum Gegenlesen; noch nicht in Forgejo angelegt.
