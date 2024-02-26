import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 0:
        ip_address = data[0]  # Extract the IP address
        print(ip_address + "\t1")
