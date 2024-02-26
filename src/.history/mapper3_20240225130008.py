import sys
import re

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = " ".join(data[5:-2])  # Extract the request line
        # Use regular expression to extract the request method
        match = re.match(r'\"(\w+)\s+', request_line)
        if match:
            request_method = match.group(1)
            print(request_method + "\t1")
