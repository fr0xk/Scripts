#!/bin/sh

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

# create an array to hold the excluded directories

declare -a excluded_dirs=("node_modules" "vendor")

# create a function to check if a directory should be excluded

should_exclude() {

    local dir="$1"

    for excluded_dir in "${excluded_dirs[@]}"; do

        if [ "$dir" = "$excluded_dir" ]; then

            return 0 # true

        fi

    done

    return 1 # false

}

# loop through each category and create a directory for it

for category in "${!categories[@]}"; do

    mkdir -p "$category"

done

# move each file to its respective category directory

for category in "${!categories[@]}"; do

    for file in ${categories["$category"]}; do

        find . -maxdepth 1 -name "$file" -not -path "./$category/*" -not -path "./.git/*" -type f -print0 | while read -r -d '' file_path; do

            dir=$(dirname "$file_path")

            if ! should_exclude "$(basename "$dir")"; then

                mv "$file_path" "$category"

            fi

        done

    done

done

# print out a list of files in each category directory

for category in "${!categories[@]}"; do

    echo "$category:"

    ls "$category"

    echo

done

