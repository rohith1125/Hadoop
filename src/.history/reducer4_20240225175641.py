import sys

path_counts = {}

for line in sys.stdin:
    # Split the input line into path and count
    path, count = line.strip().split('\t')
    
    # Update the path counts dictionary
    path_counts[path] = path_counts.get(path, 0) + int(count)

# Find the path with the highest count
most_hit_path = max(path_counts, key=path_counts.get)
total_hits = path_counts[most_hit_path]

# Output the most hit path and its hit count
print("Most hit path:", most_hit_path)
print("Number of hits:", total_hits)