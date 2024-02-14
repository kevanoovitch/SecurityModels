from read_signatures import read_signatures
from file_traversal import file_traversal

def  convert_files(files):
    """Takes and input of an array of paths to files that needs to be read as binary.
    Argument: Array with file paths.
    Returns: Binary version of given paths (files).
    """

    signatures = read_signatures()
    d_file = {}
    print("[START] Reading binary")
    for file in files:
        with open(file, 'rb') as f:
                data = f.read().hex()
                d_file[file] = data

    print(d_file)






    print("[END] Reading binary")

convert_files((file_traversal()))