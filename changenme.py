#!/usr/bin/env python3

import sys
import subprocess

# Open the file passed as command line argument
with open(sys.argv[1], 'r') as f:
    files = f.readlines()

# Iterate over each file and rename it
for file in files:
    file = file.strip()  # Remove leading/trailing whitespaces or newlines
    old_name = file
    new_name = file.replace("jane", "jdoe")
    
    # Run mv command to rename the file
    subprocess.run(["mv", old_name, new_name])
