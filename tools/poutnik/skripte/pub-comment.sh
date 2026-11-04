#!/bin/zsh
set -e
f="$1"; D=$(dirname "$f"); base=$(basename "$f" .md)
id=$(grep -m1 '^ID: ' "$f" | sed 's/^ID: //')
body=$(awk 'f{print} /^ID: /{getline; f=1}' "$f")
cd /Users/joerglohrer/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik
ngit --signer poutnik issue comment --repo nostr://laoc.xyz/reli-hub "$id" --body "$body" -d --json > "$D/$base.json" 2> "$D/$base.err"
cat "$D/$base.json"
