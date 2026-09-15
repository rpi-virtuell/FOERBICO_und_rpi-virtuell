from textwrap import dedent

import pytest

from cli import discover_posts, main

VOLLSTAENDIG = dedent("""\
    ---
    # commonMetadata
    id: https://oer.community/{slug}
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


@pytest.fixture
def content(tmp_path):
    """Ein kleiner Content-Baum, damit der Test nichts Echtes anfasst."""
    for slug in ("erster", "zweiter"):
        ordner = tmp_path / "de" / "posts" / slug
        ordner.mkdir(parents=True)
        (ordner / "index.md").write_text(VOLLSTAENDIG.format(slug=slug), encoding="utf-8")
    (tmp_path / "de" / "posts" / "erster" / "beiwerk.md").write_text("kein Beitrag", encoding="utf-8")
    return tmp_path


def test_discovery_finds_every_index_md_and_nothing_else(content):
    gefunden = discover_posts(content)

    assert [p.parent.name for p in gefunden] == ["erster", "zweiter"]


def test_a_dry_run_needs_no_signer_and_changes_nothing(content, capsys):
    code = main([
        "--all", "--dry-run", "--content-root", str(content),
        "--pubkey", "a" * 64, "--relay", "ws://127.0.0.1:9",
    ])

    assert code != 0, "ein unerreichbares Relay muss auffallen"
    assert "Nostr-Sync" in capsys.readouterr().out


def test_a_failing_post_makes_the_run_red(content, capsys, monkeypatch):
    import cli

    monkeypatch.setattr(cli, "publish_post", _ergebnis_fabrik(fehlschlag=True))

    assert main(["--all", "--dry-run", "--content-root", str(content), "--pubkey", "a" * 64]) == 1


def test_a_clean_run_is_green(content, capsys, monkeypatch):
    import cli

    monkeypatch.setattr(cli, "publish_post", _ergebnis_fabrik(fehlschlag=False))

    assert main(["--all", "--dry-run", "--content-root", str(content), "--pubkey", "a" * 64]) == 0


def _ergebnis_fabrik(*, fehlschlag: bool):
    from models import Outcome, PostResult

    def erzeuge(raw, *, path, **kwargs):
        ausgang = Outcome.FAILED if fehlschlag else Outcome.PUBLISHED
        return PostResult(path=path, outcome=ausgang, slug="x", reason="Test")

    return erzeuge


def test_the_default_content_root_does_not_depend_on_the_working_directory():
    """Ein relativer Vorgabepfad findet nur aus einem Verzeichnis etwas."""
    from cli import DEFAULT_CONTENT_ROOT

    assert DEFAULT_CONTENT_ROOT.is_absolute()


def test_asking_for_all_posts_but_finding_none_is_an_error(tmp_path, capsys):
    """Ein gruener Lauf, der nichts getan hat, ist die gefaehrlichste Ausgabe.

    Genau dieser Fall — Dateien erwartet, nichts bearbeitet, Job gruen — ist der
    Grund fuer diesen Umbau. Er darf im eigenen Werkzeug nicht auftreten.
    """
    leer = tmp_path / "leer"
    leer.mkdir()

    code = main(["--all", "--dry-run", "--content-root", str(leer), "--pubkey", "a" * 64])

    assert code != 0
    assert "keine" in capsys.readouterr().err.lower()


def test_calling_without_any_work_is_a_usage_error(capsys):
    """Ohne --all und ohne Pfade gibt es keinen Auftrag.

    Dritte Variante derselben Falle: „nichts zu tun" mit Exit 0 sieht aus wie
    Erfolg. Wer das Werkzeug ohne Argumente ruft, hat sich vertippt.
    """
    code = main(["--dry-run", "--pubkey", "a" * 64])

    assert code == 2
    assert "--all" in capsys.readouterr().err
