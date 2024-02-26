import sys

for line in sys.stdin:
    data = line.strip().split()
    print(data)
    if len(data) > 8:  # Ensure the line has enough parts
        status_code = data[8]  # Extract the status code
        print(status_code + "\t1")  # Output status code with count of 1
