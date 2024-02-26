import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = data[5]
        request_method = request_line.split()[0]
        print(request_method + "\t1")
