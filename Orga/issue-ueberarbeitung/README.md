# Issue-Überarbeitung 2026

Arbeitsbranch `issue-ueberarbeitung`. Hier liegen die Fassungen zum Gegenlesen und die Skripte, mit denen die Issues in den beiden Forgejo-Repos angelegt, zugeordnet und kommentiert werden. Der Branch muss nicht nach `main`: Issues laufen unabhängig von Branches.

## Fassungen

| Datei | Inhalt | Stand |
|---|---|---|
| [issue-entwuerfe-2026-09-16.md](issue-entwuerfe-2026-09-16.md) | Statusberichte 02.–16.09.2026 als Issues | umgesetzt, siehe Nummern unten |
| [issue-aufraeumen-2026-09-16.md](issue-aufraeumen-2026-09-16.md) | Aufräumen aller 213 offenen Issues: Cluster, Aktion je Issue, Kommentartexte, Pull Requests | zum Gegenlesen; Abschnitte S1, S2, S5 durch die dritte Fassung überholt |
| [issues-fuer-abschlussbericht-2026-09-16.md](issues-fuer-abschlussbericht-2026-09-16.md) | Nachweislogik für den Abschlussbericht: Deliverable-Matrix je Arbeitspaket, Abweichungen vom Antrag, Zuordnungstabelle, Doku-Issues, Muster Nachweis-Issue | zum Gegenlesen |

Buchstaben der ersten Fassung und die angelegten Issues:

| Buchstabe | Issue | Repo |
|---|---|---|
| A | [#840](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/840) Bildnachweise als Standard | offen |
| B | [#841](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/841) Bildmigration | offen |
| C | [#842](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/842) Nostr-Sync | offen |
| D | [#843](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/843) Redaktionswerkzeuge | offen |
| E1 | [#844](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/844) Hub Detailansicht | offen |
| E2 | [#845](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/845) oer.community aus Nostr | offen |
| F | [#846](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/846) Abstimmung mit edufeed | offen |
| G | [#847](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/847) Blogbeitrag KI im RU | offen |
| A' | [#191](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/191) kommentiert und geschlossen | offen |
| H | [#183](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/issues/183) Genehmigungen RPI Karlsruhe (geschlossen zur Doku) | geschlossenes Repo |
| I | [#184](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/issues/184) Bildmigration Team (geschlossen zur Doku) | geschlossenes Repo |
| J | [#185](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/issues/185) Klarnamen in Bildnachweisen | geschlossenes Repo |
| K | [#186](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/issues/186) Signatur-Infrastruktur | geschlossenes Repo |
| M | [#187](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/issues/187) Betrieb oer-community | geschlossenes Repo |
| L | gestrichen | |

## Skripte

- [`skripte/post_issues.py`](skripte/post_issues.py): legt Issues an, trägt Querverweise nach, schließt. Vorlage der Aktion vom 16.09.2026. Liest das Token aus `~/.config/forgejo/token.txt`; kein Token im Repo.
- [`skripte/verlinken.py`](skripte/verlinken.py): setzt in den Fassungen Links auf Issues, Meilensteine, Dateien und Nachbar-Repos. Nur auf unverlinkte Fassungen anwenden.

## Repos und Meilensteine

- Offen: [FOERBICO_und_rpi-virtuell](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell) · [Meilensteine](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestones) · [offene Issues](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues) · [Pull Requests](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/pulls)
- Geschlossen: [FOERBICO_und_rpi-virtuell-geschlossen](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen) · [Meilensteine](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestones) (seit 16.09.2026 identisch mit dem offenen Repo) · [Dokumentation mit Zwischenberichten und AP-Übersicht](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/src/branch/main/Dokumentation)
- Nachbarn: [oer-community](https://git.rpi-virtuell.de/Comenius-Institut/oer-community) (Hub, ehem. community-hub, [ADR-Index](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/), [STATUS](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/STATUS.md)) · [foerbico-editor](https://git.rpi-virtuell.de/Comenius-Institut/foerbico-editor) · [mdparser](https://git.rpi-virtuell.de/Comenius-Institut/mdparser)
- Antrag: Vorhabenbeschreibung 19.12.2023 (Nextcloud, `3_Projekte/2_Lauf-Projekte/FOERBICO/Antragsphase/Antrag final/Dokument CI/`); Meilensteine im Repo: [`Orga/Meilensteine.md`](../Meilensteine.md).

Die Meilenstein-Links beider Repos stehen am Ende jeder Fassung.
