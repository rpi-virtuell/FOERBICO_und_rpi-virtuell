# Video-Pipeline für den CollaborAID-Impuls

Vom Sprechtext zum fertigen MP4. Jede Animation ist eine reine Funktion der Zeit; Vorschau
im Browser und Export sind dadurch Bild für Bild identisch.

```
sprechtext.md ──parse──▶ build/beats.json + build/lesetext.html
                                  │
aufnahme/*.wav ──align (Whisper)──┴─▶ build/stimme.wav + build/timeline.json
                                                   │
player/ (Canvas, renderFrame(t)) ◀─────────────────┘
        │
        └──render (Chrome + ffmpeg)──▶ build/video.mp4
```

## Voraussetzungen

`python3`, `uv`, `ffmpeg`, Google Chrome. Python-Pakete (faster-whisper, playwright) holt `uv`
beim ersten Aufruf selbst; das Whisper-Modell „small“ lädt beim ersten Ausrichten (~500 MB).

## Ablauf

Alle Befehle im Ordner `video/`.

1. **Text zerlegen** (nach jeder Änderung an `sprechtext.md`):

   ```bash
   python3 tools/parse.py
   ```

   Erzeugt `build/lesetext.html` als Lesevorlage für die Aufnahme.

2. **Aufnehmen.** Den ganzen Text in einem Stück sprechen, nach jedem Absatz kurz Luft holen.
   Bei einem Versprecher den ganzen Absatz noch einmal sprechen: Das Skript nimmt die
   vollständigste, bei Gleichstand die letzte Fassung. Datei nach `aufnahme/` legen
   (WAV, M4A oder MP3).

3. **Ausrichten und schneiden:**

   ```bash
   uv run tools/align.py aufnahme/joerg.wav
   ```

   Ergebnis: `build/stimme.wav` (Versprecher und lange Pausen entfernt, Pausen vereinheitlicht,
   auf −16 LUFS normalisiert) und `build/timeline.json` (Start und Ende jeder Einheit und jedes
   Wortes). Warnungen nennen Einheiten, die schlecht erkannt wurden; die bitte anhören.
   Mit `--modell medium` wird die Erkennung genauer, aber langsamer. Das Transkript wird
   zwischengespeichert; `--neu` erzwingt eine neue Erkennung.

   **Nachaufnahme einzelner Einheiten:** Geänderte Absätze neu einsprechen (Vorlage:
   `python3 tools/parse.py --nur E19,E21,E22` → `build/nachaufnahme.html`) und dazugeben:

   ```bash
   uv run tools/align.py aufnahme/joerg.wav --nach aufnahme/nachaufnahme.wav --modell medium
   ```

   Jede Einheit, die in der Nachaufnahme vollständig vorkommt, ersetzt die Fassung aus der
   Hauptaufnahme; der Pegel wird angeglichen. `uv run tools/pruefen.py` erkennt die fertige
   Tonspur noch einmal und meldet abgeschnittene oder doppelte Stellen.

4. **Vorschau:** `python3 -m http.server 8771` und <http://localhost:8771/player/> öffnen
   (oder in Claude Code die Vorschau „collaboraid-video“). Leertaste spielt ab, Pfeiltasten
   springen 5 s, Klick in die Liste springt zur Einheit. „Regie“ blendet die Bildregie als
   Platzhalter ein, „Untertitel“ den gesprochenen Satz.

5. **Rendern:**

   ```bash
   uv run tools/render.py --entwurf     # 960×540, 15 fps, ~1,5 min
   uv run tools/render.py               # 1920×1080, 30 fps, ~4 min
   uv run tools/render.py --von 120 --bis 150   # nur ein Ausschnitt
   ```

   Optionen: `--untertitel` brennt Untertitel ein, `--regie` lässt die Regiehinweise stehen.

Zum Ausprobieren ohne eigene Aufnahme erzeugt `python3 tools/testaufnahme.py` eine Fassung
mit der macOS-Stimme „Anna“ (mit einem eingebauten Versprecher in E07).

## Szenen schreiben

Szenen stehen in `player/szenen.js`, eine Funktion je Sinneinheit (`E01`, `E02`, …).
Einheiten ohne eigene Funktion zeigen die Standardszene: Regietext als Platzhalter,
Lernsätze groß hingeschrieben.

```js
function E01(g, z) {
  g.kreis(g.W / 2, g.H / 2, 10, z.ab(0.4, 1.2));          // ab 0,4 s in 1,2 s zeichnen
  g.punkt(g.W / 2, g.H / 2, 10 * z.abWort('weisungsbefugt', 0.5)); // wächst beim Wort
}
```

- `z.lt` Sekunden seit Beginn der Einheit, `z.p` Fortschritt 0..1 über die Einheit
- `z.ab(sek, dauer)` Fortschritt 0..1 ab einer lokalen Zeit
- `z.wort('Wort')` lokale Sprechzeit eines Wortes, `z.abWort('Wort', dauer, versatz)` Fortschritt ab dem Wort
- Zeichnen in `player/zeichnen.js`: `linie`, `pfad`, `kreis`, `punkt`, `text`, `schreiben`
  (Text schreibt sich hin), `absatz`; Hilfen `sanft`, `aus`, `mix`, `zufall(startwert)`
- Keine Zustände zwischen Bildern, kein `Math.random()`: sonst weichen Vorschau und Export voneinander ab.
