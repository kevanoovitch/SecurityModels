from file_traversal import file_traversal

def convert_bytes(read_files):

    converted_files = {}

    for file in read_files:

        try:
            text = open(file, 'r', encoding='utf-8').read()
        except UnicodeDecodeError:
            text = open(file, 'r', encoding='ISO-8859-1').read()  # Try a different encoding


        data = text
        converted_files[file] = data


    print(converted_files)


convert_bytes(file_traversal())