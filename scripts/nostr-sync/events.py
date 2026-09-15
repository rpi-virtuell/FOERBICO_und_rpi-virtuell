"""Baut die Nostr-Events aus den Frontmatter-Metadaten.

Beantwortet genau eine Frage: Wie sieht das Event zu diesem Beitrag aus?

UEBERGANGSZUSTAND — zweite Implementierung derselben Konventionen:
Website/scripts/md2blossom.mjs baut ebenfalls kind:30023 und kind:1063. Das
Werkzeug wird bewusst nicht angepasst, solange dieser Sync nicht getestet und
produktiv ist; danach wird es entfernt.

PFLICHT bis dahin: Die kind:1063-Tags dieses Moduls muessen zeichengleich zu
md2blossom.mjs bleiben. 1063 ist nicht ersetzbar — weichen die beiden ab,
publizieren sie sich wechselseitig ueber und die Nachweise akkumulieren, ohne
einer Quelle zuordenbar zu sein.

Bekannte Abweichungen bei kind:30023 (gemessen 2026-09-14) — unkritisch, weil
md2blossoms 30023-Vorlage nie publiziert wird:

  Aspekt         md2blossom.mjs                  dieses Modul
  ------------   -----------------------------   ------------------------------
  Frontmatter    ganzes Dokument flach           nur der commonMetadata-Block
  Schlagworte    keywords ?? tags                nur keywords
  t-Werte        .toLowerCase()                  unveraendert
  title-Tag      Hugo-title vor AMB-name         AMB-name
  d-Tag/Slug     meta.url woertlich              id-Pfad ohne Rand-Schraegstriche

Tut ausdruecklich NICHT: signieren, publizieren, pruefen.
Hintergrund: docs/superpowers/specs/2026-09-14-md-to-nostr-sync-neu-design.md
"""

from datetime import datetime, timezone

from models import CommonMetadata
from references import extract_slug, image_references

ARTICLE = 30023
AMB = 30142


def build_article(
    metadata: CommonMetadata, content: str, pubkey: str, amb_relay: str
) -> dict:
    """kind:30023 — der Beitrag mit Volltext.

    `pubkey`, `id` und `sig` fehlen bewusst: Die setzt `nak` beim Signieren.
    """
    slug = extract_slug(metadata.id)
    language = metadata.inLanguage[0] if metadata.inLanguage else "de"

    tags = [
        ["d", slug],
        ["title", metadata.name],
        ["summary", metadata.description, language],
        ["published_at", _epoch_seconds(metadata.datePublished)],
        ["inLanguage", language],
    ]

    if metadata.image:
        tags.append(["image", metadata.image])
    for reference in image_references(metadata.image, content):
        tags.append(["x", reference.hash])

    tags.extend(["about", uri] for uri in metadata.about)
    tags.extend(["t", keyword] for keyword in metadata.keywords)

    if metadata.type == "LearningResource":
        tags.append(["a", f"{AMB}:{pubkey}:{slug}", amb_relay, "amb-metadata"])

    return {"kind": ARTICLE, "tags": tags, "content": content}


def _epoch_seconds(date_published: str) -> str:
    """`2026-08-12` → `"1786492800"`.

    Strikt auf `YYYY-MM-DD`: Ein nachsichtiger Parser deutet `12.08.2026` als
    8. Dezember und schreibt das stillschweigend ins Event.
    """
    day = datetime.strptime(date_published, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return str(int(day.timestamp()))


def build_amb(metadata: CommonMetadata, pubkey: str, content_relay: str) -> dict:
    """kind:30142 — die AMB-Metadaten, damit OER-Suchdienste den Beitrag finden.

    Wird nur fuer `type: LearningResource` gebaut; die Entscheidung trifft der
    Aufrufer. Anders als im Artikel-Event stehen hier **alle** Sprachen und das
    Datum als Datum, nicht als Zeitstempel.
    """
    slug = extract_slug(metadata.id)

    tags = [
        ["d", slug],
        ["type", metadata.type or "LearningResource"],
        ["name", metadata.name],
        ["description", metadata.description],
    ]
    if metadata.license:
        tags.append(["license:id", metadata.license])

    for creator in metadata.creator:
        tags.extend(_creator_tags(creator))

    tags.extend(["inLanguage", language] for language in metadata.inLanguage)
    tags.extend(["about:id", uri] for uri in metadata.about)
    tags.extend(["learningResourceType:id", uri] for uri in metadata.learningResourceType)
    tags.extend(["educationalLevel:id", uri] for uri in metadata.educationalLevel)

    if metadata.datePublished:
        tags.append(["datePublished", metadata.datePublished])
    if metadata.image:
        tags.append(["image", metadata.image])
    tags.extend(["t", keyword] for keyword in metadata.keywords)

    tags.append(["a", f"{ARTICLE}:{pubkey}:{slug}", content_relay, "content"])

    return {"kind": AMB, "tags": tags, "content": metadata.description or ""}


def _creator_tags(creator) -> list[list[str]]:
    """Ein Creator wird zu mehreren flachen Tags — AMB kennt keine Verschachtelung."""
    tags = [["creator:name", f"{creator.givenName} {creator.familyName}"]]
    if creator.type:
        tags.append(["creator:type", creator.type])
    if creator.id:
        tags.append(["creator:id", creator.id])
    if creator.affiliation:
        tags.append(["creator:affiliation:name", creator.affiliation.name])
        if creator.affiliation.id:
            tags.append(["creator:affiliation:id", creator.affiliation.id])
    return tags
