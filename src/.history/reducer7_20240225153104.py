import sys

status_404_count = 0

for line in sys.stdin:
    status_code, count = line.strip().split('\t')  # Split status code and count
    if status_code == "404":  # Check if the status code is 404
        status_404_count += int(count)  # Increment count if status code is 404

print("Total number of requests with status code 404:", status_404_count)
