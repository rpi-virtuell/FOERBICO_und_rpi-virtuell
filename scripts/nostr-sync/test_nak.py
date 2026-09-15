import pytest

import nak

SLUG = "ein-test-beitrag"


def artikel(slug: str = SLUG, titel: str = "Ein Titel") -> dict:
    return {"kind": 30023, "tags": [["d", slug], ["title", titel]], "content": "Text"}


def test_generate_key_returns_a_hex_secret():
    key = nak.generate_key()

    assert len(key) == 64
    assert all(c in "0123456789abcdef" for c in key)


def test_public_key_belongs_to_the_secret(throwaway_key):
    pubkey = nak.public_key(throwaway_key)

    assert len(pubkey) == 64
    assert nak.public_key(throwaway_key) == pubkey


def test_fetching_an_unpublished_event_gives_none(local_relay, throwaway_key):
    """Grundfall der Idempotenz: Zum Slug gibt es noch nichts."""
    found = nak.fetch_event(
        kind=30023, pubkey=nak.public_key(throwaway_key), relay=local_relay, identifier="gibt-es-nicht"
    )

    assert found is None


def test_a_published_event_can_be_fetched_back(local_relay, throwaway_key):
    pubkey = nak.public_key(throwaway_key)

    assert nak.publish(artikel(), relay=local_relay, signer=throwaway_key)

    found = nak.fetch_event(kind=30023, pubkey=pubkey, relay=local_relay, identifier=SLUG)
    assert found is not None
    assert [t for t in found["tags"] if t[0] == "d"] == [["d", SLUG]]


def test_nak_fills_in_pubkey_id_and_signature(local_relay, throwaway_key):
    """Wir liefern nur kind, tags und content — den Rest macht der Signer."""
    nak.publish(artikel("signatur-test"), relay=local_relay, signer=throwaway_key)

    found = nak.fetch_event(
        kind=30023, pubkey=nak.public_key(throwaway_key), relay=local_relay, identifier="signatur-test"
    )

    assert found["pubkey"] == nak.public_key(throwaway_key)
    assert len(found["id"]) == 64
    assert len(found["sig"]) == 128


def test_the_tag_order_survives_the_round_trip(local_relay, throwaway_key):
    """Die Cover-Konvention haengt an der Position — Umsortieren waere fatal."""
    event = {
        "kind": 30023,
        "tags": [["d", "reihenfolge"], ["image", "https://x/y.jpg"], ["x", "a" * 64], ["t", "eins"]],
        "content": "Text",
    }
    nak.publish(event, relay=local_relay, signer=throwaway_key)

    found = nak.fetch_event(
        kind=30023, pubkey=nak.public_key(throwaway_key), relay=local_relay, identifier="reihenfolge"
    )

    assert found["tags"] == event["tags"]


def test_publishing_to_an_unreachable_relay_reports_failure(throwaway_key):
    """Kein stilles Scheitern: Der Aufrufer muss das als Fehler sehen koennen."""
    assert not nak.publish(artikel("nirgendwo"), relay="ws://127.0.0.1:9", signer=throwaway_key)


def test_an_unreachable_relay_raises_when_asked_for_state(throwaway_key):
    """Beim Idempotenz-Check darf ein totes Relay nicht als „nichts da" durchgehen.

    Sonst wuerde der Sync jedes Mal neu publizieren — oder schlimmer, ein
    „unchanged" melden, das niemand geprueft hat.
    """
    with pytest.raises(nak.NakFailed):
        nak.fetch_event(kind=30023, pubkey="a" * 64, relay="ws://127.0.0.1:9", identifier=SLUG)
