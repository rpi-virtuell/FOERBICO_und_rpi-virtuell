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


def test_show_events_prints_the_built_event_as_json(content, capsys, monkeypatch):
    """Damit nachsehbar ist, was das Werkzeug tatsaechlich senden wuerde."""
    import cli
    from models import Outcome, PostResult

    ereignis = {"kind": 30023, "tags": [["d", "erster"]], "content": "Ein Absatz.\n"}
    monkeypatch.setattr(
        cli, "publish_post",
        lambda raw, *, path, **kw: PostResult(
            path=path, outcome=Outcome.PUBLISHED, slug="erster", article=ereignis
        ),
    )

    main(["--all", "--dry-run", "--show-events", "--content-root", str(content),
          "--pubkey", "a" * 64])

    ausgabe = capsys.readouterr().out
    assert '"kind": 30023' in ausgabe
    assert '"d"' in ausgabe


def test_a_log_file_records_every_post_machine_readable(content, tmp_path, monkeypatch):
    """Das Log-Artefakt der CI: vollstaendig, auch was die Summary kuerzt."""
    import json

    import cli
    from models import Finding, Outcome, PostResult, Severity

    befund = Finding(severity=Severity.ERROR, origin="NIP-23", message="HTML im content",
                     lines=[70], found=["<br>"])
    monkeypatch.setattr(
        cli, "publish_post",
        lambda raw, *, path, **kw: PostResult(
            path=path, outcome=Outcome.FAILED, slug="x", reason="kaputt", findings=[befund]
        ),
    )
    log = tmp_path / "lauf.json"

    main(["--all", "--dry-run", "--log", str(log), "--content-root", str(content),
          "--pubkey", "a" * 64])

    eintraege = json.loads(log.read_text(encoding="utf-8"))
    assert len(eintraege) == 2
    assert eintraege[0]["outcome"] == "fehlgeschlagen"
    assert eintraege[0]["findings"][0]["lines"] == [70]
    assert eintraege[0]["findings"][0]["origin"] == "NIP-23"


def test_every_option_explains_itself_in_the_help():
    """`--help` ist die Dokumentation, die immer mitkommt — ohne Luecken."""
    from cli import build_parser

    ohne_hilfe = [
        aktion.option_strings
        for aktion in build_parser()._actions
        if not aktion.help and aktion.option_strings
    ]

    assert ohne_hilfe == [], f"Optionen ohne Hilfetext: {ohne_hilfe}"


def test_a_published_post_gets_its_nostr_address(content, capsys, monkeypatch):
    """Ohne naddr bleibt der Bericht ohne Links — gebaut, aber nie verdrahtet.

    Die Links stehen nur im ausfuehrlichen Bericht; der knappe nennt publizierte
    Beitraege gar nicht.
    """
    import cli

    monkeypatch.setattr(cli, "publish_post", _ergebnis_fabrik(fehlschlag=False))
    monkeypatch.setattr(cli.nak, "encode_naddr", lambda **kwargs: "naddr1testadresse")

    main([
        "--all", "--dry-run", "--verbose",
        "--content-root", str(content), "--pubkey", "a" * 64,
    ])

    ausgabe = capsys.readouterr().out
    assert "naddr1testadresse" in ausgabe
    assert "habla.news/a/naddr1testadresse" in ausgabe


def test_a_failing_address_encoding_does_not_break_the_run(content, capsys, monkeypatch):
    """Ein Darstellungsdetail darf keinen gruenen Lauf rot faerben."""
    import cli

    monkeypatch.setattr(cli, "publish_post", _ergebnis_fabrik(fehlschlag=False))
    monkeypatch.setattr(cli.nak, "encode_naddr", lambda **kwargs: None)

    assert main(["--all", "--dry-run", "--content-root", str(content), "--pubkey", "a" * 64]) == 0


def test_paths_in_the_report_stay_relative_to_the_repository(content, capsys, monkeypatch):
    """In der CI stuende sonst /home/runner/work/... in jeder Zeile."""
    import cli

    monkeypatch.chdir(content.parent)
    monkeypatch.setattr(cli, "publish_post", _ergebnis_fabrik(fehlschlag=True))

    main(["--all", "--content-root", str(content), "--pubkey", "a" * 64, "--dry-run"])

    assert str(content) not in capsys.readouterr().out


# --- Punkt 5: knapp ist die Vorgabe, --verbose macht es ausfuehrlich -------

def lauf_mit(args, content, monkeypatch, *, fehlschlag=False):
    import cli

    monkeypatch.setattr(cli, "publish_post", _ergebnis_fabrik(fehlschlag=fehlschlag))
    monkeypatch.setattr(cli.nak, "encode_naddr", lambda **kwargs: "naddr1testadresse")
    return main(["--all", "--dry-run", "--content-root", str(content),
                 "--pubkey", "a" * 64, *args])


def test_the_default_report_is_brief(content, capsys, monkeypatch):
    """In der CI soll nur eine Uebersicht stehen, keine 500 Zeilen."""
    lauf_mit([], content, monkeypatch)

    ausgabe = capsys.readouterr().out
    assert "| publiziert | 2 |" in ausgabe
    assert "### Publiziert" not in ausgabe
    assert "naddr1testadresse" not in ausgabe


def test_verbose_gives_the_full_report(content, capsys, monkeypatch):
    lauf_mit(["--verbose"], content, monkeypatch)

    ausgabe = capsys.readouterr().out
    assert "### Publiziert" in ausgabe
    assert "naddr1testadresse" in ausgabe


def test_every_post_gets_a_progress_line_before_the_report(content, capsys, monkeypatch):
    """Der Fortschritt muss waehrend der Arbeit erscheinen, nicht danach."""
    lauf_mit([], content, monkeypatch)

    ausgabe = capsys.readouterr().out
    fortschritt = [z for z in ausgabe.splitlines() if z.startswith("publiziert ")]
    assert len(fortschritt) == 2
    assert ausgabe.index("publiziert ") < ausgabe.index("## Nostr-Sync")


def test_a_progress_line_names_path_and_slug(content, capsys, monkeypatch):
    lauf_mit([], content, monkeypatch)

    erste = capsys.readouterr().out.splitlines()[0]
    assert "index.md" in erste and erste.endswith("x")


def test_the_brief_report_still_names_a_failure(content, capsys, monkeypatch):
    """Knapp heisst nicht, Probleme zu verschweigen."""
    code = lauf_mit([], content, monkeypatch, fehlschlag=True)

    ausgabe = capsys.readouterr().out
    assert code == 1
    assert "[!CAUTION]" in ausgabe
    assert "fehlgeschlagen " in ausgabe, "auch der Fortschritt muss es zeigen"
