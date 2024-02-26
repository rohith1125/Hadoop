import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 6:  # Ensure the line has enough parts
        date = data[3][1:12]  # Extract the date from the timestamp
        size = data[9] if data[9] != "-" else "0"  # Extract the size of the requested resource
        print(f"{date}\t{size}")  # Output date and size
