# Bildmigration: Beiträge ohne `# bilder`-Block

Stand 2026-09-10. 70 Beiträge mit zusammen 198 verwendeten Bildern warten auf ihren Block.
Migriert sind bereits: die-kraft-der-gemeinschaft, oercamp-2026, tagung-open-education, und seit dem 10.09. (Ginas Branch `add-bildlizenzen` plus drei von main): OER-Fachtag-Orca.NRW, OER-erklaert, OERcamp-Hamburg, OER-Brownbag, Raus-aus-den-Bubbles, Git-Treffen-Medienhaus, Austausch-digiLL, Bibel_OER, OER-Werkstatt, Workshop-KlimaOER, Canva, Rechtsfragen-Workshop, IT-Sommercamp-2025 — 24 Bilder auf Blossom mit Nachweis.
Offen beim OER-Fachtag: das Cover ist eine cdn.midjourney.com-URL ohne Datei im Ordner (Download aus dem Midjourney-Konto nötig, dann `ai: generated`).

## So geht ein Beitrag

1. Block unten in das Frontmatter von `index.md` übernehmen, direkt vor die schließende `---`.
   Der Vorschlag folgt der Footer-Regel von oer.community (CC BY FOERBICO). **Prüfen**, ob das für jedes Bild stimmt:
   fremde Fotos, Logos, Screenshots fremder Seiten, Zeichnungen anderer brauchen Urheber:in, Quelle und deren Lizenz.
   Was nicht frei lizenziert werden darf, bekommt keinen CC-Eintrag und bleibt ohne Nachweis.
2. `alt` als Bildbeschreibung ausfüllen (was ist zu sehen), `title` kurz benennen.
   Vorhandene Alt-Texte aus dem Fließtext sind vorausgefüllt; Dateinamen-Labels nicht.
3. `cd Website/scripts && node md2blossom.mjs ../content/de/posts/<ordner> --write`
   schreibt Hash-URLs, Captions und Cover um. Kein Key nötig.
4. Commit auf einem Branch, Pull Request. Nach dem Merge lädt die CI die Blobs nach Blossom,
   publiziert die Lizenznachweise (kind:1063) und den Beitrag (kind:30023).

Die CI hat den Bilderschritt seit dem 09.09. (mdparser `core/bilder.ts`); `deno task upload`/`publish` braucht es nur noch für Sonderfälle.
Schritt 3 ist der einzige Handschritt, den die CI nicht übernimmt: Ohne md2blossom bleiben die Bilder relative Dateinamen, und die CI findet keine Hash-URL, zu der sie Blob und Nachweis anlegen könnte. Alternativ öffnet der foerbico-editor den Beitrag und macht denselben Schritt im Browser.
Für Handarbeit im Block: Abschnitt „Stolpersteine“ in `wissensgrundlagen/bildattribution.md` (Doppelpunkt + Leerzeichen → Wert in Anführungszeichen).

## Beiträge

### oer-und-oep

1 Bild(er) im Beitrag

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Button_zum-OER-Selbstlernmodul.png:
    alt: 'Zum OER-Selbstlernmodul'
    title: # TODO
    sourceUrl: https://oer.community/oer-und-oep
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-08-05-hello-world

4 Bild(er) im Beitrag, Cover: `FOERBICO-Team.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  FOERBICO-Team.jpg:
    alt: 'Das FOERBICO Team'
    title: # TODO
    sourceUrl: https://oer.community/hello-world
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Friedrich-Alexander-Universitaet_Erlangen-Nuernberg_Logo.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
  Goethe-Universitaet_Frankfurt_Logo.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
  comenius-institut-logo.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
```

### 2024-08-09-sdg-logos

3 Bild(er) im Beitrag, Cover: `cc-by-sa-linzenz-der-sdg-logos.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  SDG-inklusion-OER-Video_Vorschau.png:
    alt: 'Die SDG Logos in OER'
    title: # TODO
    sourceUrl: https://oer.community/sdg-logos-und-oer-wie-darf-ich-sie-verwenden
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  cc-by-sa-linzenz-der-sdg-logos.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
  uno-urheberrecht-grundprinzipien.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/sdg-logos-und-oer-wie-darf-ich-sie-verwenden
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-08-15-OER-im-Blick

3 Bild(er) im Beitrag, Cover: `OER-im-Blick.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  OER-im-Blick-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/rueckblick-auftaktkonferenz-oer-im-blick
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER-im-Blick-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/rueckblick-auftaktkonferenz-oer-im-blick
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER-im-Blick.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/rueckblick-auftaktkonferenz-oer-im-blick
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-09-02-blog_its_jointly_2024

