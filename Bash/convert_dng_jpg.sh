#!/bin/sh

# Check if dcraw is installed
if ! command -v dcraw >/dev/null 2>&1; then
    echo "Error: dcraw is required but not installed. Please install it using 'pkg install dcraw'. Aborting."
    exit 1
fi

# Check if imagemagick is installed
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

    # Convert DNG to PPM with specified dcraw parameters
    dcraw -v -c -o 0 -q 3 -n 25 -H 2 -C 0.25 7 -6 -T "$input_file" > "${filename_noext}.ppm"
    
    """
    Explanation:
    - -v: Print verbose messages.
    - -c: Write image data to standard output.
    - -o 0: Output colorspace set to raw.
    - -q 3: Set the interpolation quality to a high level.
    - -n 25: Set threshold for wavelet denoising to reduce noise by 25%.
    - -H 2: Highlight mode set to blend to reduce chromatic noise.
    - -C 0.25 7: Correct chromatic aberration with a chroma threshold of 7.
    - -6: Write 16-bit instead of 8-bit for higher quality.
    - -T: Write TIFF instead of PPM for high-quality output.
    - "$input_file": Specifies the input raw file.
    - > "${filename_noext}.ppm": Redirects output to a PPM file with the same name as the input file.
    """

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
