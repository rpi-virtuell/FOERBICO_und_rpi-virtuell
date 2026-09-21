#!/usr/bin/env bash
#
# Waehlt aus, welche Beitraege der Sync ansieht, und schreibt sie zeilenweise
# nach posts.txt.
#
# Der Git-Diff ist ein Vorfilter fuer die Laufzeit, **kein**
# Korrektheitsmechanismus: Ob publiziert wird, entscheidet allein der Vergleich
# mit dem Relay. Im Zweifel wird deshalb lieber zu viel ausgewaehlt als zu wenig
# — ein unnoetig angesehener Beitrag kostet eine Relay-Abfrage, ein
# uebersehener bleibt unveroeffentlicht.
#
# Erwartete Umgebung: ALLE, VORHER, JETZT (setzt der Workflow)
# Ausgabe: posts.txt sowie `modus` in GITHUB_OUTPUT (alle | auswahl | nichts)

set -euo pipefail

INHALT=Website/content
AUSWAHL=posts.txt
LEERER_COMMIT=0000000000000000000000000000000000000000

: > "$AUSWAHL"

notiere() { echo "$1" >> "${GITHUB_STEP_SUMMARY:-/dev/stdout}"; }
setze_modus() { echo "modus=$1" >> "${GITHUB_OUTPUT:-/dev/stdout}"; }

alle_ansehen() {
  echo "Modus: alle Beitraege."
  setze_modus alle
  exit 0
}

if [ "${ALLE:-false}" = "true" ]; then
  echo "Manuell angefordert."
  alle_ansehen
fi

# Fehlt der Vorgaengercommit, ist der Diff nicht bildbar. Das passiert bei einem
# neuen Branch, nach einem Force-Push und bei einem erneuten Lauf eines alten
# Commits. Frueher war das der stille Fall: Die Aktion meldete Erfolg, ohne
# etwas anzusehen. Jetzt fuehrt es zum vollen Lauf.
if [ -z "${VORHER:-}" ] || [ "${VORHER}" = "$LEERER_COMMIT" ] \
   || ! git cat-file -e "${VORHER}^{commit}" 2>/dev/null; then
  echo "Vorgaengercommit '${VORHER:-<leer>}' nicht auswertbar."
  notiere '> [!NOTE]'
  notiere '> Der Vorgaengercommit war nicht auswertbar (neuer Branch, Force-Push oder'
  notiere '> erneuter Lauf). Es wurden deshalb **alle** Beitraege angesehen.'
  alle_ansehen
fi

# Zu jeder geaenderten Datei den Beitrag finden, zu dem sie gehoert: nach oben
# gehen, bis eine index.md daneben liegt. Damit loest auch ein geaendertes Bild
# den Beitrag aus — Blob und Lizenznachweis haengen daran.
while IFS= read -r datei; do
  [ -n "$datei" ] || continue
  verzeichnis=$(dirname "$datei")
  while [ "$verzeichnis" = "$INHALT" ] || [ "${verzeichnis#"$INHALT"/}" != "$verzeichnis" ]; do
    if [ -f "$verzeichnis/index.md" ]; then
      printf '%s\n' "$verzeichnis/index.md" >> "$AUSWAHL"
      break
    fi
    verzeichnis=$(dirname "$verzeichnis")
  done
done < <(git diff --name-only "$VORHER" "$JETZT" -- "$INHALT")

sort -u "$AUSWAHL" -o "$AUSWAHL"
anzahl=$(wc -l < "$AUSWAHL")

if [ "$anzahl" -eq 0 ]; then
  echo "Keine Aenderung gehoert zu einer index.md."
  notiere '> [!NOTE]'
  notiere "> Unter \`$INHALT\` hat sich etwas geaendert, aber zu keiner dieser Aenderungen"
  notiere '> gehoert eine `index.md` — etwa nur eine Sektionsseite (`_index.md`) oder eine'
  notiere '> geloeschte Datei. Es wurde **nichts publiziert und nichts uebersehen**.'
  setze_modus nichts
  exit 0
fi

echo "Geaenderte Beitraege: $anzahl"
cat "$AUSWAHL"
setze_modus auswahl
