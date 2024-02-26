import sys

requested_data = 0

target_date = "19/Dec/2020"  # Set the target date for which we want 

for line in sys.stdin:
    date, size = line.strip().split('\t')  
    if date == target_date:  # Check if the 
        requested_data += int(size)  # Increment requested data by 

print(f"Total data requested on {target_date}: {requested_data} bytes")
