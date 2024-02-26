import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 6:  # Ensure the line 
        date = data[3][1:12]  # Extract the date 
        status_code = data[8]  # 
        size = data[9] if data[9] != "-" else "0"  # Extract the size of 
        print(f"{date}\t{status_code}\t{size}")  # Output date, status 
