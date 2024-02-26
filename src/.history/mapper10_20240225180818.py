import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 6:  # Ensure the line has enough 
        date = data[3][1:12]  # Extract the date from the 
        status_code = data[8]  # Extract the 
        size = data[9] if data[9] != "-" else "0"  # Extract the size of the requested 
        print(f"{date}\t{status_code}\t{size}")  # Output date, status code, 
