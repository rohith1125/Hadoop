import sys
import re

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\s\/images\/smilies\/",line):
        # Emit key-value pair
        print("hits_to_smilies_directory\t1")