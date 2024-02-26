import sys

post_count = 0

for line in sys.stdin:
    request_method, count = line.strip().split('\t')

    if request_method == "POST":
        post_count += int(count)

# Output the total count of "POST" requests
print("Total count of POST requests:", post_count)
