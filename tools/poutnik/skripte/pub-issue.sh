#!/bin/zsh
# usage: pub-issue.sh <entwurf.md>  -> schreibt <entwurf>.json und gibt nevent aus
set -e
f="$1"; D=$(dirname "$f"); base=$(basename "$f" .md)
title=$(grep -m1 '^TITEL: ' "$f" | sed 's/^TITEL: //')
labels=$(grep -m1 '^LABEL: ' "$f" | sed 's/^LABEL: //' | tr ',' '\n' | sed 's/^ *//;s/ *$//')
body=$(awk 'f{print} /^LABEL: /{getline; f=1}' "$f")
args=()
while IFS= read -r l; do [ -n "$l" ] && args+=(--label "$l"); done <<< "$labels"
cd /Users/joerglohrer/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik
ngit --signer poutnik issue create --repo nostr://laoc.xyz/reli-hub --subject "$title" --body "$body" "${args[@]}" -d --json > "$D/$base.json" 2> "$D/$base.err"
cat "$D/$base.json"
