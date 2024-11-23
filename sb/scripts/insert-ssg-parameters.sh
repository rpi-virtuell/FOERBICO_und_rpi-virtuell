#!/bin/bash
FILE=$1
SSG_PARAMETER_TEMPLATE='sb/content/posts/_staticSiteGenerator_.yaml'

echo "working on >>"$FILE"<<"

sed -i -e '/oerCommunityPermalink/e cat sb\/content\/posts\/_staticSiteGenerator_.yaml' $FILE

echo ' - extract'
SSG_TITLE=$(grep -E "^# " $FILE | sed 's/# //')
SSG_COVER_IMAGE=$(grep -E "^image:" $FILE | cut -d: -f2 | tr -d ' ')
sed -n -E '/^description:/,/^\S/{p;/zweitwo/q}' $FILE | head -n -1 | sed 's/description:/summary:/' > _ssg-summary
SSG_URL=$(grep "oerCommunityPermalink" "$FILE" | cut -d/ -f 4)

echo ' - replace var'
sed -i "s/title: TITLE/title: ${SSG_TITLE}/" $FILE
sed -i "s/image: COVER-IMAGE/image: ${SSG_COVER_IMAGE}/" $FILE
sed -i "s/url: URL/url: ${SSG_URL}/" $FILE

echo ' - replace text'
if [ -f _ssg-summary ]; then
    sed -i -e '/summary: SUMMARY/e cat _ssg-summary' $FILE
    rm _ssg-summary
fi