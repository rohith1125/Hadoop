import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = data[5]  # Extract the request line
        request_parts = request_line.split()  # Split the request line into parts
        if len(request_parts) > 0:
            request_method = request_parts[0]  # Extract the HTTP request method
            print(request_method + "\t1")
