import hashlib

import pytest

from images import local_files, sync_images
from references import ImageReference

BLOSSOM = "https://blossom.edufeed.org"
BILD = b"\x89PNG\r\n\x1a\n" + b"beispielhafte Bilddaten"
HASH = hashlib.sha256(BILD).hexdigest()

EINTRAG = {
    "title": "Ein Titelbild",
    "alt": "Beschreibung des Bildes",
    "author": "FOERBICO",
    "licenceUrl": "https://creativecommons.org/licenses/by/4.0/",
}


@pytest.fixture
def beitrag(tmp_path):
    """Ein Beitragsordner mit einer Bilddatei, deren Hash zur URL passt."""
    (tmp_path / "titelbild.png").write_bytes(BILD)
    return tmp_path


def referenz(image_hash=HASH):
    return ImageReference(hash=image_hash, url=f"{BLOSSOM}/{image_hash}.png")


def lauf(beitrag, *, entries=None, blob_da=True, vorhanden=None, **kwargs):
    """Fuehrt sync_images mit erfundener Aussenwelt aus."""
    hochgeladen, gesendet = [], []

    ergebnis = sync_images(
        [referenz()], entries if entries is not None else {"titelbild.png": EINTRAG},
        beitrag,
        pubkey="a" * 64, signer="sec", relays=["wss://relay"], blossom=BLOSSOM,
        has_blob=lambda h, server: blob_da,
        upload=lambda pfad, server, signer: hochgeladen.append(pfad),
        fetch=lambda **kw: vorhanden,
        send=lambda event, relay, signer: gesendet.append(event) or True,
        **kwargs,
    )
    return ergebnis, hochgeladen, gesendet


def test_local_files_are_found_by_their_hash(beitrag):
    dateien = local_files(beitrag)

    assert dateien[HASH].name == "titelbild.png"
    assert dateien[HASH].size == len(BILD)
    assert dateien[HASH].mime == "image/png"


def test_an_image_with_licence_gets_its_attestation(beitrag):
    _, _, gesendet = lauf(beitrag)

    assert len(gesendet) == 1
    assert gesendet[0]["kind"] == 1063
    assert ["x", HASH] in gesendet[0]["tags"]


def test_a_missing_blob_is_uploaded_first(beitrag):
    _, hochgeladen, _ = lauf(beitrag, blob_da=False)

    assert [p.name for p in hochgeladen] == ["titelbild.png"]


def test_a_missing_blob_without_a_local_file_is_only_reported(tmp_path):
    """Die Datei liegt nicht im Ordner — hochladen koennen wir nichts."""
    ergebnis, hochgeladen, _ = lauf(tmp_path, blob_da=False)

    assert hochgeladen == []
    assert any("Blob" in f.message for f in ergebnis.findings)


def test_an_image_without_an_entry_is_reported_not_attested(beitrag):
    ergebnis, _, gesendet = lauf(beitrag, entries={})

    assert gesendet == []
    assert any("bilder" in f.message for f in ergebnis.findings)


def test_an_entry_without_a_licence_url_gets_no_attestation(beitrag):
    ergebnis, _, gesendet = lauf(beitrag, entries={"titelbild.png": {"title": "Ohne Lizenz"}})

    assert gesendet == []
    assert any("licenceUrl" in f.message for f in ergebnis.findings)


def test_an_identical_attestation_is_not_republished(beitrag):
    _, _, gesendet = lauf(beitrag)
    ergebnis, _, nochmal = lauf(beitrag, vorhanden=gesendet[0])

    assert nochmal == []


def test_a_stale_local_file_leaves_the_attestation_alone(tmp_path):
    """Realfall nostr-schrein: Die Datei wurde nach dem Attestieren neu kodiert.

    Ohne passende Datei kennen wir die Groesse nicht. Ein Neuaufbau haette
    strikt weniger Information — und kind:1063 ist nicht ersetzbar, jedes
    Publizieren legt also ein Duplikat an.
    """
    (tmp_path / "anderes-encoding.png").write_bytes(b"voellig andere Bytes")
    vorhandener = {"kind": 1063, "tags": [["x", HASH], ["size", "146385"]], "content": ""}
    # Im echten Beitrag steht der Eintrag unter der Hash-URL, nicht unter dem
    # Dateinamen — sonst waere er ohne passende Datei gar nicht auffindbar.
    unter_url = {f"{BLOSSOM}/{HASH}.png": EINTRAG}

    ergebnis, _, gesendet = lauf(tmp_path, entries=unter_url, vorhanden=vorhandener)

    assert gesendet == []
    assert any("passt nicht" in f.message for f in ergebnis.findings)


def test_an_attestation_from_another_client_is_left_alone(beitrag):
    """Der Edufeed-Browser-Editor erzeugt eine andere Form, erkennbar am client-Tag.

    Wuerden wir darueber publizieren, kaeme beim naechsten Editor-Lauf das
    Gegenteil — ein Pingpong aus Duplikaten, die keiner Quelle zuzuordnen sind.
    """
    fremder = {"kind": 1063, "tags": [["x", HASH], ["client", "Edufeed"]], "content": ""}

    ergebnis, _, gesendet = lauf(beitrag, vorhanden=fremder)

    assert gesendet == []
    assert any("client" in f.message for f in ergebnis.findings)


def test_a_dry_run_uploads_nothing_and_sends_nothing(beitrag):
    ergebnis, hochgeladen, gesendet = lauf(beitrag, blob_da=False, dry_run=True)

    assert hochgeladen == [] and gesendet == []
    assert ergebnis.would_upload == 1
    assert ergebnis.would_attest == 1
