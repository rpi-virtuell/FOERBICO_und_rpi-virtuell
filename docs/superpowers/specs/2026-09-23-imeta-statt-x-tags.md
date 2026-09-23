# Bildmetadaten im Artikel: `imeta` statt (oder neben) den `x`-Tags

**Stand: 2026-09-23 · Entwurfsnotiz, noch keine Festlegung.**
Gehört zur Spec [2026-09-14-md-to-nostr-sync-neu-design.md](2026-09-14-md-to-nostr-sync-neu-design.md);
dort steht die Risikonotiz zur `x`-Tag-Konvention, die diese Notiz ausarbeitet.

Alle Zahlen gemessen am 2026-09-23 auf `feat/md-to-nostr`. **Branch immer mitschreiben** —
`main` und dieser Branch laufen im Content auseinander.

## Warum überhaupt

Heute trägt ein kind:30023 seine Bilder so:

```json
["image", "https://blossom.edufeed.org/5d66f8e6….jpg"]
["x", "5d66f8e6…"]
["x", "200ab2e7…"]
```

Drei Schwächen:

1. **`x` am Artikel ist in keinem NIP vorgesehen.** NIP-23 standardisiert für kind:30023
   genau vier optionale Tags: `title`, `image`, `summary`, `published_at`. NIP-94 definiert
   `x` als SHA-256 einer Datei — aber im kind:1063. Ein nacktes `["x", hash]` am Artikel ist
   eine edufeed-Absprache (07.09.2026).
2. **Keine Zuordnung.** Die `x`-Liste ist eine Aufzählung von Hashes. Welcher Hash zu
   welchem Bild im Fließtext gehört, ergibt sich allein aus der Reihenfolge. Wer sortiert,
   zerstört die Bedeutung still.
3. **Der Hash hängt an der Adresse.** `x` entsteht, indem 64 Hex-Zeichen aus der URL
   geschnitten werden (`references.py:hash_from_url`). Kein Hash in der URL → kein `x`.

Punkt 3 ist der schwerwiegendste, und er trifft die Mehrheit:

| | gesamt | mit Hash in der URL | absolut ohne Hash | relativ |
|---|---|---|---|---|
| Titelbilder (`commonMetadata.image`) | 81 | 16 | **64** | 1 |
| Fließtextbilder | 236 | 25 | 14 | **197** |

**Für 64 von 81 Titelbildern lässt sich der Hash heute gar nicht übertragen** — obwohl die
Datei im Beitragsordner liegt und der Sync ihren SHA-256 problemlos berechnen könnte.

## Der Kern: `imeta` trennt Adresse von Identität

NIP-92 führt `imeta` ein — ein variadischer Tag aus Schlüssel-Wert-Paaren, der `url`
enthalten **muss** und jedes NIP-94-Feld enthalten **darf**:

```json
["imeta",
 "url https://blossom.edufeed.org/200ab2e7….jpg",
 "m image/jpeg",
 "x 200ab2e7…",
 "size 111629",
 "dim 1600x900",
 "alt Dreiteilige Grafik mit drei Varianten eines Arbeitsblatts …"]
```

Damit hängt der Hash **am Tag**, nicht an der URL. Ein Bild unter
`https://oer.community/bild.jpg` könnte seinen `x`-Wert mitführen — heute unmöglich.

Genau das ist der Grund, warum ein `imeta` auch für `commonMetadata.image` sinnvoll ist:
Es löst den Fall, dass die Adresse nicht dem Hash entspricht.

## Beispiel: `2024-12-16-Canva`, aus den echten Dateien gebaut

```json
["imeta",
 "url https://blossom.edufeed.org/5d66f8e6f78695c7c1a3c41251ad09a68fd67f38aaf0de386eb93f02db8475ce.jpg",
 "m image/jpeg",
 "x 5d66f8e6f78695c7c1a3c41251ad09a68fd67f38aaf0de386eb93f02db8475ce",
 "size 269852",
 "dim 1446x810",
 "alt Illustration eines Laptops über einem aufgeschlagenen Buch, umgeben von Symbolen, …"]
```

