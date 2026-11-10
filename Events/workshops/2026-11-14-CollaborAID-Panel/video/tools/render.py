# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright>=1.48"]
# ///
"""Rendert das Video bildgenau: Für jedes Bild ruft ein unsichtbarer Chrome
renderFrame(t) auf, liest die Leinwand aus und reicht sie an ffmpeg weiter.
Der Ton kommt aus build/stimme.wav.

Aufruf:
  uv run tools/render.py                      # komplettes Video, 1920×1080, 30 fps
  uv run tools/render.py --entwurf            # schneller Entwurf, 960×540, 15 fps
  uv run tools/render.py --von 60 --bis 90    # nur ein Ausschnitt
  uv run tools/render.py --untertitel         # mit eingebrannten Untertiteln

Ausgabe: build/video.mp4 (bzw. build/entwurf.mp4)
Braucht Google Chrome (wird über Playwright gesteuert, kein Extra-Download).
"""
import argparse
import base64
import functools
import http.server
import json
import subprocess
import sys
import threading
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

HIER = Path(__file__).resolve().parent.parent
BUILD = HIER / "build"
STAPEL = 15  # Bilder pro Aufruf in den Browser


def server_starten() -> int:
    class Leise(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

    handler = functools.partial(Leise, directory=str(HIER))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv.server_address[1]


def kontaktbogen(args):
    """Ein Standbild je Einheit, zusammengesetzt zu build/kontaktbogen.jpg (6 Spalten)."""
    import shutil
    timeline = json.loads((BUILD / "timeline.json").read_text(encoding="utf-8"))
    ordner = BUILD / "kontakt"
    shutil.rmtree(ordner, ignore_errors=True)
    ordner.mkdir(parents=True)
    port = server_starten()
    query = "render=1" + ("&untertitel=1" if args.untertitel else "") + ("&regie=1" if args.regie else "")
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", headless=True)
        seite = browser.new_page(viewport={"width": 1920, "height": 1080})
        seite.on("console", lambda m: m.type in ("error", "warning") and print("  Browser:", m.text, file=sys.stderr))
        seite.on("pageerror", lambda e: print("  Seitenfehler:", e, file=sys.stderr))
        seite.goto(f"http://127.0.0.1:{port}/player/?{query}")
        seite.evaluate("window.bereit")
        for k, e in enumerate(timeline["einheiten"], 1):
            t = e["start"] + args.kontakt * (e["sprechende"] - e["start"])
            b = seite.evaluate("""([t, id]) => { renderFrame(t);
                const c = document.getElementById('leinwand'), k = document.createElement('canvas');
                k.width = 640; k.height = 360; const x = k.getContext('2d');
                x.drawImage(c, 0, 0, 640, 360);
                x.fillStyle = 'rgba(0,0,0,.6)'; x.fillRect(0, 0, 52, 24);
                x.fillStyle = '#fff'; x.font = '16px monospace'; x.fillText(id, 8, 17);
                return k.toDataURL('image/jpeg', .9).slice(23); }""", [t, e["id"]])
            (ordner / f"{k:02d}.jpg").write_bytes(base64.b64decode(b))
        browser.close()
    ziel = BUILD / "kontaktbogen.jpg"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", "1", "-i", str(ordner / "%02d.jpg"),
                    "-vf", "tile=6x7:padding=6:color=0x2b2925", "-frames:v", "1", "-q:v", "3", str(ziel)], check=True)
    print(f"{ziel.relative_to(HIER)}: {len(timeline['einheiten'])} Standbilder")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fps", type=int)
    ap.add_argument("--von", type=float, default=0.0)
    ap.add_argument("--bis", type=float)
    ap.add_argument("--entwurf", action="store_true")
    ap.add_argument("--untertitel", action="store_true")
    ap.add_argument("--regie", action="store_true", help="Regiehinweise im Bild lassen")
    ap.add_argument("--ziel", type=Path)
    ap.add_argument("--kontakt", nargs="?", const=0.85, type=float, metavar="ANTEIL",
                    help="Kontaktbogen: ein Standbild je Einheit bei ANTEIL ihrer Sprechzeit (Standard 0,85)")
    args = ap.parse_args()

    if args.kontakt:
        return kontaktbogen(args)

    fps = args.fps or (15 if args.entwurf else 30)
    ziel = args.ziel or BUILD / ("entwurf.mp4" if args.entwurf else "video.mp4")
    timeline = json.loads((BUILD / "timeline.json").read_text(encoding="utf-8"))
    bis = min(args.bis or timeline["dauer"], timeline["dauer"])
    von = max(0.0, args.von)
    n = int(round((bis - von) * fps))

    port = server_starten()
    query = "render=1" + ("&untertitel=1" if args.untertitel else "") + ("&regie=1" if args.regie else "")
    url = f"http://127.0.0.1:{port}/player/?{query}"

    vf = "scale=960:540:flags=lanczos," if args.entwurf else ""
    ffmpeg = subprocess.Popen([
        "ffmpeg", "-loglevel", "error", "-y",
        "-f", "image2pipe", "-c:v", "mjpeg", "-framerate", str(fps), "-i", "-",
        "-ss", f"{von:.3f}", "-t", f"{bis - von:.3f}", "-i", str(BUILD / timeline["audio"]),
        "-map", "0:v", "-map", "1:a",
        "-vf", f"{vf}format=yuv420p",
        "-c:v", "libx264", "-preset", "veryfast" if args.entwurf else "medium",
        "-crf", "23" if args.entwurf else "18", "-r", str(fps),
        "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(ziel),
    ], stdin=subprocess.PIPE)

    qualitaet = 0.85 if args.entwurf else 0.95
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", headless=True)
        seite = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        seite.on("console", lambda m: m.type in ("error", "warning") and print("  Browser:", m.text, file=sys.stderr))
        seite.goto(url)
        seite.evaluate("window.bereit")
        start = time.time()
        for i in range(0, n, STAPEL):
            zeiten = [von + k / fps for k in range(i, min(n, i + STAPEL))]
            bilder = seite.evaluate(
                """([zeiten, q]) => zeiten.map((t) => {
                     renderFrame(t);
                     return document.getElementById('leinwand').toDataURL('image/jpeg', q).slice(23);
                   })""", [zeiten, qualitaet])
            for b in bilder:
                ffmpeg.stdin.write(base64.b64decode(b))
            fertig = min(n, i + STAPEL)
            rest = (time.time() - start) / fertig * (n - fertig)
            print(f"\r  Bild {fertig}/{n}  ({zeiten[-1]:6.1f} s)  noch ~{rest / 60:.1f} min", end="", file=sys.stderr)
        browser.close()
    print(file=sys.stderr)
    ffmpeg.stdin.close()
    if ffmpeg.wait() != 0:
        sys.exit("ffmpeg ist fehlgeschlagen.")
    print(f"{ziel.relative_to(HIER)}: {n} Bilder, {bis - von:.1f} s, {fps} fps, "
          f"{(time.time() - start) / 60:.1f} min Renderzeit")


if __name__ == "__main__":
    main()
