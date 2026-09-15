"""Prueft, was die Veroeffentlichung eines Beitrags blockiert.

Beantwortet genau eine Frage: Verletzt dieser Beitrag eine fremde Spezifikation
(NIP-01, NIP-23, NIP-94) so, dass er nicht publiziert werden darf?

Warum blockierend: kind:30023 und kind:30142 sind ersetzbar. Ein fehlerhaftes
Event loescht die funktionierende Vorversion auf dem Relay. Nicht publizieren ist
dann besser als publizieren.

Tut ausdruecklich NICHT: eigene Konventionen pruefen (das ist warning_checks),
Events bauen, publizieren.
"""

import re

from models import Finding, Severity

# Tag-artige Muster: `<br>`, `</br>`, `<div class="x">`. Bewusst grob — im
# Fliesstext eines Blogbeitrags gibt es keinen legitimen Grund fuer spitze
# Klammern um einen Bezeichner.
HTML_TAG = re.compile(r"</?[a-zA-Z][a-zA-Z0-9]*(?:\s[^>]*)?/?>")

CODE_FENCE = "```"


def check_html(content: str, first_line: int = 1) -> list[Finding]:
    """NIP-23 verbietet HTML im Markdown — das gilt auch fuer ein einzelnes `<br>`.

    `first_line` ist die Dateizeile, in der `content` beginnt. Ohne sie meldet der
    Befund Zeilennummern des Fliesstexts, die im Editor ins Leere zeigen.
    """
    lines: list[int] = []
    found: list[str] = []
    for number, line in _lines_outside_code_blocks(content, first_line):
        tags = HTML_TAG.findall(line)
        if not tags:
            continue
        lines.append(number)
        found.extend(tag for tag in tags if tag not in found)

    if not lines:
        return []

    return [
        Finding(
            severity=Severity.ERROR,
            origin="NIP-23",
            message="HTML im content",
            rule='NIP-23 — "MUST NOT support adding HTML to Markdown"',
            fix="Tag entfernen; fuer einen Absatz eine Leerzeile setzen.",
            lines=lines,
            found=found,
        )
    ]


def _lines_outside_code_blocks(content: str, first_line: int):
    """Zeilennummer und Text, Codebloecke ausgelassen.

    In einem Codeblock ist HTML gezeigter Inhalt, kein Formatierungsversuch.
    """
    inside = False
    for number, line in enumerate(content.split("\n"), start=first_line):
        if line.lstrip().startswith(CODE_FENCE):
            inside = not inside
            continue
        if not inside:
            yield number, line
