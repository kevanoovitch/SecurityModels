from file_traversal import file_traversal

def convert_bytes(read_files):

    converted_files = {}

    for file in read_files:
        with open(file, 'rb') as f:
            data = f.read()

            converted_files[file] = data[1:2];


    print(converted_files)


convert_bytes(file_traversal())