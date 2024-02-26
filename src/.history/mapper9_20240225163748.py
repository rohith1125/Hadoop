import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) >= 10:
        ip = data[0]
        size = int(data[-1])
        print(f"{ip}\t{size}")
