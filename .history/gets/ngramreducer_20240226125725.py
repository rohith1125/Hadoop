import sys

current_ngram = None
current_count = 0

# Read input from stdin
for line in sys.stdin:
    line = line.strip()
    ngram, count = line.split('\t', 1)
    count = int(count)

    if current_ngram == ngram:
        current_count += count
    else:
        if current_ngram:
            # Emit n-gram and its frequency
            print('%s\t%d' % (current_ngram, current_count))
        current_ngram = ngram
        current_count = count

# Emit the last n-gram
if current_ngram:
    print('%s\t%d' % (current_ngram, current_count))