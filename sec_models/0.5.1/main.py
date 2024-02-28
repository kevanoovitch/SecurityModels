from file_traversal import file_traversal
from read_signatures import read_signatures

files = file_traversal()
signatures = read_signatures()

for file in files:
    with open(file, 'rb') as f:
        data = f.read()
        for key, values in signatures.items():
            if values in data:
                print("MATCH: ", key, "in ", file)
