import sys

requested_data = 0

target_date = "19/Dec/2020"  # Set the target date for which we want to calculate the requested data

for line in sys.stdin:
    date, size = line.strip().split('\t')  # Split date and size
    if date == target_date:  # Check if the date matches the target date
        requested_data += int(size)  # Increment requested data by the size of the resource

print(f"Total data requested on {target_date}: {requested_data} bytes")
