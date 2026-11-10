# Aufträge an den KI-Agenten

So wurde der Agent (Claude Code) in den einzelnen Schritten beauftragt, verallgemeinert zum
Wiederverwenden. Platzhalter stehen in `<spitzen Klammern>`. Lizenz: CC BY 4.0, FOERBICO.

Drei Regeln haben sich durch alle Schritte bewährt:

1. **Anhalten nach jedem Zwischenergebnis.** Erst Text, dann Werkzeuge, dann Szenen. Ein Text,
   der sich noch ändert, macht sonst die Animationen wertlos.
2. **Nichts erfinden.** Fakten nur aus genannten Quellen, Lücken als `[PRÜFEN: …]` markieren.
3. **Prüfen, bevor etwas fertig heißt.** Standbilder ansehen, die Tonspur gegenprüfen lassen,
   und sagen, was nicht geprüft werden konnte.

## 1. Sprechtext

```text
ZIEL
Sprechtext für ein vorproduziertes Erklärvideo von <Länge> Minuten zu <Thema>, gesprochen von
mir. Anlass: <Veranstaltung>. Leitfrage: <Frage, auf die das Video antwortet>.
Publikum: <wer, was sie schon wissen>.

QUELLEN (nur diese; Fehlendes als [PRÜFEN: …] markieren, nichts erfinden)
- <Dateien, Webseiten>

FORMAT
- Sinneinheiten von ein bis drei Sätzen, Überschrift "### E01 · stichwort"
- je Einheit eine Zeile "> bild: …" mit Bildregie (was man sieht, was sich bewegt)
- Szenen mit "## Szene n · Titel"; jede Szene endet mit einem Lernsatz zur Leitfrage
  (Einheit "· lernsatz", Bildregie mit Lernsatz: „…“)
- durchgehende Bildmetapher: <z. B. die Form eines Netzes, die sich verändert>
- Ich-Form, gesprochene Sprache, kurze Sätze, keine Fachwörter ohne Not
- <Regeln, etwa: keine Namen von Partnern ohne Freigabe>

Am Ende: Tabelle der offenen Prüfpunkte, Quellenliste, Wortzahl und geschätzte Länge.
Danach anhalten.
```

Folgeaufträge in den Runden danach waren kurz, zum Beispiel: „Ergänze diese Fakten …“,
„Das Wort X kommt zu oft vor, reduziere auf zweimal“, „Kürze auf 8 bis 9 Minuten“,
„Dieser Satz klingt, als würde etwas übergangen, formuliere ihn um“.

## 2. Werkzeugkette

```text
Ich will den Text in einem Stück einsprechen, ohne einzelne Dateien je Absatz.
Baue eine Werkzeugkette in <Ordner>:
1. sprechtext.md zerlegen in Einheiten (JSON) und eine Lesevorlage (HTML, große Schrift)
2. Aufnahme mit Whisper erkennen (Wortzeitstempel), jede Einheit darin finden,
   bei Wiederholungen die vollständige letzte Fassung nehmen, Versprecher und lange Pausen
   herausschneiden, Pausen vereinheitlichen, Lautheit normalisieren
   → Tonspur + Zeitleiste mit Zeit je Einheit und je Wort
3. Vorschau im Browser in einfachem JavaScript, jedes Bild als reine Funktion der Zeit t
4. bildgenaues Rendern zu MP4 mit Ton (Chrome headless + ffmpeg)
Teste alles mit einer künstlichen Aufnahme, in die du einen Versprecher einbaust.
```

## 3. Szenen

```text
Baue für jede Sinneinheit eine Szene nach ihrer Bildregie.
Stil: <z. B. Tusche auf Papier, eine Serifenschrift, eine Akzentfarbe>.
Bewegungen hängen an gesprochenen Wörtern aus der Zeitleiste, nicht an festen Sekunden.
Wiederkehrende Motive als Bausteine, damit Szenen aufeinander aufbauen.
Text im Bild verdichtet den Satz, statt ihn zu wiederholen; höchstens wenige Wörter.
Prüfe mit einem Kontaktbogen (ein Standbild je Einheit) und rendere einen Entwurf.
```

## 4. Aufnahme einsetzen

```text
Die Aufnahme liegt in <Ordner>. Füge die Dateien zusammen, richte sie aus und schneide.
Prüfe danach die fertige Tonspur gegen den Text: fehlen Anfänge oder Enden, gibt es
doppelte Stellen? Melde, was du nicht prüfen konntest.
```

## 5. Rückmeldungen verarbeiten

```text
Hier ist eine Rückmelderunde zum Video. Leite daraus mögliche Änderungen ab und stimme sie
mit mir ab, bevor du etwas umsetzt. Trenne: nur Bild (ohne Nachaufnahme) und Text
(mit Nachaufnahme). Übernimm nichts Wörtliches aus der Rückmeldung ins Repo.
```

Danach: geänderte Absätze in eine Datei nachsprechen und mit `--nach` einsetzen lassen.

## 6. Veröffentlichen

```text
Erzeuge aus der Zeitleiste Untertitel (WebVTT) und Kapitelmarken, ein Vorschaubild und
Titel, Beschreibung und Schlagworte für <Plattform>. Dokumentiere das Making-of im Ordner
so, dass andere es unter <Lizenz> nachmachen können.
```
