import sys

def generate_ngrams(text, n):
    ngrams = []
    for i in range(len(text) - n + 1):
        ngrams.append(text[i:i+n])
    return ngrams

# Read input from stdin
text = sys.stdin.read().strip().lower()

# Get n from command-line argument
n = int(sys.argv[1])

# Split text into words
words = text.split()
for word in words:
    # Generate n-grams for each word
    ngrams = generate_ngrams(word, n)
    for ngram in ngrams:
        # Emit n-gram and count of 1
        print('%s\t%d' % (ngram, 1))