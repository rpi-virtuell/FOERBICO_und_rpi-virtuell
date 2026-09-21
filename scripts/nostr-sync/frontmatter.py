"""Liest das Drei-Block-Frontmatter eines Hugo-Beitrags.

Beantwortet genau eine Frage: Welche Werte stehen in welchem Block?

Tut ausdruecklich NICHT: fachlich validieren, Events bauen, Dateien schreiben.
"""

import re
from dataclasses import dataclass
from datetime import date

import yaml

STATIC_SITE_GENERATOR = "# staticSiteGenerator"
IMAGES = "# bilder"

MARKERS = (STATIC_SITE_GENERATOR, IMAGES)

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


class NoFrontmatter(Exception):
    """Die Datei hat keinen Frontmatter-Block zwischen `---`-Zeilen."""


@dataclass
class ParsedPost:
    metadata: dict
    images: dict
    site_generator: dict
    """Der `# staticSiteGenerator`-Block. Wandert in kein Event — er dient allein
    dem Vergleich in warning_checks, weil die Schlagworte faktisch dort leben."""
    content: str
    content_line: int
    """Dateizeile, in der der Fliesstext beginnt — fuer Befunde mit brauchbaren
    Zeilennummern."""


def parse_post(raw: str) -> ParsedPost:
    """Zerlegt den Rohtext einer index.md in seine Frontmatter-Bloecke."""
    match = FRONTMATTER.match(raw)
    if match is None:
        raise NoFrontmatter("kein Frontmatter zwischen `---`-Zeilen gefunden")
    front, body = match.group(1), match.group(2)
    return ParsedPost(
        metadata=_common_metadata(front),
        images=_images(front),
        site_generator=_block(front, STATIC_SITE_GENERATOR),
        content=body,
        content_line=raw[: match.start(2)].count("\n") + 1,
    )


def _images(front: str) -> dict:
    """Der `# bilder`-Block, falls vorhanden — sonst leer.

    Unter dem Marker steht der eigentliche YAML-Schluessel `bilder`; der Marker
    selbst ist nur ein Kommentar.
    """
    return _block(front, IMAGES).get("bilder") or {}


def _block(front: str, marker: str) -> dict:
    """Der YAML-Block ab `marker` bis zum naechsten anderen Marker.

    Der Marker selbst bleibt stehen: YAML liest ihn als Kommentar. Dieselbe
    Abschneideregel wie in mdparser/sync/core/parser.ts.
    """
    start = front.find(marker)
    if start < 0:
        return {}
    weitere = [front.find(m, start + len(marker)) for m in MARKERS if m != marker]
    ends = [i for i in weitere if i >= 0]
    body = front[start : min(ends)] if ends else front[start:]
    return _normalize(yaml.safe_load(body) or {})


def _common_metadata(front: str) -> dict:
    """Alles vom Anfang bis zum ersten anderen Blockmarker.

    Bewusst ab Position 0 und nicht ab `# commonMetadata`: So zaehlen auch Felder
    dazu, die vor dem Marker stehen, und ein Frontmatter ganz ohne Marker bleibt
    vollstaendig. Dieselbe Regel wie in mdparser/sync/core/parser.ts — Abweichung
    hier wuerde andere Events erzeugen als die bestehende Loesung.

    Die Zeile `# commonMetadata` muss nicht entfernt werden: YAML liest sie als
    Kommentar.
    """
    positions = [front.find(m) for m in (STATIC_SITE_GENERATOR, IMAGES)]
    ends = [i for i in positions if i >= 0]
    body = front[: min(ends)] if ends else front
    return _normalize(yaml.safe_load(body) or {})


def _normalize(value):
    """Macht die Typ-Automatik von YAML rueckgaengig, soweit verlustfrei moeglich.

    YAML liest `2026-08-12` als Datum und `2026` als Zahl. Als Tag-Wert braucht
    Nostr aber Strings (NIP-01). Ein Bool bleibt dagegen stehen: `no` wurde zu
    `False`, und daraus „False" zu machen waere geraten — gemeint war das Wort.
    Solche Werte meldet spaeter error_checks mit Feldnamen.
    """
    if isinstance(value, dict):
        return {key: _normalize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_normalize(item) for item in value]
    if isinstance(value, bool):
        # Muss vor der Zahl stehen: bool ist in Python eine Unterklasse von int.
        return value
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, (int, float)):
        return str(value)
    return value
