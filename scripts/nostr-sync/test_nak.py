import hashlib

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


MINI_PNG = bytes.fromhex(
    "89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c4890000000d4944415478"
    "9c6364f8cf500f000501010018dd8db10000000049454e44ae426082"
)


def test_an_unknown_blob_is_reported_as_missing(local_blossom):
    unbekannt = "b" * 64

    assert not nak.blossom_has(unbekannt, server=local_blossom)


def test_an_uploaded_blob_is_found_afterwards(local_blossom, throwaway_key, tmp_path):
    bild = tmp_path / "testbild.png"
    bild.write_bytes(MINI_PNG)
    erwarteter_hash = hashlib.sha256(MINI_PNG).hexdigest()

    beschreibung = nak.blossom_upload(bild, server=local_blossom, signer=throwaway_key)

    assert beschreibung["sha256"] == erwarteter_hash
    assert nak.blossom_has(erwarteter_hash, server=local_blossom)


def test_encode_naddr_produces_a_shareable_address():
    adresse = nak.encode_naddr(
        kind=30023, pubkey="a" * 64, identifier="ein-beitrag",
        relay="wss://relay-rpi.edufeed.org",
    )

    assert adresse.startswith("naddr1")


def test_a_failing_naddr_encoding_gives_none_instead_of_raising():
    """Nicht fatal: Ein Darstellungsdetail darf keinen gruenen Lauf rot faerben."""
    assert nak.encode_naddr(kind=30023, pubkey="kein-hex", identifier="x", relay="wss://x") is None
