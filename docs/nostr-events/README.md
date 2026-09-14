# Nostr-Events aus dem Sync-Workflow

Der Workflow [`nostr-sync.yml`](../../.github/workflows/nostr-sync.yml) veröffentlicht die
Blogposts aus `Website/content/` über das `sync`-Modul von
[`edufeed-org/mdparser`](https://github.com/edufeed-org/mdparser/tree/main/sync) als
signierte Nostr-Events. Pro Post entstehen bis zu drei Event-Typen ("kinds"):

| Kind | Name | Zweck | Relay | Wann |
|---|---|---|---|---|
| [`30023`](kind-30023.md) | Article | Der eigentliche Blogpost (Titel, Text, Cover) | `relay-rpi.edufeed.org` | immer |
| [`30142`](kind-30142.md) | AMB-Metadaten | Strukturierte Bildungsmetadaten (Lizenz, Autor\*innen, Fach, Sprache …) | `amb-relay.edufeed.org` | nur wenn `type: LearningResource` |
| [`1063`](kind-1063.md) | Bild-Lizenznachweis | Ein Nachweis pro Bild im Post (Lizenz, Quelle, Credit) | `relay-rpi.edufeed.org`, `relay.edufeed.org` | pro Bild aus dem `# bilder`-Block |

## Wie die drei Events zusammenhängen

```
Frontmatter (index.md)                 Nostr
─────────────────────                  ─────
# commonMetadata          ──────────►  kind:30023  (Article, Volltext)
                                             │  a-Tag ──────┐
                                             ▼              │
                           ──────────►  kind:30142  (AMB)   │
                                             │  a-Tag ◄──────┘
                                             ▼  (Querverweis in beide Richtungen)

# bilder                  ──────────►  kind:1063  (je Bild ein Lizenznachweis)
                                             │  x-Tag (SHA-256-Hash)
                                             ▼
                           kind:30023  x-Tag zeigt auf denselben Hash
```

- **30023 ↔ 30142**: Beide tragen denselben `d`-Tag (Slug aus `commonMetadata.id`) und
  verweisen sich per `a`-Tag gegenseitig (`kind:pubkey:d`). Die Adresse kollidiert nicht,
  weil `kind` Teil des Schlüssels ist.
- **30023 → 1063**: Jedes Bild (Cover + Fließtextbilder mit Hash-URL) bekommt im
  Article-Event ein `x`-Tag mit seinem SHA-256-Hash. Das zugehörige `1063`-Event trägt
  denselben Hash im eigenen `x`-Tag — so lässt sich vom Artikel zum Lizenznachweis
  auflösen, ohne dass der Artikel selbst Lizenzdaten enthält.

## Beispiel-Quelle

Die Beispiele in den drei Detail-Dateien sind **echte, bereits veröffentlichte Events**
dieses Projekts (`oer.community` / FOERBICO), abgefragt direkt von den produktiven
Relays — keine erfundenen Testdaten.

## Details

- [`kind-30023.md`](kind-30023.md) — Article
- [`kind-30142.md`](kind-30142.md) — AMB-Metadaten
- [`kind-1063.md`](kind-1063.md) — Bild-Lizenznachweis
