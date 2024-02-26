import sys

ip_counts = {}

for line in sys.stdin:
    # Split the input line into IP address and count
    ip_address, count = line.strip().split('\t')
    
    # Update the IP counts dictionary
    ip_counts[ip_address] = ip_counts.get(ip_address, 0) + int(count)

# Find the IP with the highest count
most_accessed_ip = max(ip_counts, key=ip_counts.get)
total_accesses = ip_counts[most_accessed_ip]

# Output the most accessed IP and its access count
print("Most accessed IP:", most_accessed_ip)
print("Number of accesses:", total_accesses)
