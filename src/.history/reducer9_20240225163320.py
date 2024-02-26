import sys

current_ip = None
total_size = 0

for line in sys.stdin:
    line = line.strip()
    if line:  # Check if the line is not empty
        ip, size = line.split("\t")
        size = int(size)
        
        # If the IP address changes, print the total size for the previous IP
        if current_ip and current_ip != ip:
            print(f"{current_ip}\t{total_size}")
            total_size = 0  # Reset total size for the new IP
            
        current_ip = ip
        total_size += size

# Print the total size for the last IP
if current_ip:
    print(f"{current_ip}\t{total_size}")
