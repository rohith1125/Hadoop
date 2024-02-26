#!/usr/bin/env python

import sys

total_hits = 0

# Read input from stdin
for line in sys.stdin:
    line = line.strip()
    hits, count = line.split('\t')
    total_hits += int(count)

print("Total hits to /images/smilies/:", total_hits)
