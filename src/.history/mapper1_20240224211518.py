import sys

def map_specific_directory_hits():
    target_directory = "/images/smiles/"
    for line in sys.stdin:
        try:
            parts = line.strip().split(' ')
            if len(parts) > 6:
                method, path, protocol = parts[5].strip('"').split()
                # Check if the requested path starts with the target directory
                if path.startswith(target_directory):
                    print(f"{path}\t1")
        except Exception as e:
            continue  # Skip any lines that do not match the expected format

if __name__ == "__main__":
    map_specific_directory_hits()
