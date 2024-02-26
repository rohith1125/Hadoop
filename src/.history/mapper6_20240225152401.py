import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = data[5]  # Extract the request line
        print(request_line)
        if request_line[0] == "\"POST":
            print("POST" + "\t1")
