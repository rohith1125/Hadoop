import sys
import re

# Regular expression pattern to match the desired directory


# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # print(line)
    # Check if the line matches the directory pattern
    if re.match(r"\s\/images\/smilies\/",line):
        # Emit key-value pair
        print("hits_to_smilies_directory\t1")
