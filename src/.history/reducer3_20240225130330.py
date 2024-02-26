import sys

total_requests = 0

for line in sys.stdin:
    request_line, _ = line.strip().split('\t')
    total_requests += 1

print("Total number of HTTP requests:", total_requests)