3 Bild(er) im Beitrag, Cover: `phillip-und-ludger.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  brainstorming.jpg:
    alt: 'Viele gute Ideen wurden gesammelt'
    title: # TODO
    sourceUrl: https://oer.community/einblicke-zum-oer-it-sommercamp-its-jointly-2024
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  empoert.jpg:
    alt: 'jOERn sucht nach neuen Netzwerken'
    title: # TODO
    sourceUrl: https://oer.community/einblicke-zum-oer-it-sommercamp-its-jointly-2024
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  phillip-und-ludger.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/einblicke-zum-oer-it-sommercamp-its-jointly-2024
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-09-15-pirner-oer-youtube

1 Bild(er) im Beitrag, Cover: `Prompt-the-Youtube-Logo-but-not-wit-You-and-Tube-instead-with-Creative-and-Commons.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Prompt-the-Youtube-Logo-but-not-wit-You-and-Tube-instead-with-Creative-and-Commons.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
```

### 2024-09-17-GwR-Tagung

2 Bild(er) im Beitrag, Cover: `IMG_3850-scaled.jpg`, unbenutzt im Ordner: `foerbico-flyer.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  FOERBICO-Workshop-GwR-Tagung-2024.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/sichtbarkeit-und-netzwerk-durch-oer-staerken-foerbico-auf-der-gwr-tagung-in-wuerzburg-zum-thema-oeffentlichkeitsarbeit
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Vorteile-von-OER-flipchart.jpg:
    alt: 'Aussagen zu OER-Vorteilen auf einem Flipchart'
    title: # TODO
    sourceUrl: https://oer.community/sichtbarkeit-und-netzwerk-durch-oer-staerken-foerbico-auf-der-gwr-tagung-in-wuerzburg-zum-thema-oeffentlichkeitsarbeit
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-09-18-TikTok

1 Bild(er) im Beitrag, Cover: `kemnitzer-tiktok.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  kemnitzer-tiktok.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/theologie-auf-tiktok-religioese-kommunikation-im-digitalen-raum
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-10-02-AKRK

5 Bild(er) im Beitrag, Cover: `AKRK-Tagung_OER-standards.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  AKRK-Tagung_OER-OEP-workshop.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/welche-impulse-setzt-oer-fuer-die-religionsdidaktik-ein-einblick-in-die-akrk-tagung-in-leitershofen-von-19-21-9-2024
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  AKRK-Tagung_OER-standards.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/welche-impulse-setzt-oer-fuer-die-religionsdidaktik-ein-einblick-in-die-akrk-tagung-in-leitershofen-von-19-21-9-2024
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  AKRK-Tagung_OER-und-ihre-didaktik.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/welche-impulse-setzt-oer-fuer-die-religionsdidaktik-ein-einblick-in-die-akrk-tagung-in-leitershofen-von-19-21-9-2024
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  AKRK-Tagung_Vortrag.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/welche-impulse-setzt-oer-fuer-die-religionsdidaktik-ein-einblick-in-die-akrk-tagung-in-leitershofen-von-19-21-9-2024
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  AKRK-Tagung_laura-und-viera.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/welche-impulse-setzt-oer-fuer-die-religionsdidaktik-ein-einblick-in-die-akrk-tagung-in-leitershofen-von-19-21-9-2024
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-10-07-DisKursLab

