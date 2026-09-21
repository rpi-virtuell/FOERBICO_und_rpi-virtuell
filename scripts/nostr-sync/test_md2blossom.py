"""Abnahmekriterium: unsere kind:1063 sind zeichengleich zu md2blossom.mjs.

Solange beide Werkzeuge existieren, publizieren sie Lizenznachweise unter
demselben Pubkey und in derselben Tag-Form. kind:1063 ist **nicht ersetzbar** —
weichen die Tags voneinander ab, legt jedes Werkzeug seine eigene Variante dazu,
und die Duplikate sind hinterher keiner Quelle mehr zuzuordnen.

Dieser Test ist deshalb Pflicht, nicht Kuer. Er faellt erst mit `md2blossom` weg.

Eigene Datei statt in `test_events.py`, weil er die Aussenwelt braucht: `node`,
die npm-Abhaengigkeiten unter `Website/scripts/` und die echten Bilddateien aus
`Website/content/`. `test_events.py` bleibt hermetisch und schnell.

Lokal wird uebersprungen, wenn `node` oder die Abhaengigkeiten fehlen
(`cd Website/scripts && npm ci`) — **in der CI ist er Pflicht und darf nicht
uebersprungen werden.**
"""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from frontmatter import parse_post
from images import local_files, sync_images
from references import image_references

REPO = Path(__file__).resolve().parents[2]
MD2BLOSSOM = REPO / "Website" / "scripts" / "md2blossom.mjs"
NODE_MODULES = REPO / "Website" / "scripts" / "node_modules"
CONTENT = REPO / "Website" / "content"
BLOSSOM = "https://blossom.edufeed.org"

# Gemessen am 2026-09-21: 33 Bilder in 16 Beitraegen. Die Schranke faengt den
# Fall ab, dass eine Seite nichts mehr baut — dann waere der Vergleich leer
# und der Test gruen, ohne etwas zu beweisen.
MINDESTENS_VERGLICHEN = 30

pytestmark = [
    pytest.mark.md2blossom,
    pytest.mark.skipif(shutil.which("node") is None, reason="node fehlt"),
    pytest.mark.skipif(
        not NODE_MODULES.is_dir(),
        reason="npm-Abhaengigkeiten fehlen — `cd Website/scripts && npm ci`",
    ),
]


def posts_with_image_block() -> list[Path]:
    """Nur Beitraege mit `# bilder`-Block — nur dort entsteht ueberhaupt ein 1063."""
    if not CONTENT.is_dir():
        return []
    return [
        pfad.parent
        for pfad in sorted(CONTENT.rglob("index.md"))
        if "\n# bilder" in pfad.read_text(encoding="utf-8")
    ]


POSTS = posts_with_image_block()


@pytest.fixture(scope="session")
def attestations(tmp_path_factory) -> dict[str, tuple[dict, dict]]:
    """Je Beitrag beide Nachweis-Saetze, einmal fuer die ganze Sitzung gebaut.

    `md2blossom` startet je Beitrag einen node-Prozess; das dreimal zu tun waere
    verschwendete Laufzeit ohne zusaetzliche Aussage.
    """
    gebaut = {}
    for post_dir in POSTS:
        ausgabe = tmp_path_factory.mktemp("md2blossom")
        gebaut[post_dir.name] = (
            our_attestations(post_dir),
            md2blossom_attestations(post_dir, ausgabe),
        )
    return gebaut


@pytest.mark.parametrize("post_dir", POSTS, ids=lambda p: p.name)
def test_1063_byte_identical_to_md2blossom(post_dir, attestations):
    """Fuer jedes Bild, das beide Werkzeuge attestieren, muessen die Tags gleich sein."""
    unsere, fremde = attestations[post_dir.name]

    for image_hash in sorted(set(unsere) & set(fremde)):
        assert unsere[image_hash] == fremde[image_hash], (
            f"{post_dir.name}, Bild {image_hash[:8]}: Tags weichen ab"
        )


def test_the_comparison_covers_enough_images(attestations):
    """Sonst waere der Test auch dann gruen, wenn eine Seite gar nichts mehr baut."""
    verglichen = sum(len(set(u) & set(f)) for u, f in attestations.values())

    assert verglichen >= MINDESTENS_VERGLICHEN, f"nur {verglichen} Bilder verglichen"


