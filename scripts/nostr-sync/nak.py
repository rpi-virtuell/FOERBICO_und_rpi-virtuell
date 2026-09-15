"""Ruft das Werkzeug `nak` auf — die einzige Stelle mit Subprozessen.

Beantwortet genau eine Frage: Wie spreche ich mit Relays und dem Mediaserver?

Diese Datei ist die austauschbare Grenze. Faellt `nak` weg oder aendert Flags,
wird nur hier getauscht; die Domaenenlogik bleibt unberuehrt. Deshalb darf kein
reines Modul dieses hier importieren.

**stdin muss bei jedem Aufruf gesetzt sein.** Erbt `nak` ein Nicht-TTY-stdin — und
das tut es in jedem Skript-Subprozess — haelt es das fuer eine Pipe und bricht ab
mit `do not pass arguments when piping from stdin`. Deshalb gibt `_run` immer
etwas mit, notfalls nichts.

Tut ausdruecklich NICHT: Events bauen, Frontmatter lesen, entscheiden.
"""

import json
import subprocess

NAK = "nak"


class NakFailed(Exception):
    """Ein `nak`-Aufruf ist fehlgeschlagen, der nicht fehlschlagen durfte."""


def generate_key() -> str:
    return _run(["key", "generate"]).stdout.strip()


def public_key(secret: str) -> str:
    return _run(["key", "public", secret]).stdout.strip()


def fetch_event(
    kind: int, pubkey: str, relay: str, identifier: str | None = None, image_hash: str | None = None
) -> dict | None:
    """Das juengste Event zu diesem Filter, oder None.

    `pubkey` ist Pflicht und nicht bequem: Ohne ihn ginge ein fremdes Event zum
    selben Slug als „schon publiziert" durch, und unser Beitrag wuerde nie
    aktualisiert.

    Ein nicht erreichbares Relay wirft — „nichts gefunden" waere eine Luege, auf
    die hin entweder unnoetig publiziert oder faelschlich uebersprungen wuerde.
    """
    args = ["req", "-k", str(kind), "-a", pubkey, "-l", "1"]
    if identifier is not None:
        args += ["-d", identifier]
    if image_hash is not None:
        args += ["-t", f"x={image_hash}"]
    args.append(relay)

    result = _run(args)
    if result.returncode != 0:
        raise NakFailed(f"Relay {relay} nicht abfragbar: {result.stderr.strip()}")

    lines = [line for line in result.stdout.splitlines() if line.strip()]
    return json.loads(lines[0]) if lines else None


def publish(event: dict, relay: str, signer: str) -> bool:
    """Signiert das Event und schickt es an **ein** Relay.

    Ein Aufruf je Relay: So ist der Exit-Code die Antwort, und die Zahl der
    Bestaetigungen ergibt sich aus dem Zaehlen der Erfolge — ohne stderr zu parsen.

    `signer` ist ein Hex-Schluessel oder eine `bunker://`-URL; `nak` behandelt
    beides gleich.
    """
    result = _run(["event", "--sec", signer, relay], stdin=json.dumps(event))
    return result.returncode == 0


def _run(args: list[str], stdin: str | None = None) -> subprocess.CompletedProcess:
    """Ruft `nak` auf und setzt stdin **immer** explizit.

    Ohne Eingabe muss es `DEVNULL` sein, nicht der leere String. Eine leere Pipe
    liest `nak req` als Filter von stdin — und liefert dann stillschweigend
    **nichts** zurueck, mit Exit 0. Im Idempotenz-Check hiesse das „noch nicht
    publiziert", und der Sync wuerde bei jedem Lauf alles neu publizieren.
    Ein leerer String ist hier also nicht dasselbe wie keine Eingabe.
    """
    if stdin is None:
        return subprocess.run(
            [NAK, *args], stdin=subprocess.DEVNULL, capture_output=True, text=True, check=False
        )
    return subprocess.run(
        [NAK, *args], input=stdin, capture_output=True, text=True, check=False
    )


def blossom_has(image_hash: str, server: str) -> bool:
    """Liegt der Blob schon auf dem Mediaserver?

    `nak blossom check` beantwortet das ueber den Exit-Code: 0 gefunden,
    sonst nicht. Ein fehlender Blob ist kein Fehler, sondern der Normalfall
    vor dem ersten Upload.
    """
    return _run(["blossom", "-s", server, "check", image_hash]).returncode == 0


def blossom_upload(path, server: str, signer: str) -> dict:
    """Laedt eine Datei per BUD-01 hoch und gibt die Blob-Beschreibung zurueck.

    `nak` erledigt dabei das signierte kind:24242-Auth-Event. Schlaegt der Upload
    fehl, ist das ein echter Fehler — ohne Blob zeigt die Bild-URL im Beitrag ins
    Leere.

    Achtung: `-s` und `--sec` gehoeren an das Elternkommando `blossom`, vor das
    Unterkommando.
    """
    result = _run(["blossom", "-s", server, "--sec", signer, "upload", str(path)])
    if result.returncode != 0:
        raise NakFailed(f"Upload von {path} fehlgeschlagen: {result.stderr.strip()}")
    return json.loads(result.stdout.strip().splitlines()[0])


def encode_naddr(kind: int, pubkey: str, identifier: str, relay: str) -> str | None:
    """Die NIP-19-Adresse des Beitrags, zum Teilen und Nachsehen.

    Bewusst **nicht fatal**: Schlaegt das Encoding fehl, bleibt der Publish
    gueltig und die Summary vermerkt nur, dass die Adresse fehlt.

    `--relay` steht nicht in `nak encode naddr --help`, funktioniert aber und
    legt den Relay-Hinweis in den Code (gegen v0.17.3 geprueft). Bei einem
    Versionssprung erneut pruefen.
    """
    result = _run([
        "encode", "naddr", "-k", str(kind), "-p", pubkey, "-d", identifier, "--relay", relay
    ])
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None