1 Bild(er) im Beitrag, Cover: `videokonferenz_diskurslab-rpi-foerbico.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  videokonferenz_diskurslab-rpi-foerbico.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-zum-thema-antisemitismus-gemeinsam-bildungsmaterialien-gestalten
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-10-14-OERinfo-Fachtag

5 Bild(er) im Beitrag, Cover: `OERinfo-Fachtag-FOERBICO-Team.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Community-Staerkung-Erweiterung.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oerinfo-fachtag-am-7-10-2024-in-frankfurt-how-to-build-a-community
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  DIPF-Gebaeude.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oerinfo-fachtag-am-7-10-2024-in-frankfurt-how-to-build-a-community
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Kurzvorstellung-FOERBICO-vorschau.png:
    alt: 'FOERBICO kurz vorgestellt von Jörg'
    title: # TODO
    sourceUrl: https://oer.community/oerinfo-fachtag-am-7-10-2024-in-frankfurt-how-to-build-a-community
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OERinfo-Fachtag-Begruessung.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oerinfo-fachtag-am-7-10-2024-in-frankfurt-how-to-build-a-community
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OERinfo-Fachtag-FOERBICO-Team.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oerinfo-fachtag-am-7-10-2024-in-frankfurt-how-to-build-a-community
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-11-29-libori-social

2 Bild(er) im Beitrag, Cover: `liboriSocial_postcard.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  liboriSocial_postcard.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/libori-social
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  startodon-reliverse.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/libori-social
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-11-30-OERcamp-Essen

19 Bild(er) im Beitrag, Cover: `20241118-OERcamp-OER-Festival-Essen-%E2%80%93-Website-Kachel-komprimiert-1.png?fit=768%2C432&ssl=1`, unbenutzt im Ordner: `OERcamp-OER-Festival-2024-Essen.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  ABBA-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  ABBA-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  DesignFuturing.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  FDM-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  KI-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  KI-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER-Assistent-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER-Assistent-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER-Assistent-3.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER-Assistent-4.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Stack.nrw-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Stack.nrw-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Stack.nrw-3.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Stack.nrw-4.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Unperfekthaus-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Unperfekthaus-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  digiLL.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  edufeed.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  workshop-organisationsentwicklung.jpg:
    alt: 'Video auf YouTube'
    title: # TODO
    sourceUrl: https://oer.community/oercamp-und-oer-festival-2024-in-essen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-12-03-Konzeptionstag

5 Bild(er) im Beitrag, Cover: `Teamtreffen.jpg`, unbenutzt im Ordner: `Ergebnisse-1.jpg`, `Ergebnisse-2.jpg`, `Ergebnisse-3.jpg`, `Ergebnisse-4.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Kleingruppe-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/konzeptionstag
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Kleingruppe-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/konzeptionstag
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Lego.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/konzeptionstag
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Teamtreffen.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/konzeptionstag
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  mindmap-bedarfe.jpg:
    alt: 'Minmap "Bedarfe"'
    title: # TODO
    sourceUrl: https://oer.community/konzeptionstag
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2024-12-10-Antisemitismus-Treffen

1 Bild(er) im Beitrag, Cover: `Community-Treffen.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Community-Treffen.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/gemeinsam-gegen-antisemitismus
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-01-12-OER-Remix

1 Bild(er) im Beitrag, Cover: `Open_Educational_Resources.png`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  CC_License_Compatibility_Chart.jpg:
    alt: 'Vereinbarkeit von CC Lizenzen'
    title: # TODO
    sourceUrl: https://oer.community/oer-remix
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-02-25-KLT-Münster

2 Bild(er) im Beitrag, Cover: `Gruppenarbeit_Tagung.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Gruppenarbeit_Tagung.jpg:
    alt: 'Gruppenarbeits Ergebnisse'
    title: # TODO
    sourceUrl: https://oer.community/oer-meets-fachdidaktik
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Markdown_Tagung.jpg:
    alt: 'Notizen mit Markdown'
    title: # TODO
    sourceUrl: https://oer.community/oer-meets-fachdidaktik
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-03-04-dezentrale-oep-oer

1 Bild(er) im Beitrag, Cover: `dezentrale-oep-oer.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  dezentrale-oep-oer.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/dezentrale-oep-oer
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-03-11-OER-Fortbildung-Teil1

1 Bild(er) im Beitrag, Cover: `OER-Fortbildungsreihe-1.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  OER-Fortbildungsreihe-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-fortbildungsreihe-1
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-03-20-dezentrale-oer-infrastrukturen

1 Bild(er) im Beitrag, Cover: `gina-matthias-joerg.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  gina-matthias-joerg.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/dezentrale-oer-infrastrukturen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-03-21-fachzeitschriften

