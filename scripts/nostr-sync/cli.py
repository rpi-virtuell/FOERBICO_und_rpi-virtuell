"""Einstiegspunkt: Argumente lesen, verdrahten, Exit-Code setzen.

Beantwortet genau eine Frage: Welche Beitraege sollen bearbeitet werden, und wie
ging es aus?

Tut ausdruecklich NICHT: entscheiden (das ist `publish`), Events bauen,
berichten (das ist `report`).

Aufruf:
    python cli.py --all --dry-run
    python cli.py Website/content/de/posts/ein-beitrag/index.md
"""

import argparse
import dataclasses
import json
import os
import sys
from pathlib import Path

from models import Outcome
from publish import publish_post
from report import render_summary

ARTICLE_RELAYS = ["wss://relay-rpi.edufeed.org/"]
AMB_RELAY = "wss://amb-relay.edufeed.org/"
# Relativ zum Skript, nicht zum Arbeitsverzeichnis: Ein relativer Vorgabepfad
# findet nur aus einem Verzeichnis etwas und laeuft sonst still ins Leere.
DEFAULT_CONTENT_ROOT = (Path(__file__).resolve().parent / ".." / ".." / "Website" / "content").resolve()


def discover_posts(root: Path) -> list[Path]:
    """Alle `index.md` unterhalb von `root`, in stabiler Reihenfolge."""
    return sorted(root.rglob("index.md"))


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    if args.all:
        wurzel = Path(args.content_root)
        posts = discover_posts(wurzel)
        if not posts:
            print(
                f"Keine index.md unter {wurzel} gefunden. Mit --all ist das ein Fehler: "
                "Ein gruener Lauf, der nichts bearbeitet hat, verdeckt genau die "
                "Stoerung, die er melden soll.",
                file=sys.stderr,
            )
            return 2
    elif args.paths:
        posts = [Path(p) for p in args.paths]
    else:
        print(
            "Kein Auftrag: weder --all noch Pfade angegeben. "
            "Beispiel: cli.py --all --dry-run",
            file=sys.stderr,
        )
        return 2

    pubkey = args.pubkey or os.environ.get("AUTHOR_PUBKEY_HEX", "")
    signer = os.environ.get("BUNKER_URL", "")
    if not pubkey:
        print("AUTHOR_PUBKEY_HEX fehlt — ohne ihn ist der Idempotenz-Check blind.", file=sys.stderr)
        return 2
    if not signer and not args.dry_run:
        print("BUNKER_URL fehlt — ohne Signer kann nichts publiziert werden.", file=sys.stderr)
        return 2

    relays = args.relay or ARTICLE_RELAYS
    results = [
        publish_post(
            path.read_text(encoding="utf-8", errors="replace"),
            path=str(path),
            pubkey=pubkey,
            signer=signer,
            relays=relays,
            amb_relay=args.amb_relay,
            dry_run=args.dry_run,
        )
        for path in posts
    ]

    if args.show_events:
        _print_events(results)

    summary = render_summary(results)
    print(summary)
    _write_step_summary(summary)

    if args.log:
        _write_log(results, Path(args.log))

    return 1 if any(r.outcome is Outcome.FAILED for r in results) else 0


def build_parser() -> argparse.ArgumentParser:
    """Die Kommandozeile an einer Stelle — auch fuer Tests und `--help`."""
    parser = argparse.ArgumentParser(description="Publiziert Markdown-Beitraege nach Nostr.")
    parser.add_argument("paths", nargs="*", help="einzelne index.md-Dateien")
    parser.add_argument("--all", action="store_true", help="alle Beitraege unter --content-root")
    parser.add_argument("--dry-run", action="store_true", help="entscheiden, aber nichts senden")
    parser.add_argument(
        "--content-root", default=str(DEFAULT_CONTENT_ROOT),
        help="Wurzel der Beitraege fuer --all (Vorgabe: Website/content im Repo)",
    )
    parser.add_argument("--pubkey", default="", help="sonst aus AUTHOR_PUBKEY_HEX")
    parser.add_argument(
        "--relay", action="append",
        help="Relay fuer kind:30023, mehrfach angebbar (Vorgabe: relay-rpi.edufeed.org)",
    )
    parser.add_argument(
        "--amb-relay", default=AMB_RELAY, help="Relay fuer die AMB-Metadaten (kind:30142)",
    )
    parser.add_argument(
        "--show-events", action="store_true",
        help="die gebauten Events als JSON ausgeben — zeigt, was gesendet wuerde",
    )
    parser.add_argument(
        "--log", default="",
        help="Ergebnisse maschinenlesbar in diese JSON-Datei schreiben (CI-Artefakt)",
    )
    return parser


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    return build_parser().parse_args(argv)


def _print_events(results: list) -> None:
    """Gibt jedes gebaute Event aus, damit nachsehbar ist, was gesendet wuerde."""
    for result in results:
        if result.article is None:
            continue
        print(f"─── {result.path} — {result.outcome.value} ───")
        print(json.dumps(result.article, ensure_ascii=False, indent=2))
        print()


def _write_log(results: list, ziel: Path) -> None:
    """Das vollstaendige Ergebnis als JSON — auch was die Summary kuerzt.

    Bewusst maschinenlesbar und komplett: Die Summary ist fuer Menschen gemacht
    und laesst weg, das Log soll hinterher jede Frage beantworten koennen.
    """
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(
        json.dumps([_als_dict(r) for r in results], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _als_dict(result) -> dict:
    eintrag = dataclasses.asdict(result)
    eintrag["outcome"] = result.outcome.value
    for befund, roh in zip(eintrag["findings"], result.findings):
        befund["severity"] = roh.severity.value
    return eintrag


def _write_step_summary(summary: str) -> None:
    """Schreibt die Zusammenfassung zusaetzlich in die GitHub-Job-Summary."""
    ziel = os.environ.get("GITHUB_STEP_SUMMARY")
    if not ziel:
        return
    with open(ziel, "a", encoding="utf-8") as datei:
        datei.write(summary + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
