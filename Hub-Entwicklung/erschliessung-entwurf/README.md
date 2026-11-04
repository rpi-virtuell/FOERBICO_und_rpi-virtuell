# Erschließungs-Layer: Entwurf der Seiten

Arbeitstitel „Erschließungs-Layer", Seitentitel vorläufig „Vom Antrag zum Hub" (Titel offen, Entscheidung Jörg). Ein eigenes Schaufenster im reli_hub für den Fördermittelgeber: die sechs Arbeitsziele des Antrags als Gliederung, darunter die Zusagen mit ihrem Ort im Hub und ihren Belegen. Grundlage: Gesamtkonzeption `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md`, Abschnitt 5 und Matrix 4.1 bis 4.20.

Diese Dateien sind Entwürfe. Zielpfad nach Freigabe: `Website/content/de/erschliessung/<slug>/index.md` im Seitenformat von `Website/content/de/qualitaet/index.md`; von dort gehen sie den normalen Weg über die Sync-Pipeline als `kind:30023`-Seiten vom FOERBICO-Schlüssel auf das Relay. Solange sie hier liegen, baut Hugo sie nicht und die Pipeline veröffentlicht sie nicht.

Platzhalter `{{nachweis:<datei>}}` stehen für die URLs der Nachweis-Issues (werden nach dem Anlegen aus `Orga/nachweis-hub/ergebnis.json` ersetzt). Stufen: A = beim Launch echt, B = beim Launch echt oder gekennzeichneter Nachbau, C = nach dem Launch; Einträge der Stufen B und C tragen „in Arbeit, Stand 2026-11-04".

| Datei | Arbeitsziel | Zusagen (Zeilen der Konzeption) |
|---|---|---|
| 00-einleitung | Einleitung | |
| az-1 | AZ 1 Potenzial bestehender Communities ausschöpfen | 4.7, 4.8, 4.20 |
| az-2 | AZ 2 Koordinierte Zusammenarbeit der Netzwerke | 4.1, 4.6, 4.11, 4.16, 4.17, 4.19 |
| az-3 | AZ 3 Qualitätssicherung und -entwicklung | 4.2, 4.3, 4.12, 4.13 |
| az-4 | AZ 4 OER/OEP-Netzwerke in Hochschulen | 4.14 |
| az-5 | AZ 5 Professionalisierung von Fachkräften und Institutionen | 4.4, 4.9, 4.10 |
| az-6 | AZ 6 Community-übergreifende Redaktion und Qualitätssicherung | 4.5, 4.15, 4.18 |
| 99-schluss | Was über den Antrag hinausging, was anders kam | |

Prüfung: `python3 -I tools/nachweis/check.py erschliessung Hub-Entwicklung/erschliessung-entwurf`.
