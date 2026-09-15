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
    else:
        posts = [Path(p) for p in args.paths]

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

    summary = render_summary(results)
    print(summary)
    _write_step_summary(summary)

    return 1 if any(r.outcome is Outcome.FAILED for r in results) else 0


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publiziert Markdown-Beitraege nach Nostr.")
    parser.add_argument("paths", nargs="*", help="einzelne index.md-Dateien")
    parser.add_argument("--all", action="store_true", help="alle Beitraege unter --content-root")
    parser.add_argument("--dry-run", action="store_true", help="entscheiden, aber nichts senden")
    parser.add_argument("--content-root", default=str(DEFAULT_CONTENT_ROOT))
    parser.add_argument("--pubkey", default="", help="sonst aus AUTHOR_PUBKEY_HEX")
    parser.add_argument("--relay", action="append", help="mehrfach angebbar")
    parser.add_argument("--amb-relay", default=AMB_RELAY)
    return parser.parse_args(argv)


def _write_step_summary(summary: str) -> None:
    """Schreibt die Zusammenfassung zusaetzlich in die GitHub-Job-Summary."""
    ziel = os.environ.get("GITHUB_STEP_SUMMARY")
    if not ziel:
        return
    with open(ziel, "a", encoding="utf-8") as datei:
        datei.write(summary + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
