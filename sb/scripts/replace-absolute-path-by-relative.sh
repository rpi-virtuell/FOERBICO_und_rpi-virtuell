#!/bin/bash
set -e

# script im root dir ausführen
working_directory=$(basename $(pwd))
if [ "$working_directory" != "FOERBICO" ]; then
  echo "not in root dir 'FOERBICO'"
  exit 1
fi

find sb/content -type f -name '*.md' | while read FILE ;
do
    sed -i -s -E 's|http.*://oer.community/wp-content/upload.+/.+/.+/||g' $FILE
    sed -i -s -E 's|http.*://pad..*/upload.*/.+/.+/||g' $FILE
    sed -i -s 's|../assets/images/blog/||g' $FILE
done

# Aufruf mit `$ sb/scripts/replace-absolute-path-by-relative.sh``