1 Bild(er) im Beitrag, Cover: `fachzeitschriften.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  fachzeitschriften.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-zeitschriften-religionspaedagogik
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-03-25-Third-Mission

1 Bild(er) im Beitrag, Cover: `clemens-van-lay-ppJjSjpaw58-unsplash.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  clemens-van-lay-ppJjSjpaw58-unsplash.jpg:
    alt: 'Eine rote Flagge am Strand mit dem Aufdruck "Open"'
    title: # TODO
    sourceUrl: https://oer.community/third-mission
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-03-26-OER-Hochschulreihe-Teil-2

1 Bild(er) im Beitrag, Cover: `OER-Fortbildungsreihe-2.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  OER-Fortbildungsreihe-2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-fortbildungsreihe-2
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-04-10-So-arbeiten-wir

3 Bild(er) im Beitrag, Cover: `foerbildfunktion.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Grafik-1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/so-arbeiten-wir
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Redaktionsprozess.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/so-arbeiten-wir
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  foerbildfunktion.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/so-arbeiten-wir
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-04-11-OER-Hochschulreihe-Teil-3

1 Bild(er) im Beitrag, Cover: `classroom.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  classroom.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-fortbildungsreihe-3
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-04-15-open-net

1 Bild(er) im Beitrag, Cover: `greg-und-joerg-we-are-open.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  greg-und-joerg-we-are-open.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/evangelisches-labor
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-04-20-OER-und-Symbole

1 Bild(er) im Beitrag, Cover: `nadel-im-heuhaufen.jpg`, unbenutzt im Ordner: `nadel-im-heuhaufen-comic.jpg`, `nadel-im-heuhaufen-fotorealistisch.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  nadel-im-heuhaufen.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lizenz-irrtum-oer
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-04-24-Konzeptionstage

1 Bild(er) im Beitrag, Cover: `Weg_zum_Community-Hub.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Weg_zum_Community-Hub.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-konzeptionstage
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-05-04-HackathOERn

6 Bild(er) im Beitrag, Cover: `gina-ludger-joerg.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  gina-ludger-joerg.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/hackathoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  hackathoern-teilnehmer-innen.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/hackathoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  hackerboys.jpg:
    alt: 'Die Hackerboys'
    title: # TODO
    sourceUrl: https://oer.community/hackathoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  hacking-in-nature.jpg:
    alt: 'Hacking in Nature'
    title: # TODO
    sourceUrl: https://oer.community/hackathoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  plattformen-als-inseln.jpg:
    alt: 'Plattformem als Inseln (ein KI generiertes Bild)'
    title: # TODO
    sourceUrl: https://oer.community/hackathoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  praesentation.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/hackathoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-05-16-OER-im-Blick-2025

11 Bild(er) im Beitrag, Cover: `IMG_9713.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  IMG_6385.jpg:
    alt: 'Ergebnisse Pre-Workshop'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  IMG_9713.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  IMG_9725.jpg:
    alt: 'Vortrag Prof. Dr. Otto'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  mermaid-diagram-Tisch2.jpg:
    alt: 'Gruppenergebnisse Tisch 2'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  mermaid-diagram-Tisch3.jpg:
    alt: 'Gruppenergebnisse Tisch 3'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  mermaid-diagram-Tisch4.jpg:
    alt: 'Gruppenergebnisse Tisch 4'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  mermaid-diagramm_Tisch1.jpg:
    alt: 'Gruppenergebnisse Tisch 1'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  tisch1.jpg:
    alt: 'Gruppenarbeit Community-Hub Tisch 1'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  tisch2a.jpg:
    alt: 'Gruppenarbeit Community-Hub Tisch 2'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  tisch3b.jpg:
    alt: 'Gruppenarbeit Community-Hub Tisch 3'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  tisch4.jpg:
    alt: 'Gruppenarbeit Community-Hub Tisch 4'
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-06-02-RPT25

