#!/bin/sh

# Check if pandoc is installed
if ! command -v pandoc >/dev/null 2>&1; then
    echo "pandoc is not installed. Please install pandoc and try again."
    exit 1
fi

# Parse command-line arguments
input_file=""
output_format="html"
output_file="output.html"
syntax_highlighting="false"
generate_toc="false"

while [ $# -gt 0 ]; do
    case $1 in
        -i|--input)
            input_file="$2"
            shift 2
            ;;
        -f|--format)
            output_format="$2"
            shift 2
            ;;
        -o|--output)
            output_file="$2"
            shift 2
            ;;
        -s|--syntax-highlighting)
            syntax_highlighting="true"
            shift
            ;;
        -t|--toc)
            generate_toc="true"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check if input file is specified
if [ -z "$input_file" ]; then
    echo "No input file specified. Please specify an input file using the -i or --input option."
    exit 1
fi

# Check if input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file does not exist: $input_file"
    exit 1
fi

# Convert the input file to the desired output format
case $output_format in
    html)
        if [ "$syntax_highlighting" = "true" ]; then
            pandoc "$input_file" -o "$output_file" --syntax-highlighting --self-contained
        else
            pandoc "$input_file" -o "$output_file" --self-contained
        fi
        ;;
    pdf)
        if [ "$generate_toc" = "true" ]; then
            pandoc "$input_file" -o "$output_file" --toc --pdf-engine=pdflatex
        else
            pandoc "$input_file" -o "$output_file" --pdf-engine=pdflatex
        fi
        ;;
    epub)
        pandoc "$input_file" -o "$output_file"
        ;;
    *)
        echo "Unknown output format: $output_format"
        exit 1
        ;;
esac

# Check if output file exists
if [ ! -f "$output_file" ]; then
    echo "Output file not created: $output_file"
    exit 1
fi

# Display the output file
case $output_format in
    html)
        if command -v lynx >/dev/null 2>&1; then
            lynx "$output_file"
        else
            echo "No viewer found for HTML output. Please install lynx or another HTML viewer."
        fi
        ;;
    pdf)
        if command -v zathura >/dev/null 2>&1; then
            zathura "$output_file"
        else
            echo "No viewer found for PDF output. Please install zathura or another PDF viewer."
        fi
        ;;
    epub)
        if command -v fbreader >/dev/null 2>&1; then
            fbreader "$output_file"
        else
            echo "No viewer found for EPUB output. Please install fbreader or another EPUB viewer."
        fi
        ;;
esac

