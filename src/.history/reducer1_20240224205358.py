#!/usr/bin/env python

import sys

total_hits = 0

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Increment total hits for each input
    total_hits += 1

# Output the total hits
print(f"Total hits to /images/smilies/: {total_hits}")

