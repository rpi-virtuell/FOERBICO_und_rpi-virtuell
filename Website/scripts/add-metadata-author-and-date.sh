#!/bin/bash
set -e

# script im root dir ausführen
working_directory=$(basename $(pwd))
if [ "$working_directory" != "FOERBICO" ]; then
  echo "not in root dir 'FOERBICO'"
  exit 1
fi

find sb/content/posts -type f -name 'index.md' | while read FILE ;
do
    awk -f sb/scripts/move-author.awk $FILE > $FILE.out
    awk -f sb/scripts/move-date.awk $FILE.out > $FILE.out2
    mv $FILE.out2 $FILE
    rm $FILE.out
done