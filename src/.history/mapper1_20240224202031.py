#!/usr/bin/env python

import sys

# Read input from stdin
for line in sys.stdin:
    line = line.strip()
    # Extract the request path
    path = line.split()[6]
    if path.startswith("/images/smilies/"):
        print("hits\t1")
