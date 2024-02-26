import sys

request_counts = {}

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = " ".join(data[5:-2])  
        request_method = request_line

        # Increment 
        request_counts[request_method] = request_counts.get(request_method, 0) + 1

        # Output the request method and a count of 1
        print(request_method + "\t1")

# Output the count for each request method at the end
for method, count in request_counts.items():
    print(method + "_count" + "\t" + str(count))
