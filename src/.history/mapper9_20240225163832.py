import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) >= 10:
        ip = data[0]
        size = data[-1]
        # Check if the size is not a dash, then convert it to an integer
        if size != '-':
            size = int(size)
            print(f"{ip}\t{size}")
