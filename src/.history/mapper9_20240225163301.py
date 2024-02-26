import sys

for line in sys.stdin:
    line = line.strip()
    if line:  # Check if the line is not empty
        data = line.split()
        if len(data) > 6:  # Ensure the line has enough parts
            ip = data[0]  # Extract the IP address
            size = int(data[-1]) if data[-1] != "-" else 0  # Extract the size of the requested resource
            print(f"{ip}\t{size}")  # Output IP address and size