1 Bild(er) im Beitrag, Cover: `rpt25.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  rpt25.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/ki-und-religionspaedagogik
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-06-26-Save_the_Date

2 Bild(er) im Beitrag, Cover: `Save the Date.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  'Save the Date.jpg':
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/save-the-date
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  anmeldebutton.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/save-the-date
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-07-03-ÖRF-Deeper-Learning

2 Bild(er) im Beitrag, Cover: `OERF-2025-gruppenfoto.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  OERF-2025-gruppenfoto.jpg:
    alt: 'Gruppenfoto OERF 2025'
    title: # TODO
    sourceUrl: https://oer.community/going-deep-er-oerf-tagung-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  praesentation-foerbico.jpg:
    alt: 'Präsentation des FOERBICO-Projekts'
    title: # TODO
    sourceUrl: https://oer.community/going-deep-er-oerf-tagung-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-07-07-oer-rel-paed

3 Bild(er) im Beitrag, Cover: `theoweb-OER.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Abbildung-1.jpg:
    alt: 'Überblick Prismma'
    title: # TODO
    sourceUrl: https://oer.community/oer-oep-literaturbericht
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Abbildung-2.jpg:
    alt: 'Adaptiertes Qualitätsmodell'
    title: # TODO
    sourceUrl: https://oer.community/oer-oep-literaturbericht
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  theoweb-OER.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-oep-literaturbericht
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-07-10-TriebfedOERn

5 Bild(er) im Beitrag, Cover: `einhorn-sonja-silvia-joerg.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  deputat-fuer-OER.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/triebfedoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  einhorn-sonja-silvia-joerg.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/triebfedoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  moodle-zoerr.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/triebfedoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  oer-wimmelbild-cc-mixer.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/triebfedoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  sessionplan-triebfedoern-barcamp.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/triebfedoern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-07-19-OER-Beratung

2 Bild(er) im Beitrag, Cover: `check-306411_1280.png`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  MaPS-Logo-17.10-rounded.png:
    alt: 'M@ps Logo'
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
  check-306411_1280.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-beratung-und-qualitätskriterien
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-07-28-Instagram-religionspädagogischer-Lernort

4 Bild(er) im Beitrag, Cover: `ima_22a17d4.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  ima_22a17d4.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/instagram-als-lernort
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  ima_2648be8.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/instagram-als-lernort
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  ima_a6fc6d5.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/instagram-als-lernort
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  ima_eb6a938.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/instagram-als-lernort
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-08-26-Edufeed-Pitch

2 Bild(er) im Beitrag, Cover: `ChatGPT-Plattforminseln.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  ChatGPT-Plattforminseln.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/edufeed-pitch
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  edufeed-pitch-vorschaubild.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/edufeed-pitch
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-09-02-Imaginationen-von-Offenheit-in-der-Bildung

1 Bild(er) im Beitrag, Cover: `geo-tueren-offenheit.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  geo-tueren-offenheit.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/imaginationen-offenheit-bildung
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-09-10-OER-und-visuelle-Qualität

1 Bild(er) im Beitrag, Cover: `pictureframe.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  pictureframe.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-visuelle-qualität
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-09-11-OEP-Von-Ressourcen-zu-Praktiken

2 Bild(er) im Beitrag, Cover: `oer-cube.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  constitutive-elements-of-OEP-Ehlers-2011.jpg:
    alt: 'Figure 2: Matrix 1 . Constitutive Elements of OEP (Ehlers 2011)'
    title: # TODO
    sourceUrl: https://oer.community/oep-von-ressourcen-zu-praktiken
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  oer-cube.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oep-von-ressourcen-zu-praktiken
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-09-24-Theologie-Memes

3 Bild(er) im Beitrag, Cover: `Social-Media-Logo-Uni-Vechta.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Meme-1.jpg:
    alt: 'Psalm 137,9'
    title: # TODO
    sourceUrl: https://oer.community/theologie-memes
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Meme-3.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/theologie-memes
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Social-Media-Logo-Uni-Vechta.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
```

### 2025-10-06-Reformation

3 Bild(er) im Beitrag, Cover: `2.png`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/luther-influencer
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  2.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/luther-influencer
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Toolhinweis.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/luther-influencer
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-10-10 Offenheit braucht Tiefe TiRU Projekt

