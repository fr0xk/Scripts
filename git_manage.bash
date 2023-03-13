#!/bin/bash

# create an associative array to hold the categories and their corresponding file extensions

declare -A categories

categories["code"]="*.c *.cpp *.h *.hpp *.py *.js *.html *.css"

categories["documents"]="*.txt *.md *.doc *.pdf"

categories["images"]="*.png *.jpg *.gif"

categories["archives"]="*.zip *.tar.gz *.tgz"

categories["videos"]="*.mp4 *.avi *.mov"

categories["audio"]="*.mp3 *.wav *.flac"

categories["data"]="*.csv *.tsv *.json *.xml"

categories["binaries"]="*.exe *.dll *.so"

categories["misc"]="*"

# loop through each category and create a directory for it

for category in "${!categories[@]}"; do

    mkdir -p "$category"

done

# move each file to its respective category directory

for category in "${!categories[@]}"; do

    for file in ${categories["$category"]}; do

        find . -maxdepth 1 -name "$file" -exec mv {} "$category" \;

    done

done

# print out a list of files in each category directory

for category in "${!categories[@]}"; do

    echo "$category:"

    ls "$category"

    echo

done

