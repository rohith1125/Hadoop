import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = " ".join(data[5:-2])  # Extract the request line
        print(request_line + "\t1")
