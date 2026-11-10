# syntax=docker/dockerfile:1
#
# Statische Auslieferung der HTML-Seiten aus dem Ordner "docs".
#
# Whitelist: Ausgeliefert werden nur *.html-Dateien aus docs/ (inkl. Unterordner).
# Alles andere (Markdown, JSON, Quellcode, .env, .git, app.yaml, Dockerfile usw.)
# bleibt draußen. docs/ wird zur Wurzel der Website: docs/foo.html -> /foo.html
# Das Caddyfile liefert versteckte Pfade mit 404 aus.

FROM alpine:3 AS filefilter
WORKDIR /src
COPY docs/ .
RUN mkdir /out && \
    find . -type f -name '*.html' \
        -exec sh -c 'mkdir -p "/out/$(dirname "$1")" && cp "$1" "/out/$1"' _ {} \;

FROM caddy:2-alpine
# Caddys mitgelieferte Begrüßungsseite (index.html) entfernen
RUN rm -rf /usr/share/caddy/*
COPY --from=filefilter /out /usr/share/caddy
RUN printf '%s\n' \
    ':80 {' \
    '    root * /usr/share/caddy' \
    '    @hidden path /.* /app.yaml /Dockerfile' \
    '    respond @hidden 404' \
    '    file_server browse' \
    '}' > /etc/caddy/Caddyfile
