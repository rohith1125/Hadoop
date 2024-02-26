import sys

unique_methods = set()

for line in sys.stdin:
    request_method, _ = line.strip().split('\t')
    unique_methods.add(request_method)

print("Number of HTTP request methods:", len(unique_methods))
print("HTTP request methods used:")
for method in unique_methods:
    print(method)
