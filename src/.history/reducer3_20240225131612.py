import sys

request_counts = {}

# Iterate through each line of input from the Mapper
for line in sys.stdin:
    # Split the input line into request method and count
    request_method, count = line.strip().split('\t')
    
    # Update the request counts dictionary
    request_counts[request_method] = request_counts.get(request_method, 0) + int(count)

# Output the total count for each request method
for method, count in request_counts.items():
    print(method, count, sep='\t')