def test_we_skip_an_attestation_only_without_a_matching_local_file(attestations):
    """Die einzige erlaubte Abweichung: wir bauen einen Nachweis *nicht*.

    Realfall `2025-07-02-nostr-schrein`: Die Bilddatei wurde nach dem Attestieren
    neu kodiert, ihr Hash passt nicht mehr zur URL. `md2blossom` baut trotzdem
    einen Nachweis — ohne `size`, weil es die Datei nicht findet. Wir lassen den
    vorhandenen in Ruhe, statt ein Duplikat mit weniger Angaben anzulegen.

    Umgekehrt darf es nichts geben: Ein Nachweis, den nur wir bauen, waere eine
    echte Divergenz.
    """
    for name, (unsere, fremde) in attestations.items():
        post_dir = next(p for p in POSTS if p.name == name)
        vorhandene_dateien = local_files(post_dir)

        for image_hash in set(fremde) - set(unsere):
            assert image_hash not in vorhandene_dateien, (
                f"{name}: wir bauen keinen Nachweis fuer {image_hash[:8]}, "
                "obwohl die passende Datei im Ordner liegt"
            )
        assert not set(unsere) - set(fremde), (
            f"{name}: wir bauen Nachweise, die md2blossom nicht baut — "
            f"{sorted(set(unsere) - set(fremde))}"
        )


def our_attestations(post_dir: Path) -> dict[str, list]:
    """Die Nachweise, die unser Bilder-Schritt bauen wuerde, nach Bild-Hash.

    Bewusst ueber `sync_images` und nicht ueber `build_attestation` direkt: So
    laeuft dieselbe Strecke wie im Betrieb, samt der Entscheidung, zu welchen
    Bildern ueberhaupt ein Nachweis entsteht. Die Aussenwelt ist erfunden — der
    Blob gilt als vorhanden, auf dem Relay liegt nichts.
    """
    post = parse_post((post_dir / "index.md").read_text(encoding="utf-8"))
    gesendet = []

    sync_images(
        image_references(post.metadata.get("image"), post.content),
        post.images,
        post_dir,
        pubkey="0" * 64,
        signer="sec",
        relays=["wss://relay-im-test"],
        blossom=BLOSSOM,
        has_blob=lambda image_hash, server: True,
        upload=lambda pfad, server, signer: None,
        fetch=lambda **kwargs: None,
        send=lambda event, relay, signer: gesendet.append(event) or True,
    )
    return {hash_of(event): event["tags"] for event in gesendet}


def md2blossom_attestations(post_dir: Path, ausgabe: Path) -> dict[str, list]:
    """Dasselbe aus `md2blossom.mjs`, nach Bild-Hash.

    Auf einer Kopie und mit `--out`, damit der Lauf den Beitrag im Repo nicht
    anfasst: `md2blossom` schreibt sonst Markdown und Frontmatter um.
    """
    kopie = ausgabe / post_dir.name
    shutil.copytree(post_dir, kopie)
    ziel = ausgabe / "out"

    lauf = subprocess.run(
        ["node", str(MD2BLOSSOM), str(kopie), "--out", str(ziel)],
        stdin=subprocess.DEVNULL, capture_output=True, text=True, check=False,
    )
    # Exit 2 heisst „Bild ohne Eintrag im `# bilder`-Block" (TODO:LICENSE). Die
    # uebrigen Nachweise schreibt das Skript trotzdem — genau die wollen wir.
    assert lauf.returncode in (0, 2), f"md2blossom scheiterte: {lauf.stderr}"

    nachweise = {}
    for datei in sorted(ziel.glob("*.1063.*.json")):
        event = json.loads(datei.read_text(encoding="utf-8"))
        nachweise[hash_of(event)] = event["tags"]
    return nachweise


def hash_of(event: dict) -> str:
    """Der `x`-Tag — nach ihm wird ein kind:1063 wiedererkannt (NIP-94)."""
    for tag in event["tags"]:
        if tag[0] == "x":
            return tag[1]
    raise AssertionError(f"kind:1063 ohne x-Tag: {event['tags']}")
