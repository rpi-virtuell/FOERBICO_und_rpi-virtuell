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


def lauf(raw=VOLLSTAENDIG, *, vorhanden=None, acks=2, **kwargs):
    """Fuehrt publish_post mit erfundener Aussenwelt aus."""
    gesendet = []

    def fetch(kind, pubkey, relay, identifier=None, image_hash=None):
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
