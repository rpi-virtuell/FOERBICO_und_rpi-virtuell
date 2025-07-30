# wordpress to markdown

Übersicht über getestete Möglichkeiten zu Konvertierung/Export von WordPress-Beiträgen nach MarkDown.

## Alex Seifert - export-wordpress-to-markdown
https://github.com/eiskalteschatten/export-wordpress-to-markdown

### Was?
id, title, status, authors, titleImage, excerpt, categories, tags, publishedDate, updatedAt, wordpressId


### Wie?
Skript, das via REST-API WordPress-Beiträge  und ihre Bilder in Markdown-Dateien importiert.
Es exportiert auch Autoren, Kategorien und Tags in JSON-Dateien.

### Herausforderungen
- Metadaten separat in meta.json


## lonekorean - wordpress-export-to-markdown
https://github.com/lonekorean/wordpress-export-to-markdown

### Wie?
Konvertiert eine WordPress export XML Datei in Markdown Dateien, die kompatibel sind. 

### Was? 
title, date, categories, tags, coverImage

### Herausforderungen
- Autoren fehlen im YAML
- Bilder zwar heruntergeladen aber nicht korrekt verlinkt


## Swizec - wordpress-to-markdown
https://github.com/Swizec/wordpress-to-markdown?tab=readme-ov-file

### Herausforderungen
Arbeitet mit [Yarn - seit 2020 in Maintenance](https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable)

## Robert DeVore - Markdown Exporter for WordPress®
https://robertdevore.com/introducing-markdown-exporter-for-wordpress/
https://github.com/getstattic/stattic/
### Wie
Plugin in WordPress
### Herausforderungen
- HTML im Content bleibt in Paragraphs
- YAML-Metadaten inkl vielen Fragmenten aus anderen WordPress-Plugins
- ausschließlich MarkDown - Kein Medienexport

## DAEXT - Ultimate Markdown – Markdown Editor, Importer, & Exporter
### Wie?
Plugin
### Herausforderungen
- Markdown-Export nur mit Premium-Version

## gohugo - wordpress-to-hugo-exporter
https://github.com/SchumacherFM/wordpress-to-hugo-exporter
### Was?
WordPress Plugin
https://www.irbe.ch/migration-von-wordpress-zu-hugo/
### Herausforderungen
- WordPress hängt sich auf