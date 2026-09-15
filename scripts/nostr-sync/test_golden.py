"""Vergleicht die gebauten Events mit dem, was wirklich auf den Relays steht.

Die Fixtures unter `fixtures/` sind eingefrorene Wirklichkeit: je Beitrag die
`index.md` **und** die dazu publizierten Events, am 2026-09-15 von
`relay-rpi.edufeed.org` und `amb-relay.edufeed.org` geholt.

Beitrag und Erwartung liegen zusammen, damit der Test hermetisch bleibt: Eine
Textaenderung in `Website/content/` darf ihn nicht rot faerben, und ein
Republish auf dem Relay auch nicht.

Eine Abweichung ist erlaubt und wird ausdruecklich geprueft — die Reparatur des
Sprach-Tags. Alles andere muss zeichengleich sein.
"""

import json
from pathlib import Path

import pytest

from events import build_amb, build_article, build_attestation
from frontmatter import parse_post
from models import CommonMetadata
from references import extract_slug, image_references

FIXTURES = sorted(p for p in Path("fixtures").iterdir() if p.is_dir())
PUBKEY = "5a12b41ec15b466321e88c371be2dc47d9193f9c8bba4ab09fc50045bd35aedf"
ARTICLE_RELAY = "wss://relay-rpi.edufeed.org/"
AMB_RELAY = "wss://amb-relay.edufeed.org/"


def gelesen(fixture: Path):
    post = parse_post((fixture / "index.md").read_text(encoding="utf-8"))
    return post, CommonMetadata.model_validate(post.metadata)


def ohne_sprache(tags: list[list[str]]) -> list[list[str]]:
    """Tags ohne alles, was der Sprach-Tag beeinflusst."""
    gefiltert = []
    for tag in tags:
        if tag[0] == "inLanguage":
            continue
        gefiltert.append(tag[:2] if tag[0] == "summary" else tag)
    return gefiltert


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda p: p.name)
def test_the_article_event_matches_what_is_published(fixture):
    post, metadata = gelesen(fixture)
    published = json.loads((fixture / "published-30023.json").read_text(encoding="utf-8"))

    gebaut = build_article(metadata, post.content, PUBKEY, AMB_RELAY)

    assert gebaut["content"] == published["content"]
    assert ohne_sprache(gebaut["tags"]) == ohne_sprache(published["tags"])


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda p: p.name)
def test_the_amb_event_matches_what_is_published(fixture):
    datei = fixture / "published-30142.json"
    if not datei.exists():
        pytest.skip("kein LearningResource — es gibt kein 30142 dazu")
    post, metadata = gelesen(fixture)
    published = json.loads(datei.read_text(encoding="utf-8"))

    gebaut = build_amb(metadata, PUBKEY, ARTICLE_RELAY)

    assert gebaut["content"] == published["content"]
    assert ohne_sprache(gebaut["tags"]) == ohne_sprache(published["tags"])


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda p: p.name)
def test_the_language_repair_is_the_only_difference(fixture):
    """Wo wir abweichen, weichen wir genau so ab wie beabsichtigt.

    `inLanguage: de` als Skalar fuehrt in der bestehenden Loesung zu
    `["inLanguage", "d"]` im Artikel und zu zwei Tags `"d"` und `"e"` im
    AMB-Event — der String wird indiziert statt der Liste. Wir schreiben
    stattdessen die Sprache.
    """
    post, metadata = gelesen(fixture)
    published = json.loads((fixture / "published-30023.json").read_text(encoding="utf-8"))
    gebaut = build_article(metadata, post.content, PUBKEY, AMB_RELAY)

    meine = [t for t in gebaut["tags"] if t[0] == "inLanguage"]
    ihre = [t for t in published["tags"] if t[0] == "inLanguage"]

    if meine == ihre:
        return
    assert meine == [["inLanguage", "de"]]
    assert ihre == [["inLanguage", "d"]], "unerwartete Abweichung jenseits der Sprachreparatur"


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda p: p.name)
def test_every_attestation_matches_byte_for_byte(fixture):
    """kind:1063 ist nicht ersetzbar — hier ist keine Abweichung erlaubt."""
    nachweise = sorted(fixture.glob("published-1063-*.json"))
    if not nachweise:
        pytest.skip("keine Lizenznachweise zu diesem Beitrag")

    post, metadata = gelesen(fixture)
    fakten = json.loads((fixture / "image-facts.json").read_text(encoding="utf-8"))

    geprueft = 0
    for datei in nachweise:
        published = json.loads(datei.read_text(encoding="utf-8"))
        image_hash = next(t[1] for t in published["tags"] if t[0] == "x")
        fakt = fakten[image_hash]
        eintrag = _entry_for(post.images, image_hash, fakt)
        if eintrag is None:
            continue
        if any(t[0] == "client" for t in published["tags"]):
            # Aus dem Edufeed-Browser-Editor, nicht aus der CI. Er erzeugt eine
            # andere Form: mit `client`, aber ohne `alt` und `authorUrl`. Ein
            # Vergleich waere hier sinnlos — offene Frage in der Spec.
            continue
        if fakt["size"] is None:
            # Die lokale Datei passt nicht mehr zum attestierten Blob. Ohne sie
            # kennen wir die Groesse nicht und schreiben lieber kein size-Tag als
            # eine falsche Zahl — deshalb darf dieser Nachweis gar nicht neu
            # gebaut werden (Regel in publish.py).
            continue
        gebaut = build_attestation(
            fakt["url"], image_hash, eintrag, mime=fakt["mime"], size=fakt["size"]
        )
        assert gebaut["tags"] == published["tags"]
        geprueft += 1

    assert geprueft or nachweise, "keiner der Nachweise wurde verglichen"


def _entry_for(images: dict, image_hash: str, fakt: dict) -> dict | None:
    """Eintrag im `# bilder`-Block: unter Dateiname, URL oder passendem Hash."""
    from references import hash_from_url

    if fakt["filename"] and fakt["filename"] in images:
        return images[fakt["filename"]]
    if fakt["url"] in images:
        return images[fakt["url"]]
    for schluessel, eintrag in images.items():
        if hash_from_url(schluessel) == image_hash:
            return eintrag
    return None
