from read_signatures import read_signatures

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
                data = f.read()
                d_file[file] = data
                for key, value in signatures.items():
                    if value in data:
                        print(f"MATCH: {key}\n{value}\n")





    print("[END] Reading binary")