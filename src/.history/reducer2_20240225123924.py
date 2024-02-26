import sys

total_hits = 0

for line in sys.stdin:
    ip_address, count = line.strip().split('\t')
    total_hits += int(count)

print("Total hits from IP", target_ip + ":", total_hits)
