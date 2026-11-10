# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright>=1.48"]
# ///
"""Vorschaubild (1920×1080) für Videoplattformen: Titel über der Übersicht aller
Netzformen aus E39. Ausgabe: ../veroeffentlichung/vorschaubild.jpg

Aufruf: uv run tools/vorschaubild.py ["Titel"] ["Untertitel"]
"""
import base64
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import BUILD, HIER, server_starten  # noqa: E402

TITEL = sys.argv[1] if len(sys.argv) > 1 else "Vom Sender zum Netz"
UNTER = sys.argv[2] if len(sys.argv) > 2 else "Zusammenarbeit ohne Weisung in der religiösen Bildung"


def main():
    tl = json.loads((BUILD / "timeline.json").read_text(encoding="utf-8"))
    e = next(x for x in tl["einheiten"] if x["id"] == "E39")
    port = server_starten()
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", headless=True)
        seite = browser.new_page(viewport={"width": 1920, "height": 1080})
        seite.goto(f"http://127.0.0.1:{port}/player/?render=1")
        seite.evaluate("window.bereit")
        daten = seite.evaluate("""([t, titel, unter]) => {
            renderFrame(t);
            const quelle = document.getElementById('leinwand');
            const c = document.createElement('canvas'); c.width = 1920; c.height = 1080;
            const x = c.getContext('2d');
            x.drawImage(quelle, 0, 0);                       // Papier und Rand
            x.fillStyle = 'rgba(244,239,228,1)'; x.fillRect(0, 0, 1920, 1080);
            x.drawImage(quelle, 0, 0);
            x.fillStyle = '#f4efe4'; x.fillRect(0, 0, 1920, 1080);
            x.drawImage(quelle, 60, 180, 1800, 900, 160, 300, 1600, 800);  // Übersicht verkleinert
            x.fillStyle = '#1f1d1a'; x.textAlign = 'center';
            x.font = '400 104px Georgia, serif'; x.fillText(titel, 960, 165);
            x.fillStyle = '#203A8F'; x.font = 'italic 400 44px Georgia, serif'; x.fillText(unter, 960, 240);
            x.fillStyle = '#FFA500'; x.fillRect(900, 270, 120, 6);
            return c.toDataURL('image/jpeg', 0.92).slice(23);
        }""", [e["start"] + 0.95 * (e["sprechende"] - e["start"]), TITEL, UNTER])
        browser.close()
    ziel = HIER.parent / "veroeffentlichung" / "vorschaubild.jpg"
    ziel.parent.mkdir(exist_ok=True)
    ziel.write_bytes(base64.b64decode(daten))
    print(ziel.relative_to(HIER.parent))


if __name__ == "__main__":
    main()
