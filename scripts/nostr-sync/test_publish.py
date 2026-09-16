from textwrap import dedent

import nak
from models import Outcome, Severity
from publish import publish_post

PUBKEY = "5a12b41ec15b466321e88c371be2dc47d9193f9c8bba4ab09fc50045bd35aedf"
RELAYS = ["wss://relay-eins", "wss://relay-zwei"]
AMB_RELAY = "wss://amb-relay"

VOLLSTAENDIG = dedent("""\
    ---
    # commonMetadata
    id: https://oer.community/ein-beitrag
    name: Ein Beitrag
    description: Eine Zusammenfassung.
    license: https://creativecommons.org/licenses/by/4.0/
    creator:
      - givenName: Gina
        familyName: Buchwald-Chassée
    inLanguage:
      - de
    datePublished: '2026-08-12'
    ---
    Ein Absatz.
    """)


def lauf(raw=VOLLSTAENDIG, *, vorhanden=None, acks=99, **kwargs):
    """Fuehrt publish_post mit erfundener Aussenwelt aus.

    `vorhanden` ist entweder ein Event (fuer jede Abfrage) oder ein Dict je Kind.
    """
    gesendet = []

    def fetch(kind, pubkey, relay, identifier=None, image_hash=None):
        if isinstance(vorhanden, dict) and "kind" not in vorhanden:
            return vorhanden.get(kind)
        return vorhanden

    def send(event, relay, signer):
        gesendet.append((event, relay))
        return len(gesendet) <= acks

    ergebnis = publish_post(
        raw, path="ein/pfad/index.md", pubkey=PUBKEY, signer="sec",
        relays=RELAYS, amb_relay=AMB_RELAY, fetch=fetch, send=send, **kwargs
    )
    return ergebnis, gesendet


def test_a_complete_post_without_a_live_event_gets_published():
    ergebnis, gesendet = lauf()

    assert ergebnis.outcome is Outcome.PUBLISHED
    assert len(gesendet) == len(RELAYS)


def test_an_identical_live_event_stays_untouched():
    """Kern der Idempotenz: Das Relay entscheidet, nicht die Git-Historie."""
    erster, _ = lauf()
    ergebnis, gesendet = lauf(vorhanden=erster.article)

    assert ergebnis.outcome is Outcome.UNCHANGED
    assert gesendet == []


def test_missing_required_fields_are_skipped_not_failed():
    """Eine Seite ohne AMB-Metadaten ist nicht kaputt — sie ist nicht gemeint."""
    ohne_pflicht = dedent("""\
        ---
        # commonMetadata
        id: https://oer.community/eine-seite
        ---
        Text
        """)

    ergebnis, gesendet = lauf(ohne_pflicht)

    assert ergebnis.outcome is Outcome.SKIPPED
    assert "name" in ergebnis.reason
    assert gesendet == []


def test_a_file_without_frontmatter_is_skipped():
    """Realfall 2026-01-27-pilgern-im-ru: 0 Byte."""
    ergebnis, gesendet = lauf("")

    assert ergebnis.outcome is Outcome.SKIPPED
    assert gesendet == []


def test_a_nip_violation_blocks_publishing():
    """Ein fehlerhaftes Event wuerde die gute Vorversion auf dem Relay ersetzen."""
    mit_html = VOLLSTAENDIG.replace("Ein Absatz.", "Ein Absatz <br>mit HTML.")

    ergebnis, gesendet = lauf(mit_html)

    assert ergebnis.outcome is Outcome.FAILED
    assert gesendet == []
    assert any(f.severity is Severity.ERROR and f.origin == "NIP-23" for f in ergebnis.findings)


def test_too_few_acknowledgements_count_as_failure():
    ergebnis, _ = lauf(acks=1, min_acks=2)

    assert ergebnis.outcome is Outcome.FAILED


def test_an_unreachable_relay_fails_instead_of_guessing():
    """Weder „sicherheitshalber publizieren" noch „unveraendert annehmen"."""

    def fetch(**_):
        raise nak.NakFailed("Relay nicht abfragbar")

    ergebnis = publish_post(
        VOLLSTAENDIG, path="p", pubkey=PUBKEY, signer="sec", relays=RELAYS,
        amb_relay=AMB_RELAY, fetch=fetch, send=lambda **_: True,
    )

    assert ergebnis.outcome is Outcome.FAILED


def test_a_dry_run_decides_but_sends_nothing():
    ergebnis, gesendet = lauf(dry_run=True)

    assert ergebnis.outcome is Outcome.PUBLISHED
    assert gesendet == []


def test_a_learning_resource_also_publishes_its_amb_event():
    lernressource = VOLLSTAENDIG.replace(
        "# commonMetadata\n", "# commonMetadata\ntype: LearningResource\n"
    )

    ergebnis, gesendet = lauf(lernressource)

    kinds = [e["kind"] for e, _ in gesendet]
    assert 30023 in kinds and 30142 in kinds
    assert ergebnis.amb is not None


def test_the_amb_event_goes_to_its_own_relay():
    lernressource = VOLLSTAENDIG.replace(
        "# commonMetadata\n", "# commonMetadata\ntype: LearningResource\n"
    )

    _, gesendet = lauf(lernressource)

    ziel = {e["kind"]: relay for e, relay in gesendet}
    assert ziel[30142] == AMB_RELAY
    assert ziel[30023] in RELAYS


def test_without_learning_resource_no_amb_event_is_built():
    ergebnis, gesendet = lauf()

    assert ergebnis.amb is None
    assert [e["kind"] for e, _ in gesendet] == [30023] * len(RELAYS)


def test_an_unchanged_amb_event_is_not_republished():
    lernressource = VOLLSTAENDIG.replace(
        "# commonMetadata\n", "# commonMetadata\ntype: LearningResource\n"
    )
    erster, _ = lauf(lernressource)

    ergebnis, gesendet = lauf(lernressource, vorhanden={30023: erster.article, 30142: erster.amb})

    assert ergebnis.outcome is Outcome.UNCHANGED
    assert gesendet == []


def test_a_post_counts_as_published_only_when_both_events_are_through():
    """Halb publiziert ist nicht publiziert.

    Geht der Artikel durch und das AMB-Event nicht, faellt der Beitrag durch.
    Der naechste Lauf sieht den Artikel als unveraendert und holt das AMB-Event
    nach — die Strecke heilt sich selbst.
    """
    lernressource = VOLLSTAENDIG.replace(
        "# commonMetadata\n", "# commonMetadata\ntype: LearningResource\n"
    )

    ergebnis, _ = lauf(lernressource, acks=len(RELAYS), min_acks=1)

    assert ergebnis.outcome is Outcome.FAILED
    assert "30142" in ergebnis.reason or "AMB" in ergebnis.reason
