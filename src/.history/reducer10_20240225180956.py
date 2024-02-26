import sys

requested_data = 0

target_date = "16/Jan/2022"  
target_status_code = "200"  # Set the target status code

for line in sys.stdin:
    date, status_code, size = line.strip().split('\t')  # Split date, status code, and size
    if date == target_date and status_code == target_status_code:  
        requested_data += int(size)  

print(f"Total data requested with status code 200 on {target_date}: {requested_data} bytes")
