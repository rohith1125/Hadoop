import sys

request_counts = {}

# Process each line of input separately
for line in sys.stdin:
    # Split the input line into request method and count
    request_method, count = line.strip().split('\t')
    
    # Update the request counts dictionary
    request_counts[request_method] = request_counts.get(request_method, 0) + int(count)

    # Output the current count for each request method
    print(request_method, request_counts[request_method], sep='\t')
