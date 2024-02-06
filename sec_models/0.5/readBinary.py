from fileTraversal import fileTraversal

def readBinary(file_arr):
    """Takes and input of an array of paths to files that needs to be read as binary.
    Argument: Array with file paths.
    Returns: Binary version of given paths (files).
    """
 # NEEDS TO BE SOLVED


    print("[START] Reading binary")
    for file in file_arr:
        if not "DS_Store" in file:
            f = open(file, 'rb')
            data = f.read()
            print("index:",file,":", data, "\n")
            f.close()



    print("[END] Reading binary")
# fileTraversal
    

readBinary(fileTraversal("/Users/0x/Documents/GitHub/SecurityModels/sec_models/abc"))