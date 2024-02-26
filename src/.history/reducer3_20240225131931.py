import sys

# Initialize a dictionary to store counts of each request method
request_counts = {}

# Initialize a counter to store the total number of HTTP requests
total_requests = 0

for line in sys.stdin:
    # Split the input line into request method and count
    data = line.strip().split('\t')
    if len(data) == 2:
        if data[0].endswith("_count"):
            # Update the total number of HTTP requests
            total_requests += int(data[1])
        else:
            # Update the counts of each request method
            request_counts[data[0]] = request_counts.get(data[0], 0) + int(data[1])

# Output the total count for each request method
for method, count in request_counts.items():
    print(method, count, sep='\t')

# Output the total number of HTTP requests
print("Total_HTTP_requests", total_requests, sep='\t')
