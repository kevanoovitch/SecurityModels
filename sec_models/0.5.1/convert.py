def toHex(file_path):
    """
    Arg: File path 
    Tries to open file if succesfull converts contents t 
    Return: file content in hex
    """
    try:
        with open(file_path, 'rb') as file:
            # Read the file content in binary mode
            file_content = file.read()

            # Convert binary data to hexadecimal
            hex_representation = file_content.hex()

            return hex_representation
    except FileNotFoundError:
        return f"File '{file_path}' not found."


def toByte(file_path):
    
    """

   - **Description:** This function takes the path of a file as input, reads its content in binary mode, and returns the binary data as a bytes object.
   - **Parameters:**
     - `file_path` (str): The path to the file to be processed.
   - **Returns:**
     - (bytes): The binary representation of the file's content.
     - (str): If the file is not found, a message indicating the file is not found.
    """
    try:
        with open(file_path, 'rb') as file:
            # Read the file content in binary mode
            byte_representation = file.read()

            return byte_representation
    except FileNotFoundError:
        return f"File '{file_path}' not found."
