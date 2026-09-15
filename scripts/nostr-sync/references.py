"""Leitet Bezeichner und Medienverweise aus einem Beitrag ab.

Beantwortet genau eine Frage: Wie heisst dieses Ding, und auf welche Bilder
zeigt der Beitrag?

Tut ausdruecklich NICHT: Dateien lesen, Netz ansprechen, Events bauen.
"""

import re
from dataclasses import dataclass
from urllib.parse import urlparse

# Blossom-Hash-URL (BUD-01): letztes Pfadsegment ist der SHA-256, Endung optional.
HASH_IN_PATH = re.compile(r"/([0-9a-f]{64})(?:\.[a-z0-9]+)?$", re.IGNORECASE)

# Bild-Syntax in Markdown — dieselbe Regex wie mdparser, md2blossom und der Hub.
MARKDOWN_IMAGE = re.compile(r"""!\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)""")


@dataclass(frozen=True)
class ImageReference:
    hash: str
    url: str


def extract_slug(post_id: str) -> str:
    """Der `d`-Tag-Wert: der Pfad von `commonMetadata.id` ohne aeussere Schraegstriche.

    Innere Schraegstriche bleiben stehen — aus `…/en/our-team` wird `en/our-team`,
    nicht `our-team`. Dieselbe Regel wie mdparsers `extractSlug`; ein anderer Slug
    wuerde ein anderes Event adressieren.
    """
    return urlparse(post_id).path.strip("/")


def hash_from_url(url: str) -> str | None:
    """Der SHA-256 aus einer Blossom-URL, sonst None.

    Eine Bild-URL ohne Hash im Pfad zeigt auf keinen Lizenznachweis. Relative oder
    kaputte URLs ergeben None statt eines geratenen Werts — ein falscher Hash waere
    schlimmer als gar keiner.
    """
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return None
    match = HASH_IN_PATH.search(parsed.path)
    return match.group(1).lower() if match else None


def image_references(cover_url: str | None, content: str) -> list[ImageReference]:
    """Die Bilder eines Beitrags mit Blossom-Hash — Cover zuerst, dann der Fliesstext.

    Die Reihenfolge ist bedeutungstragend: edufeeds ArticleView und der Hub lesen
    das **erste** Ergebnis als Cover. Es gibt dafuer kein Label, nur die Position.

    Dedupliziert nach Hash: Zeigt der Text das Cover erneut, erscheint es einmal.
    Bilder ohne Hash im Pfad (relative Pfade, fremde Hosts) fallen weg — zu ihnen
    gibt es weder Blob noch Nachweis.
    """
    candidates = []
    if cover_url:
        candidates.append(cover_url)
    candidates.extend(match.group(2) for match in MARKDOWN_IMAGE.finditer(content))

    references: list[ImageReference] = []
    seen: set[str] = set()
    for url in candidates:
        image_hash = hash_from_url(url)
        if image_hash is None or image_hash in seen:
            continue
        seen.add(image_hash)
        references.append(ImageReference(hash=image_hash, url=url))
    return references
