# Kataloge im Hub: Grundschicht, Kuratierung, Vorlagen

Der Hub zeigt je Community einen Katalog (`#community?c=<id>&zu=katalog`). Er hat zwei Schichten.

## Grundschicht: was mit der Community geteilt wurde

Alles mit `h`-Tag auf den Community-Schlüssel gehört zum Katalog: Material, Beiträge, Termine. Bereits Vorhandenes wird als Repost (`kind:16`) geteilt. Das Team macht das in der edufeed-App über „In Community teilen“; niemand muss dafür eine Liste anlegen. Wer mit dem Community-Schlüssel teilt, ist immer zugelassen.

## Kuratierung: Listen des Redaktionskreises

Die zweite Schicht („Vom Redaktionskreis zusammengestellt“) sind Listen `kind:30004`.

- In der edufeed-App: Listen › Neue Liste › Kuratierungsliste, `d` = `katalog` (weitere Listen `katalog-<thema>`).
- Für das Schaufenster (FOERBICO) entsteht die Liste aus `Website/navigation.yaml` (Schlüssel `katalog`) per `mdparser sync navigation`, Lauf von Hand.
- Die Personen-Liste (`kind:30000`, `d = personen`) liegt als Vorlage `personen-liste.json` bereit; `p`-Tags werden nur nach Einverständnis eingetragen, zuerst die hauptamtlichen Teams.

## Entfernen

Im Menü „Aus der Community entfernen“. Im Hub wirkt das nur, wenn es mit dem Community-Schlüssel geschieht.

## Vorlagen und Veröffentlichung

- `personen-liste.json`: Vorlage der Personen-Liste.
- `teilen-<community>.json`: Reposts als Vorschläge zur Entscheidung durch Redaktion und Jörg Lohrer; Stand und Auswahlkriterien in `teilen-vorschlaege.md`.
- Veröffentlicht wird mit `tools/listen/veroeffentlichen.ts`, siehe `tools/listen/README.md`.

## Sicherheit

Private Schlüssel (`nsec`) und Bunker-Links gehören nie ins Repository, in Vorlagen oder Commits. Sie liegen nur in einer Env-Datei außerhalb des Repos.
