#!/bin/bash
set -e

# script im root dir ausführen
working_directory=$(basename $(pwd))
if [ "$working_directory" != "FOERBICO" ]; then
  echo "not in root dir 'FOERBICO'"
  exit 1
fi

find sb/public -type f | while read FILE ;
do
    sed -i -s -E 's|http://oer.community/|http://int.oer.community/|g' "$FILE"
    sed -i -s -E 's|https://oer.community/|https://int.oer.community/|g' "$FILE"
    #sed -i -s -E 's|https://oer.community/|https://xxx.oer.community/|g' "$FILE"
done
#TODO / FIXME: Basis-Ordner dynamsich; als Parameter