1 Bild(er) im Beitrag, Cover: `TiRU.png`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  TiRU.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/digitale-offenheit-braucht-tiefe
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-10-10-OER-Qualitätskriterien-Checkliste

1 Bild(er) im Beitrag, Cover: `Quality.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Quality.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/offenheit-ist-kein-gegensatz-zu-qualität
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-10-15-Meeting-Kerres

1 Bild(er) im Beitrag, Cover: `Kerres-Moessle2025.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Kerres-Moessle2025.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/austausch-mit-michael-kerres
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-10-24-OERinfo-Fachtag-2025

3 Bild(er) im Beitrag, Cover: `20251024_150726-min.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  20251024_100342-min.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oerinfo-fachtag-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  20251024_150726-min.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oerinfo-fachtag-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OERinfo-Fachtag-2025-min.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oerinfo-fachtag-2025
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-11-10-Actionbound

4 Bild(er) im Beitrag, Cover: `Titelbild-Martin.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Actionbound-Übersicht.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/wertebildung
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Hinweis-Actionbound.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/wertebildung
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Hinweis-Martin.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/wertebildung
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Titelbild-Martin.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/wertebildung
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-12-08-Lichtmomente

8 Bild(er) im Beitrag, Cover: `Titelbild.jpg`, unbenutzt im Ordner: `Weihnachten global.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  1.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lichtmomente
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  10.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lichtmomente
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  17.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lichtmomente
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  2.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lichtmomente
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  6.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lichtmomente
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  GlobalesLernen.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lichtmomente
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Titelbild.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lichtmomente
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Weihnachtenglobal.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/lichtmomente
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-12-08-Musik-OER

1 Bild(er) im Beitrag, Cover: `Music-House-Susanlenox-CC0.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Music-House-Susanlenox-CC0.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/musik-oer
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-12-10-Wie-gehen-Lehrpersonen-mit-OER-um

1 Bild(er) im Beitrag, Cover: `we-are-open.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  we-are-open.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/open-ist-eine-haltung
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2025-12-12-Interview-relilab

3 Bild(er) im Beitrag, Cover: `RelilabInterviewTitelpage.jpg`, unbenutzt im Ordner: `TitelBlog_Interview.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  FOERBICO_Tagung_Logo.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
  RelilabInterviewTitelpage.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/interview-relilab
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  relilab_logo.png:
    alt: 'Logo relilab'
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
```

### 2025-12-12-InterviewOtto

1 Bild(er) im Beitrag, Cover: `FOERBICO_Tagung_Logo.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  FOERBICO_Tagung_Logo.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
```

### 2026-01-22-Autorisierte-Schulbuecher-oder-offene-OER

1 Bild(er) im Beitrag, Cover: `Buecherregal.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Buecherregal.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/autorisierte-schulbuecher-oder-offene-oer
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-01-28

4 Bild(er) im Beitrag, Cover: `RELImentarInterviewTitelpage.jpg`, unbenutzt im Ordner: `anmeldebutton(2).png`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  FOERBICO_Tagung_Logo.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
  RELImentarInterviewTitelpage.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/interview-relimentar
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Screenshot_RELImentar.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/interview-relimentar
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  logo-relimentar-final-2.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    author: # TODO fremdes Logo – Rechteinhaber:in
    sourceUrl: # TODO
    licenceUrl: # TODO (kein CC, wenn nicht freigegeben)
```

### 2026-02-04-loewe-von-juda

3 Bild(er) im Beitrag, Cover: `loewe_von_juda_titelbild.jpg`, unbenutzt im Ordner: `Gemini_Generated_Image_k0cbmok0cbmok0cb.jpg`, `loewe_von_juda_01.jpg`, `loewe_von_juda_02.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  loewe_von_juda_03.jpg:
    alt: 'Männliche Charaktere'
    title: # TODO
    sourceUrl: https://oer.community/der-loewe-schwierigkeiten
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  loewe_von_juda_04.jpg:
    alt: '»Mit der Löwe von Juda schaffen wir einen neuen Zugang: liebevoll illustriert, verständlich erzählt, einzigartig gestaltet und zugleich bibeltheologisch verantwortet. Die Tierfiguren sind dabei mehr als ein gestalterisches Mittel: Sie sind Brücken zwischen der Welt der Kinder und der Welt der Bibel. Diese Darstellungen sind nicht willkürlich, sondern symbolisch aufgeladen und medienpädagogisch fundiert. Sie ermöglichen Kindern, sich mit den Figuren zu identifizieren, ohne durch kulturelle und soziale Merkmale ausgeschlossen zu werden.«'
    title: # TODO
    sourceUrl: https://oer.community/der-loewe-schwierigkeiten
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  loewe_von_juda_titelbild.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/der-loewe-schwierigkeiten
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-02-18-Interview-reliGlobal

