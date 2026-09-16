"""Entscheidet je Beitrag: publizieren, ueberspringen oder scheitern.

Beantwortet genau eine Frage: Was soll mit diesem Beitrag geschehen?

Die Aussenwelt kommt als Funktionsparameter herein (`fetch`, `send`) statt als
Import. Dadurch ist jede Verzweigung ohne laufendes Relay pruefbar — kein
Framework, keine Interfaces, nur Argumente. Voreingestellt sind die echten
`nak`-Operationen, im Betrieb aendert sich also nichts.

Tut ausdruecklich NICHT: Events bauen, Regeln formulieren, Berichte schreiben.
"""

from dataclasses import dataclass
from pathlib import Path

import images
import nak
from error_checks import check_hard_line_breaks, check_html
from events import build_amb, build_article, tags_equal
from frontmatter import NoFrontmatter, parse_post
from models import CommonMetadata, Outcome, PostResult
from pydantic import ValidationError
from references import extract_slug, image_references

ARTICLE = 30023
AMB = 30142
BLOSSOM = "https://blossom.edufeed.org"


@dataclass
class _Abgleich:
    """Ergebnis fuer ein einzelnes Event: lag es schon so da, und ging es raus?"""

    existing: dict | None = None
    changed: bool = False
    error: str = ""


def publish_post(
    raw: str,
    *,
    path: str,
    pubkey: str,
    signer: str,
    relays: list[str],
    amb_relay: str,
    fetch=nak.fetch_event,
    send=nak.publish,
    sync_images=images.sync_images,
    blossom: str = BLOSSOM,
    min_acks: int = 2,
    dry_run: bool = False,
) -> PostResult:
    """Fuehrt einen Beitrag durch die Entscheidungskette.

    Reihenfolge mit Absicht: Erst wird geklaert, ob der Beitrag ueberhaupt fuer
    Nostr gedacht ist (Frontmatter, Pflichtfelder) — das ist kein Defekt und
    faerbt den Lauf nicht rot. Erst danach greifen die Spezifikationspruefungen,
    die blockieren.
    """
    try:
        post = parse_post(raw)
    except NoFrontmatter as fehlt:
        return PostResult(path=path, outcome=Outcome.SKIPPED, reason=str(fehlt))

    try:
        metadata = CommonMetadata.model_validate(post.metadata)
    except ValidationError as ungueltig:
        return PostResult(
            path=path, outcome=Outcome.SKIPPED, reason=_missing_fields(ungueltig)
        )

    slug = extract_slug(metadata.id)
    findings = check_html(post.content, post.content_line) + check_hard_line_breaks(
        post.content, post.content_line
    )
    if findings:
        return PostResult(
            path=path, outcome=Outcome.FAILED, slug=slug, findings=findings,
            reason="Spezifikationsverletzung — nicht publiziert",
        )

    article = build_article(metadata, post.content, pubkey, amb_relay)
    amb = build_amb(metadata, pubkey, relays[0]) if metadata.type == "LearningResource" else None

    ziele = [(article, ARTICLE, relays)]
    if amb is not None:
        ziele.append((amb, AMB, [amb_relay]))

    abgleiche = []
    for event, kind, event_relays in ziele:
        abgleich = _sync_event(
            event, kind=kind, pubkey=pubkey, slug=slug, relays=event_relays,
            signer=signer, fetch=fetch, send=send, min_acks=min_acks, dry_run=dry_run,
        )
        abgleiche.append((kind, abgleich))
        if abgleich.error:
            return PostResult(
                path=path, outcome=Outcome.FAILED, slug=slug, article=article, amb=amb,
                existing=abgleiche[0][1].existing, reason=f"kind:{kind} — {abgleich.error}",
            )

    bilder = sync_images(
        image_references(metadata.image, post.content), post.images, Path(path).parent,
        pubkey=pubkey, signer=signer, relays=relays, blossom=blossom, dry_run=dry_run,
    )

    geaendert = any(a.changed for _, a in abgleiche)
    gemeinsam = dict(
        path=path, slug=slug, article=article, amb=amb,
        existing=abgleiche[0][1].existing, findings=list(bilder.findings),
    )
    if not geaendert:
        return PostResult(outcome=Outcome.UNCHANGED, **gemeinsam)
    return PostResult(
        outcome=Outcome.PUBLISHED,
        reason="dry-run — nichts gesendet" if dry_run else "",
        **gemeinsam,
    )


def _sync_event(
    event: dict, *, kind: int, pubkey: str, slug: str, relays: list[str],
    signer: str, fetch, send, min_acks: int, dry_run: bool,
) -> _Abgleich:
    """Holt den Relay-Stand, vergleicht und sendet nur bei Abweichung.

    Das Relay entscheidet, nicht die Git-Historie — deshalb ist ein nicht
    abfragbares Relay ein Fehler und kein „dann eben neu publizieren".
    """
    try:
        existing = fetch(kind=kind, pubkey=pubkey, relay=relays[0], identifier=slug)
    except nak.NakFailed as nicht_erreichbar:
        return _Abgleich(error=f"Relay nicht abfragbar: {nicht_erreichbar}")

    if existing is not None and tags_equal(event, existing):
        return _Abgleich(existing=existing, changed=False)

    if dry_run:
        return _Abgleich(existing=existing, changed=True)

    acks = sum(send(event=event, relay=relay, signer=signer) for relay in relays)
    if acks < min(min_acks, len(relays)):
        return _Abgleich(
            existing=existing,
            error=f"nur {acks} von {min(min_acks, len(relays))} noetigen Bestaetigungen",
        )
    return _Abgleich(existing=existing, changed=True)


def _missing_fields(error: ValidationError) -> str:
    """Nennt die Felder beim Namen — „ungueltig" allein hilft der Redaktion nicht."""
    felder = sorted({".".join(str(teil) for teil in e["loc"]) for e in error.errors()})
    return "Pflichtfelder fehlen oder haben den falschen Typ: " + ", ".join(felder)
