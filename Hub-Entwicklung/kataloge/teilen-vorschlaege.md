# Vorschläge zum beispielhaften Teilen

Stand 05.11.2026. Die Vorlagen `teilen-alpika-grundschule.json`, `teilen-religlobal.json` und `teilen-rpi-virtuell.json` enthalten je drei Vorschläge aus den Beständen von `relay-rpi.edufeed.org` (45 Materialien) und `relay.edufeed.org` (die ersten 200); der Bestand von `amb-relay.edufeed.org` lieferte nur Hochschulmaterial. Nur Lizenzen CC BY, CC BY-SA, CC0; keine Materialien der Community-Schlüssel selbst. Die Auswahl ist ein Vorschlag, Entscheidung bei Redaktion und Jörg Lohrer.

## Wie eine Vorlage entsteht

Je ausgewähltem Material ein Eintrag im Array der jeweiligen Datei (Material mit offener Lizenz, nicht vom Community-Schlüssel selbst verfasst):

```json
{
  "kind": 16,
  "tags": [
    ["a", "30142:<Schlüssel-des-Materials-hex>:<d-Kennung>", "wss://amb-relay.edufeed.org"],
    ["k", "30142"],
    ["p", "<Schlüssel-des-Materials-hex>"],
    ["h", "<Community-hex>"]
  ],
  "content": ""
}
```

Community-Schlüssel (hex) für das `h`-Tag:

| Community | `h`-Tag (hex) |
|---|---|
| ALPIKA Grundschule | `7a09d40239cb1ecc4c16868a8cb84a55981ca8a72e282e74e7bf3a3939df7d5a` |
| reliGlobal | `5757f422eeca80eb060582365156593aa9785af5f653eb614710913a2c4b42c8` |
| rpi-virtuell | `ae6199bb435d70a0ecce61324ac80e7c24dedf2b0680cbd3e94983e7557746a2` |

## Entscheidungstabelle (Stand 05.11.2026, aus relay-rpi und relay.edufeed.org)

| Community | Nr. | Materialtitel | Schlüssel (Präfix) | Lizenz | Grund |
|---|---|---|---|---|---|
| alpika-grundschule | 1 | Was ist gerecht? | `65a652cb` | CC BY 4.0 | Primarbereich, Verantwortung/Gerechtigkeit, interreligiös |
| alpika-grundschule | 2 | Eine Überschwemmung (christlich) | `65a652cb` | CC BY 4.0 | Primarbereich, Volksschule, Thema Wasser |
| alpika-grundschule | 3 | GOTT WIRKT: WUNDER: WIESO FÜRCHTET IHR EUCH? Wie Grundschulkinder im Bibliolog das Wunder der Sturmstillung erleben | `776c7bfe` | CC BY 4.0 | Grundschulkinder, Bibliolog zu Wundern |
| religlobal | 1 | Gerechtigkeit rund um die Welt | `65a652cb` | CC BY 4.0 | Gerechtigkeit global, Primarbereich |
| religlobal | 2 | Wasser - kann es zu einer gerechten Verteilung kommen | `65a652cb` | CC BY 4.0 | gerechte Verteilung von Wasser |
| religlobal | 3 | Friedensfähig oder kriegstüchtig? Arbeitsblätter mit Aufgaben zu biblischen Texten | `e8dd80cf` | CC BY-SA 4.0 | Frieden, Gewalt, Bonhoeffer |
| rpi-virtuell | 1 | Moral und Nächstenliebe – eine Frage des Geldes? | `776c7bfe` | CC BY 4.0 | Sekundarbereich I, Ethik |
| rpi-virtuell | 2 | Glaube kann Hoffnung geben | `776c7bfe` | CC BY 4.0 | Sekundarbereich I, Leid/Trauer |
| rpi-virtuell | 3 | Fürchtet euch nicht: Christus ist auferstanden! Eine Unterrichtseinheit zu Ostern mit Thematisierung orthodoxer Osterfeierlichkeiten | `776c7bfe` | CC BY 4.0 | Sekundarbereich I, Auferstehung |

Bei rpi-virtuell sind die Vorschläge ältere Artikel aus dem Bestand, weil neu angelegte Materialien noch nicht auf den Relays liegen.

Einfacher Weg ohne Vorlage: das Team teilt direkt in der edufeed-App („In Community teilen“), siehe `README.md`.
