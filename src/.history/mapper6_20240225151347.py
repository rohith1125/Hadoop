import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = " ".join(data[5:-2])  # Extract the request line
        request_method = request_line.split()[0]  # Extract the HTTP request method
        print(request_method + "\t1")
