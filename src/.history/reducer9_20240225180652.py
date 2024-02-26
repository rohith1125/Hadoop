import sys

# Initialize a dictionary to store total data flow size 
ip_data = {}

# Read input 
for line in sys.stdin:
    # Split input 
    ip, size = line.strip().split('\t')
    size = int(size)
    # Update the total data flow size 
    if ip in ip_data:
        ip_data[ip] += size
    else:
        ip_data[ip] = size

# Sort the IP addresses based on their total data flow size 
sorted_ips = sorted(ip_data.items(), key=lambda x: x[1], reverse=True)

# Print the top 3 IPs and their total 
for ip, total_size in sorted_ips[:3]:
    print(f"{ip}\t{total_size}")
