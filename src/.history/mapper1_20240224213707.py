import sys
import re

# Regular expression pattern to match the desired directory
directory_pattern = re.compile(r"\s\/images\/smilies\/")

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # print(line)
    # Check if the line matches the directory pattern
    if directory_pattern.match(line):
        # Emit key-value pair
        print("hits_to_smilies_directory\t1")