1 Bild(er) im Beitrag, Cover: `Titelbild-reliGlobal.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Titelbild-reliGlobal.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/interview-reliGlobal
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-02-20-Inklusives-Lernen-durch-OEP

1 Bild(er) im Beitrag, Cover: `you-belong.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  you-belong.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/inklusives-Lernen-durch-OEP
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-03-02-FOERBICO-Zwischenfazit-Tagung

15 Bild(er) im Beitrag, Cover: `Team.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Begleitforschung.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  CriticalFriends.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Essen.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Forschungsstand.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Grusswort-Reuter.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Hilfskraefte.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Hub-Vorstellung.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Keynote.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER_KI_Matrix.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Qualitaet.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  RELImentar.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Team.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  hoerz.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  reliGlobal.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  relilab.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/recap-foerbico-tagung-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-03-03-OER-erstellen

2 Bild(er) im Beitrag, Cover: `How_to_get_started_OER_Xue_Paschke.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  How_to_get_started_OER_Xue_Paschke.jpg:
    alt: 'Pfad für OER-Erstellung'
    title: # TODO
    sourceUrl: https://oer.community/oer-erstellen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Tabelle.png:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-erstellen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-04-02-Tagung_Theologie_und_Hochschuldidaktik

1 Bild(er) im Beitrag, Cover: `educationforall.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  educationforall.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/koennen-oep-partizipatives-lernen-und-demokratiebildung-foerdern
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-04-17-hOERz-Herzensaustausch

2 Bild(er) im Beitrag, Cover: `cover.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  cover.jpg:
    alt: 'hOERz – Holzherzen mit NFC-Chips auf der FOERBICO-Tagung'
    title: # TODO
    sourceUrl: https://oer.community/hoerz
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  foerbico-herz.png:
    alt: 'hOERz-Logo: SDG17-Logo mit orangem Herz'
    title: # TODO
    sourceUrl: https://oer.community/hoerz
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-04-24-Kinderuni

5 Bild(er) im Beitrag, Cover: `Titelbild-Copyright-Institut-Katholische-Theologie-Uni-Vechta.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Praesentation-Beispiel-Ausschnitt-1-Copyright-Institut-Katholische-Theologie-Uni-Vechta.jpg:
    alt: 'Beispielbild der Präsentation, Ausschnitt 1'
    title: # TODO
    sourceUrl: https://oer.community/junia
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Praesentation-Beispiel-Ausschnitt-2-Copyright-Institut-Katholische-Theologie-Uni-Vechta.jpg:
    alt: 'Beispielbild der Präsentation, Ausschnitt 2'
    title: # TODO
    sourceUrl: https://oer.community/junia
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Praesentation-Beispiel-Ausschnitt-3-Copyright-Institut-Katholische-Theologie-Uni-Vechta.jpg:
    alt: 'Beispielbild der Präsentation, Ausschnitt 3'
    title: # TODO
    sourceUrl: https://oer.community/junia
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Praesentation-Beispiel-Copyright-Institut-Katholische-Theologie-Uni-Vechta.jpg:
    alt: 'Beispielbild der Präsentation'
    title: # TODO
    sourceUrl: https://oer.community/junia
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Titelbild-Copyright-Institut-Katholische-Theologie-Uni-Vechta.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/junia
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-04-28-Geschoepflichkeit-als-Massstab-KI

1 Bild(er) im Beitrag, Cover: `haende.jpg`, unbenutzt im Ordner: `geschoepf-ki-banana2.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  haende.jpg:
    alt: 'Vier Hände der Arbeitsgruppe - Miriam, Simone, Jörg und Steffen - auf der Terrasse des Instituts'
    title: # TODO
    sourceUrl: https://oer.community/geschoepflichkeit-als-massstab-ki
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-05-04-OER-im-Blick-2026