`size` und `x` berechnet der Sync heute schon für den kind:1063. `alt` steht im
`# bilder`-Block. **`dim` ist das einzige wirklich neue Datum** — dafür bräuchte es einen
Bildparser.

## Ein Haken, der benannt sein will

NIP-92: *„Each `imeta` tag SHOULD match a URL in the event content."* Und:
*„The client MAY ignore `imeta` tags that do not match the URL in the event content."*

Das Titelbild steht **nicht** im `content`, sondern nur im `image`-Tag. Ein `imeta` dafür
weicht von dieser Empfehlung ab — und Clients dürfen es ausdrücklich ignorieren. Der
Nutzen bliebe also nur bei Lesern, die es trotzdem auswerten.

Mögliche Umgehung: die Cover-URL zusätzlich in den `content` aufnehmen. Das änderte aber
den sichtbaren Artikeltext und ist damit teurer als der Gewinn.

## Drei Varianten

| | Was | Risiko | Gewinn |
|---|---|---|---|
| **A — additiv** | `imeta` **zusätzlich** zu den bestehenden `x`-Tags | keins: bestehende Leser (ArticleView, Hub) bleiben unberührt | volle Metadaten, Hash auch ohne Hash-URL |
| **B — ersetzen** | `x`-Tags weg, nur noch `imeta` | bricht die edufeed-Absprache; ArticleView und Hub müssten mitziehen | sauber nach NIP |
| **C — nur Cover** | `imeta` nur für `commonMetadata.image` | gering | löst nur den Fall der 64 Nicht-Hash-Cover |

**Empfehlung für den ersten Schritt: A.** Additiv ist rückwärtskompatibel und macht den
Nutzen messbar, bevor irgendjemand etwas abschalten muss. B ist eine Absprache mit edufeed,
keine technische Entscheidung.

## Was die Umsetzung braucht

- **Bildmaße (`dim`).** Neu. Ohne zusätzliche Abhängigkeit machbar: JPEG-SOF- und
  PNG-IHDR-Header lassen sich in wenigen Zeilen lesen. Alternativ `dim` weglassen — NIP-92
  verlangt nur `url` plus **ein** weiteres Feld.
- **Reihenfolge.** `imeta` je Bild, in Auftretensreihenfolge, dedupliziert nach URL —
  dieselbe Regel wie heute bei `x` (`references.py:image_references`), aber nach URL statt
  nach Hash, weil es ohne Hash-URL keinen Hash zum Deduplizieren gibt.
- **Fehlende Angaben.** Ohne `# bilder`-Eintrag gibt es kein `alt`; ohne lokale Datei kein
  `size`/`dim`/`x`. Dann bleibt `imeta` bei dem, was da ist. Kein Grund zum Blockieren.
- **Golden-Tests.** Die Fixtures unter `scripts/nostr-sync/fixtures/` vergleichen Tag-Sätze
  zeichengenau gegen die Live-Events. Variante A fügt Tags hinzu — die Fixtures müssen
  bewusst nachgezogen werden, und zwar erst, wenn die Live-Events es auch tragen.

## Offene Fragen

1. Ziehen ArticleView und Hub mit? Ohne sie bleibt A dauerhaft additiv.
2. Soll `imeta` auch für Bilder **ohne** Blossom-Hash geschrieben werden (die 197 relativen)?
   Dort wäre `url` relativ und für einen Nostr-Client wertlos — der Tag würde das Problem
   dokumentieren, nicht lösen.
3. Verhältnis zum kind:1063: `imeta` und der Lizenznachweis tragen teils dieselben Felder.
   Bleibt 1063 die Quelle der Lizenz, und `imeta` nur die Darstellungshilfe?

## Was diese Notiz ausdrücklich nicht ist

Kein Umschreiben von Bildpfaden — das bleibt beim Handschritt (`md2blossom.mjs`) bzw. bei
dessen künftigem Ersatz. `imeta` ändert nur, **wie das Event über Bilder spricht**, nicht,
welche Bilder es gibt.
