import sys

total_post_requests = 0

# Iterate through each line of input from the Mapper
for line in sys.stdin:
    # Split the input line into request method and count
    request_method, count = line.strip().split('\t')
    
    # If the request method is POST, update the total count of POST requests
    if request_method == 'POST':
        total_post_requests += int(count)

# Output the total count of POST requests
print("Total number of POST requests:", total_post_requests)
