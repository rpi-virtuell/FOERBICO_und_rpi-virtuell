#!/bin/bash
FILE=$1
WEIGHT="weight: -20500101"
echo "working on >>"$FILE"<<"
DETECTED_DATE=$(grep datePublished $FILE | sed -E 's/datePublished...(2024)-(..)-(..)./\1\2\3/')
echo "weight to set: >>-"$DETECTED_DATE"<<"
sed -i "s/weight: xxx/weight: -${DETECTED_DATE}/" $FILE