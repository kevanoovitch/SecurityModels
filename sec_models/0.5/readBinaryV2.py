from fileTraversal import fileTraversal

def readBinary2(file_arr):
    """
    Arg: Takes in a list of files paths
    Return: Dictioanry with { file : binary file }
    """
 # NEEDS TO BE SOLVED
    Binary_dict = {}

    print("[START] Reading binary")
   
    for file_path in file_arr:
        file_name = file_path.split('/')[-1]  # Extract file name from path
        if not file_name.startswith('.'):  # Skip hidden files (like .DS_Store on macOS)
            try:
                with open(file_path, 'rb') as file:
                    byte_content = file.read()
                    binary_string = ''.join(format(byte, '08b') for byte in byte_content)
                    Binary_dict[file_name] = binary_string
            except IOError as e:
                print("Error opening file")
    print("[END] Reading binary")
    return Binary_dict
# fileTraversal
    

readBinary2(fileTraversal("C:\GitClones\SecurityModels\sec_models\test_dir"))


