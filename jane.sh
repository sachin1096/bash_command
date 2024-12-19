#!/bin/bash

# Create or clear the oldFiles.txt file
> oldFiles.txt

# Search for all lines containing 'jane' and store the file paths in 'files'
files=$(grep 'jane' ~/data/list.txt | cut -d' ' -f3)

# Iterate over the files and check if they exist
for file in $files; do
    if test -f "$file"; then
        # If the file exists, append it to oldFiles.txt
        echo "$file" >> oldFiles.txt
    fi
done
