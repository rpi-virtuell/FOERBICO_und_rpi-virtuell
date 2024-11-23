#!/bin/bash
set -e

# script im root dir ausführen
working_directory=$(basename $(pwd))
if [ "$working_directory" != "FOERBICO" ]; then
  echo "not in root dir 'FOERBICO'"
  exit 1
fi

OURTMPDIR='tmp-8JmqbYUnu'
BLOGPOSTDIR='sb/content/posts'

mkdir -p "$OURTMPDIR"
touch "$OURTMPDIR/permalink-all.txt"
touch $OURTMPDIR/found-urls.txt

find Blog -type f -name '*.md' | while read FILE ;
do
  echo '* erstelle Verzeichnis für Post >>'$FILE'<<'
  post_directory=$(basename -s .md $FILE)
  mkdir -p "$BLOGPOSTDIR/$post_directory"
  echo '   - kopiere' $FILE 'ins Verzeichnis als index.md'
  cp "$FILE" "$BLOGPOSTDIR/$post_directory/index.md"

  #assets aus "wp-content" holen
  echo >> $OURTMPDIR/found-urls.txt
  echo "***********************   " $FILE "   *************************************" >> $OURTMPDIR/found-urls.txt
  echo >> $OURTMPDIR/found-urls.txt
  grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" "$FILE" >> $OURTMPDIR/found-urls.txt

  asset_link_list=$(grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" "$FILE" | grep wp-content | grep "oer\.community" | sed 's/http:/https:/g' | sort -u)
  cd "$BLOGPOSTDIR/$post_directory/"
  for wp_content_asset in $asset_link_list
  do
    echo "    - hole asset: "${wp_content_asset:33:934}
    asset_output_file_name=$(echo $wp_content_asset | rev | cut -d'/' -f 1 | rev)
    curl -s --remote-name $wp_content_asset --output "$asset_output_file_name"
  done
  cd ../../../..
done
