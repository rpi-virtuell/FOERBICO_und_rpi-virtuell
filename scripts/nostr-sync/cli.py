"""Einstiegspunkt: Argumente lesen, verdrahten, Exit-Code setzen.

Beantwortet genau eine Frage: Welche Beitraege sollen bearbeitet werden, und wie
ging es aus?

Tut ausdruecklich NICHT: entscheiden (das ist `publish`), Events bauen,
berichten (das ist `report`).

Die Ausgabe ist knapp gehalten — fuer einen CI-Lauf zaehlen Zaehler und
Probleme. `--verbose` schaltet den ausfuehrlichen Bericht ein. Ueber den Umfang
entscheidet allein dieses Flag, nie die Umgebung.

Aufruf:
    python cli.py --all --dry-run
    python cli.py --all --dry-run --verbose
    python cli.py Website/content/de/posts/ein-beitrag/index.md
"""

import argparse
import dataclasses
import json
import os
import sys
import traceback
from pathlib import Path

import nak
from models import Outcome, PostResult
from publish import ARTICLE, publish_post
from report import progress_line, render_brief, render_summary

ARTICLE_RELAYS = ["wss://relay-rpi.edufeed.org/"]
AMB_RELAY = "wss://amb-relay.edufeed.org/"
# Relativ zum Skript, nicht zum Arbeitsverzeichnis: Ein relativer Vorgabepfad
# findet nur aus einem Verzeichnis etwas und laeuft sonst still ins Leere.
DEFAULT_CONTENT_ROOT = (Path(__file__).resolve().parent / ".." / ".." / "Website" / "content").resolve()


def discover_posts(root: Path) -> list[Path]:
    """Alle `index.md` unterhalb von `root`, in stabiler Reihenfolge."""
    return sorted(root.rglob("index.md"))


def shorten(path: Path) -> str:
    """Der Pfad relativ zum Arbeitsverzeichnis, wenn er darunter liegt.

    Sonst stuende in jeder Berichtszeile der Laufpfad der CI
    (`/home/runner/work/…`) — dreimal so lang und fuer niemanden von Nutzen.
    """
    try:
        return str(path.resolve().relative_to(Path.cwd()))
    except ValueError:
        return str(path)


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

    if args.dry_run:
        print("PROBELAUF (--dry-run) — es wird nichts gesendet", flush=True)

    relays = args.relay or ARTICLE_RELAYS
    results = _work_through(posts, pubkey=pubkey, signer=signer, relays=relays, args=args)

    _add_addresses(results, pubkey=pubkey, relay=relays[0])

    if args.show_events:
        _print_events(results)

    stufe = render_summary if args.verbose else render_brief
    bericht = stufe(results, dry_run=args.dry_run)
    print(bericht)
    _write_step_summary(bericht)

    if args.log:
        _write_log(results, Path(args.log))

    return 1 if any(r.outcome is Outcome.FAILED for r in results) else 0


def _work_through(posts: list[Path], *, pubkey: str, signer: str, relays: list[str], args) -> list:
    """Arbeitet die Beitraege ab und meldet jeden sofort.

    Die Ausgabe erfolgt **waehrend** der Arbeit, nicht danach: Ein Lauf ueber 96
    Beitraege fragt fuer jeden die Relays ab und braucht Minuten. Ohne Zeile je
    Beitrag liesse sich nicht unterscheiden, ob er arbeitet oder haengt.

    `flush=True` ist dabei keine Zier: In der CI ist die Standardausgabe kein
    Terminal, Python puffert dann 8 KB — der ganze „Fortschritt" erschiene erst
    am Prozessende.
    """
    results = []
    for path in posts:
        try:
            result = publish_post(
                path.read_text(encoding="utf-8", errors="replace"),
                path=shorten(path),
                pubkey=pubkey,
                signer=signer,
                relays=relays,
                amb_relay=args.amb_relay,
                dry_run=args.dry_run,
            )
        except Exception as abbruch:
            results.append(_abbruch(path, abbruch))
            print(progress_line(results[-1]), flush=True)
            break
        results.append(result)
        print(progress_line(result), flush=True)
    return results


def _abbruch(path: Path, fehler: Exception) -> PostResult:
    """Macht aus einem unerwarteten Fehler ein Ergebnis und haelt an.

    Ohne das faellt die Ausnahme durch `main()` durch, und es gibt **weder
    Bericht noch Protokoll** — in der CI laeuft der Artefakt-Schritt dann in
    `if-no-files-found: warn`, es bleibt ein Stacktrace und sonst nichts.

    Angehalten wird bewusst (`break` beim Aufrufer): Ein unerwarteter Fehler
    heisst, dass eine Annahme nicht stimmt. Die uebrigen Beitraege unter dieser
    Annahme zu publizieren waere schlechter als anzuhalten.

    Der Stacktrace geht nach stderr — im Bericht steht die Art des Fehlers,
    fuer die Entwicklung braucht es die Zeilen.
    """
    traceback.print_exc(file=sys.stderr)
    return PostResult(
        path=shorten(path),
        outcome=Outcome.FAILED,
        reason=f"unerwarteter Abbruch: {type(fehler).__name__}: {fehler}",
    )


def _add_addresses(results: list, *, pubkey: str, relay: str) -> None:
    """Ergaenzt je Beitrag die NIP-19-Adresse fuer die Links im Bericht.

    Auch im Dry-Run: Die Adresse ist eine reine Umrechnung aus Kind, Pubkey und
    Slug — kein Netz, keine Wirkung. Gerade beim Probelauf ist sie das, womit
    sich nachsehen laesst, welches Event gemeint ist.

    Schlaegt das Encoding fehl, bleibt `naddr` leer und der Lauf gueltig: Ein
    Darstellungsdetail darf keinen gruenen Lauf rot faerben.
    """
    for result in results:
        if result.slug is None:
            continue
        result.naddr = nak.encode_naddr(
            kind=ARTICLE, pubkey=pubkey, identifier=result.slug, relay=relay
        )


def build_parser() -> argparse.ArgumentParser:
    """Die Kommandozeile an einer Stelle — auch fuer Tests und `--help`."""
    parser = argparse.ArgumentParser(description="Publiziert Markdown-Beitraege nach Nostr.")
    parser.add_argument("paths", nargs="*", help="einzelne index.md-Dateien")
    parser.add_argument("--all", action="store_true", help="alle Beitraege unter --content-root")
    parser.add_argument("--dry-run", action="store_true", help="entscheiden, aber nichts senden")
    parser.add_argument(
        "--verbose", action="store_true",
        help="ausfuehrlicher Bericht statt Kurzfassung (publizierte Beitraege, "
             "Adressen, Aenderungen, Warnungen im Einzelnen)",
    )
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
