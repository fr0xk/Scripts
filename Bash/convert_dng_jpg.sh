#!/bin/sh

# Check if dcraw and imagemagick are installed
if ! command -v dcraw >/dev/null 2>&1; then
    echo "Error: dcraw is required but not installed. Please install it using 'pkg install dcraw'. Aborting."
    exit 1
fi

if ! command -v convert >/dev/null 2>&1; then
    echo "Error: imagemagick is required but not installed. Please install it using 'pkg install imagemagick'. Aborting."
    exit 1
fi

# Check if input files are provided
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <input_file1.dng> [<input_file2.dng> ...]"
    exit 1
fi

# Process each input file
for input_file in "$@"; do
    # Check if the input file exists
    if [ ! -f "$input_file" ]; then
        echo "Warning: File '$input_file' not found. Skipping."
        continue
    fi

    # Extract original filename without extension
    filename=$(basename -- "$input_file")
    filename_noext="${filename%.*}"

    # Convert DNG to JPEG with color balance and noise reduction using dcraw
    # -c: Output to stdout
    # -w: Use camera white balance
    # -q 3: Set quality to highest
    # -o 2: Apply Auto level stretch
    # -T: Write 16-bit TIFF
    # -H 5: Set chromatic noise reduction to 5
    # -W: Enable luminance noise reduction
    # -b 2.2: Set color balance
    dcraw -c -w -q 3 -o 2 -T -H 5 -W -b 2.2 "$input_file" > "${filename_noext}.ppm"

    if [ $? -eq 0 ]; then
        # Convert the intermediate PPM to JPEG with imagemagick
        # -colorspace sRGB: Ensure the output is a color image, not black and white
        # -quality 100: Set JPEG quality to the highest
        convert -colorspace sRGB -quality 100 "${filename_noext}.ppm" "${filename_noext}.jpg"

        # Optional: Delete intermediate PPM file
        # rm "${filename_noext}.ppm"

        echo "Conversion complete: ${filename_noext}.jpg"
    else
        echo "Error: Conversion failed for $input_file. Skipping."
    fi
done
