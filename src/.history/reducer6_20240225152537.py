import sys

post_count = 0

# Iterate through each line of input from the Mapper
for line in sys.stdin:
    # Remove leading and trailing whitespace and split the line by tab character
    request_method, count = line.strip().split('\t')

    # Check if the request method is "POST"
    if request_method == "POST":
        # Increment the count of "POST" requests
        post_count += int(count)

# Output the total count of "POST" requests
print("Total count of POST requests:", post_count)
