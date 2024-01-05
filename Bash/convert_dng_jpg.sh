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

    # Convert DNG to PPM with specified dcraw parameters
    dcraw -c -w -H 5 -o 2 -r 7 4 6 -q 0.25 -D 0.33 "$input_file" > "${filename_noext}.ppm"
    
    """
    Explanation:
    - -c: Outputs the image data to stdout instead of creating a file.
    - -w: Uses the camera white balance if possible for color adjustment.
    - -H 5: Sets the highlight mode to 5 (rebuild) to reconstruct clipped highlights.
    - -o 2: Specifies the output colorspace (Adobe RGB in this case).
    - -r 7 4 6: Adjusts white balance by specifying multipliers for red, green, and blue channels.
    - -q 0.25: Sets image quality to 0.25, reducing file size at the cost of some quality.
    - -D 0.33: Specifies the linearization threshold for adjusting image linearization.
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
