"""Bringt Blobs und Lizenznachweise zu den Bildern eines Beitrags in Ordnung.

Beantwortet genau eine Frage: Liegt zu jedem Bild der Blob auf dem Mediaserver
und ein passender Nachweis auf dem Relay?

Der Schritt blockiert den Artikel nie — Git ist die Wahrheit, die Bild-URL steht
schon im Beitrag. Was hier schiefgeht, wird gemeldet.

Die Aussenwelt kommt als Funktionsparameter herein, damit jede Verzweigung ohne
Mediaserver und Relay pruefbar ist.

Tut ausdruecklich NICHT: Artikel bauen, ueber den Beitrag entscheiden.
"""

import hashlib
import mimetypes
from dataclasses import dataclass, field
from pathlib import Path

import nak
from events import build_attestation, tags_equal
from models import Finding, Severity
from references import ImageReference, hash_from_url

FILE_METADATA = 1063
IMAGE_SUFFIXES = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".avif")

# Tags, die wir selbst nie schreiben. Traegt ein vorhandener Nachweis so einen,
# stammt er aus einem anderen Werkzeug — etwa dem Edufeed-Browser-Editor, der
# `client` setzt und dafuer `alt` und `authorUrl` weglaesst.
FOREIGN_TAGS = ("client",)


@dataclass
class LocalFile:
    name: str
    path: Path
    size: int
    mime: str | None


@dataclass
class ImageResult:
    findings: list[Finding] = field(default_factory=list)
    uploaded: int = 0
    attested: int = 0
    would_upload: int = 0
    would_attest: int = 0


def local_files(post_dir: Path) -> dict[str, LocalFile]:
    """Die Bilddateien des Beitragsordners, nach ihrem SHA-256."""
    gefunden: dict[str, LocalFile] = {}
    for datei in sorted(post_dir.iterdir()):
        if not datei.is_file() or datei.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        inhalt = datei.read_bytes()
        gefunden[hashlib.sha256(inhalt).hexdigest()] = LocalFile(
            name=datei.name,
            path=datei,
            size=len(inhalt),
            mime=mimetypes.guess_type(datei.name)[0],
        )
    return gefunden


def sync_images(
    references: list[ImageReference],
    entries: dict,
    post_dir: Path,
    *,
    pubkey: str,
    signer: str,
    relays: list[str],
    blossom: str,
    has_blob=nak.blossom_has,
    upload=nak.blossom_upload,
    fetch=nak.fetch_event,
    send=nak.publish,
    dry_run: bool = False,
) -> ImageResult:
    """Sorgt je Bild fuer Blob und Nachweis."""
    ergebnis = ImageResult()
    dateien = local_files(post_dir) if post_dir.is_dir() else {}

    for referenz in references:
        datei = dateien.get(referenz.hash)
        _ensure_blob(referenz, datei, ergebnis, blossom, signer, has_blob, upload, dry_run)
        _ensure_attestation(
            referenz, datei, entries, ergebnis,
            pubkey=pubkey, signer=signer, relays=relays,
            fetch=fetch, send=send, dry_run=dry_run,
        )
    return ergebnis


def _ensure_blob(referenz, datei, ergebnis, blossom, signer, has_blob, upload, dry_run) -> None:
    """Laedt die Datei hoch, wenn der Blob fehlt und wir sie haben."""
    if has_blob(referenz.hash, server=blossom):
        return
    if datei is None:
        ergebnis.findings.append(_warnung(
            f"Blob fehlt auf Blossom und keine Datei mit diesem Hash im Ordner "
            f"({referenz.url})"
        ))
        return
    if dry_run:
        ergebnis.would_upload += 1
        return
    upload(datei.path, server=blossom, signer=signer)
    ergebnis.uploaded += 1


def _ensure_attestation(
    referenz, datei, entries, ergebnis, *, pubkey, signer, relays, fetch, send, dry_run
) -> None:
    """Baut den Nachweis und publiziert ihn, wenn er sich geaendert hat."""
    eintrag = _entry_for(entries, referenz, datei)
    if eintrag is None:
        ergebnis.findings.append(_warnung(
            f"kein Eintrag im `# bilder`-Block fuer {datei.name if datei else referenz.url} "
            "— kein Nachweis"
        ))
        return
    if not eintrag.get("licenceUrl"):
        ergebnis.findings.append(_warnung(
            f"Eintrag fuer {datei.name if datei else referenz.url} ohne licenceUrl "
            "— kein Nachweis"
        ))
        return

    vorhanden = fetch(kind=FILE_METADATA, pubkey=pubkey, relay=relays[0], image_hash=referenz.hash)

    if datei is None:
        ergebnis.findings.append(_warnung(
            f"lokale Datei passt nicht zum attestierten Hash ({referenz.url}) — Nachweis "
            "bleibt unangetastet, sonst entstuende ein Duplikat mit weniger Angaben"
        ))
        return
    if vorhanden is not None and _from_another_tool(vorhanden):
        ergebnis.findings.append(_warnung(
            f"vorhandener Nachweis zu {datei.name} traegt einen `client`-Tag, stammt also "
            "aus einem anderen Werkzeug — bleibt unangetastet"
        ))
        return

    nachweis = build_attestation(
        referenz.url, referenz.hash, eintrag, mime=datei.mime, size=datei.size
    )
    if vorhanden is not None and tags_equal(nachweis, vorhanden):
        return
    if dry_run:
        ergebnis.would_attest += 1
        return
    for relay in relays:
        send(event=nachweis, relay=relay, signer=signer)
    ergebnis.attested += 1


def _entry_for(entries: dict, referenz: ImageReference, datei) -> dict | None:
    """Der Eintrag im `# bilder`-Block: unter Dateiname, URL oder passendem Hash."""
    if datei is not None and datei.name in entries:
        return entries[datei.name]
    if referenz.url in entries:
        return entries[referenz.url]
    for schluessel, eintrag in entries.items():
        if hash_from_url(schluessel) == referenz.hash:
            return eintrag
    return None


def _from_another_tool(vorhanden: dict) -> bool:
    return any(tag[0] in FOREIGN_TAGS for tag in vorhanden.get("tags", []))


def _warnung(text: str) -> Finding:
    return Finding(severity=Severity.WARNING, origin="FOERBICO-Konvention", message=text)
