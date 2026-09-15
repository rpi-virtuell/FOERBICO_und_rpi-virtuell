"""Entscheidet je Beitrag: publizieren, ueberspringen oder scheitern.

Beantwortet genau eine Frage: Was soll mit diesem Beitrag geschehen?

Die Aussenwelt kommt als Funktionsparameter herein (`fetch`, `send`) statt als
Import. Dadurch ist jede Verzweigung ohne laufendes Relay pruefbar — kein
Framework, keine Interfaces, nur Argumente. Voreingestellt sind die echten
`nak`-Operationen, im Betrieb aendert sich also nichts.

Tut ausdruecklich NICHT: Events bauen, Regeln formulieren, Berichte schreiben.
"""

import nak
from error_checks import check_hard_line_breaks, check_html
from events import build_article, tags_equal
from frontmatter import NoFrontmatter, parse_post
from models import CommonMetadata, Outcome, PostResult
from pydantic import ValidationError
from references import extract_slug

ARTICLE = 30023


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

    try:
        existing = fetch(kind=ARTICLE, pubkey=pubkey, relay=relays[0], identifier=slug)
    except nak.NakFailed as nicht_erreichbar:
        return PostResult(
            path=path, outcome=Outcome.FAILED, slug=slug, article=article,
            reason=f"Relay nicht abfragbar: {nicht_erreichbar}",
        )

    if existing is not None and tags_equal(article, existing):
        return PostResult(path=path, outcome=Outcome.UNCHANGED, slug=slug, article=article)

    if dry_run:
        return PostResult(
            path=path, outcome=Outcome.PUBLISHED, slug=slug, article=article,
            existing=existing, reason="dry-run — nichts gesendet",
        )

    acks = sum(send(event=article, relay=relay, signer=signer) for relay in relays)
    if acks < min_acks:
        return PostResult(
            path=path, outcome=Outcome.FAILED, slug=slug, article=article, acks=acks,
            reason=f"nur {acks} von {min_acks} noetigen Bestaetigungen",
        )

    return PostResult(
        path=path, outcome=Outcome.PUBLISHED, slug=slug, article=article,
        existing=existing, acks=acks,
    )


def _missing_fields(error: ValidationError) -> str:
    """Nennt die Felder beim Namen — „ungueltig" allein hilft der Redaktion nicht."""
    felder = sorted({".".join(str(teil) for teil in e["loc"]) for e in error.errors()})
    return "Pflichtfelder fehlen oder haben den falschen Typ: " + ", ".join(felder)
