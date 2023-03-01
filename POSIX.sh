#!/bin/sh

# This script demonstrates the use of various Unix shell tools and features in strict compliance with the POSIX shell standard.

# Set a variable

MY_VAR="Hello, world!"

# Print the variable

echo "$MY_VAR"

# Use command substitution to get the current date

DATE=$(date)

# Print the date

echo "$DATE"

# Use the test command to check if a file exists

if test -f "myfile.txt"; then

  echo "myfile.txt exists"

else

  echo "myfile.txt does not exist"

fi

# Use the for loop to iterate over a list of items

for ITEM in "apple" "banana" "cherry"; do

  echo "$ITEM"

done

# Use the while loop to read lines from a file

while read LINE; do

  echo "$LINE"

done < myfile.txt

# Use the case statement to perform pattern matching

FRUIT="apple"

case $FRUIT in

  "apple")

    echo "It's an apple!"

    ;;

  "banana")

    echo "It's a banana!"

    ;;

  *)

    echo "I don't know what it is!"

    ;;

esac

# Use the awk command to manipulate text

echo "1,2,3" | awk -F "," '{print $2}'

# Use the sed command to replace text

echo "Hello, world!" | sed 's/world/POSIX/'

# Use the grep command to search for text

echo "apple banana cherry" | grep "banana"

# Use the cut command to extract fields from text

echo "apple,banana,cherry" | cut -d "," -f 2

# Use the sort command to sort lines of text

echo "apple banana cherry" | tr " " "\n" | sort

# Use the uniq command to remove duplicate lines of text

echo "apple banana apple cherry" | tr " " "\n" | sort | uniq

# Use the wc command to count lines, words, and characters in text

echo "apple banana cherry" | wc

# Use the expr command to perform arithmetic operations

SUM=$(expr 2 + 2)

echo "2 + 2 = $SUM"

# Use the exit command to exit the script with a status code

exit 0

