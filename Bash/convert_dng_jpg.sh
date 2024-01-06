#!/bin/bash

# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright 2024 <Sudarshan Kakoty>

# 1. Check for required tools
check_tool() {
    if ! command -v "$1" >/dev/null 2>&1; then
        echo "Error: $1 is required but not installed. Please install it using 'pkg install $1'. Aborting."
        exit 1
    fi
}

check_tool dcraw
check_tool convert

# 2. Check for input files
if [ $# -eq 0 ]; then
    echo "Usage: $0 <input_file1.dng> [<input_file2.dng> ...]"
    exit 1
fi

# 3. Process each input file
for input_file in "$@"; do
    # Extract original filename without extension
    filename=$(basename -- "$input_file")
    filename_noext="${filename%.*}"

    # 5. Convert DNG to PPM with high quality and chromatic noise reduction
    dcraw -4 -H 0 -e -W -q 3 -n 25 -H 2 -C 0.25 7 -6 -T "$input_file" > "${filename_noext}.ppm"

    # Explain dcraw arguments in a comment below:
    # -4: Highest quality processing.
    # -H 0: No highlight/shadow adjustment.
    # -e: Embed EXIF data in output file.
    # -W: Automatically white balance the image.
    # -q 3: High interpolation quality.
    # -n 25: Wavelet denoising strength at 25%.
    # -H 2: Blending highlight mode for chromatic noise reduction.
    # -C 0.25 7: Chromatic aberration correction with threshold of 7.
    # -6: Output 16-bit TIFF for higher quality.
    # -T: Save output as TIFF for better conversion by ImageMagick.

    if [ $? -eq 0 ]; then
        # 6. Convert PPM to JPEG with high quality and sRGB colorspace
        convert -quality 100 -colorspace sRGB "${filename_noext}.ppm" "${filename_noext}.jpg"

        # Optionally remove intermediate PPM file
        # rm "${filename_noext}.ppm"

        echo "Conversion complete: ${filename_noext}.jpg"
    else
        echo "Error: Conversion failed for $input_file. Skipping."
    fi
done

echo "Processed $#@ files."

exit 0
