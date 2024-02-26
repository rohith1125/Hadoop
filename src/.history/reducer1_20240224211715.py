import sys

    current_path = None
    current_count = 0

    for line in sys.stdin:
        path, count = line.strip().split('\t', 1)

        try:
            count = int(count)
        except ValueError:
            continue

        if path != current_path:
            if current_path:
                # Emit total count for the previous path
                print(f"{current_path}\t{current_count}")
            current_path = path
            current_count = count
        else:
            current_count += count

    # Emitting the last path count if not None
    if current_path:
        print(f"{current_path}\t{current_count}")