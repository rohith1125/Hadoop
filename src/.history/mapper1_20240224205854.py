import sys
import re

# Regular expression pattern to match the desired directory
47.39.156.135 - - [01/Apr/2022:15:21:59 +0200] "HEAD /templates/jp_hotel/images/smiles/ HTTP/1.1" 404 0 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)" "-"
directory_pattern = re.compile(r'^GET\s+/images//.*$')

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Check if the line matches the directory pattern
    if directory_pattern.match(line):
        # Emit key-value pair
        print("hits_to_smilies_directory\t1")