3 Bild(er) im Beitrag, Cover: `OER-im-Blick-2026-Titelbild.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  OER-im-Blick-2026-Projektvorstellung.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER-im-Blick-2026-Titelbild.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  OER-im-Blick-2026-Workshop.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/oer-im-blick-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-05-18-HackathOERn-2026

4 Bild(er) im Beitrag, Cover: `Gruppenfoto-HackathOERn.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  11.jpg:
    alt: 'Die NavigatOER- und Termi-Crew vor der Ökosystem-Folie – „See you later, NavigatOER"'
    title: # TODO
    sourceUrl: https://oer.community/hackathoern-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  2.jpg:
    alt: 'Das Termi-Team am Whiteboard: Ludger, Steffen, Gina und Jörg vom FOERBICO-Team mit Toby (GWDG) und Maskottchen „Termi"'
    title: # TODO
    sourceUrl: https://oer.community/hackathoern-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  5.jpg:
    alt: 'Das Ökosystem: WordPress/Drupal/HTML5 → Termi → OERSI + Nostr → NavigatOER'
    title: # TODO
    sourceUrl: https://oer.community/hackathoern-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Gruppenfoto-HackathOERn.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/hackathoern-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-06-25-Personal-Learning-Environments

1 Bild(er) im Beitrag, Cover: `Wortwolke.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Wortwolke.jpg:
    alt: 'Wortwolke aus den seminarbegleitenden Evaluationen mit wiederkehrend genannten Stärken der Seminarkonzeption, u.a. Methodenvielfalt, Lernatmosphäre, Praxisnähe und die Verknüpfung von Fachwissenschaft und Fachdidaktik'
    title: # TODO
    sourceUrl: https://oer.community/personal-learning-environments-in-der-hochschulbildung
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-07-21-OER-Plattformen-neu

1 Bild(er) im Beitrag, Cover: `mohammed-zayan-khan-ack4TTlozAw-unsplash.jpg`, unbenutzt im Ordner: `humaaans-characters.png`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  mohammed-zayan-khan-ack4TTlozAw-unsplash.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/offen-und-leicht-zu-finden-oer-plattformen
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### 2026-08-12-Just-calling-it-open-is-not-enough

1 Bild(er) im Beitrag, Cover: `Herausforderung-Bildungsinfrastruktur-KI-generiert.jpg`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  Herausforderung-Bildungsinfrastruktur-KI-generiert.jpg:
    alt: # TODO Bildbeschreibung
    title: # TODO
    sourceUrl: https://oer.community/just-calling-it-open-is-not-enough
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

### unser-team

8 Bild(er) im Beitrag, unbenutzt im Ordner: `PaulaPaschke.png`

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
bilder:
  GinaBuchwaldChassee.jpg:
    alt: 'Portrait Gina Buchwald-Chassée'
    title: # TODO
    sourceUrl: https://oer.community/unser-team
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  JensDechow.jpg:
    alt: 'Portrait Jens Dechow'
    title: # TODO
    sourceUrl: https://oer.community/unser-team
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  JoergLohrer.jpg:
    alt: 'Portrait Jörg Lohrer'
    title: # TODO
    sourceUrl: https://oer.community/unser-team
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  LauraMoessle.jpg:
    alt: 'Portrait Laura Mößle'
    title: # TODO
    sourceUrl: https://oer.community/unser-team
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  LudgerSicking.jpg:
    alt: 'Portrait Ludger Sicking'
    title: # TODO
    sourceUrl: https://oer.community/unser-team
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  ManfredPirner.jpg:
    alt: 'Portrait Manfred Pirner'
    title: # TODO
    sourceUrl: https://oer.community/unser-team
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  PhillipAngelina.jpg:
    alt: 'Portrait Phillip Angelina'
    title: # TODO
    sourceUrl: https://oer.community/unser-team
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  VieraPirker.jpg:
    alt: 'Portrait Viera Pirker'
    title: # TODO
    sourceUrl: https://oer.community/unser-team
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
```

