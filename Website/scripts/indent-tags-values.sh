#!/bin/bash
set -e

# script im root dir ausführen
working_directory=$(basename $(pwd))
if [ "$working_directory" != "FOERBICO" ]; then
  echo "not in root dir 'FOERBICO'"
  exit 1
fi

find Website/content -type f -name 'index.md' | while read FILE ;
do
    #sed -i -s -E 's|^- |  - |g' $FILE
    sed -i '/^---$/,/^---$/ {
        /^- / s/^/  /
    }' $FILE
done


#sed '/^---$/,/^---$/ { /^-/ s/^/  / }' input.md
#$sed '/^---$/,/^---$/ { /^- / s/^/  / }' Website/content/posts/2025-04-11-OER-Hochschulreihe-Teil-3/index.md | less
