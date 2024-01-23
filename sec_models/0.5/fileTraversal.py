import os

# def fileTraversal(start_dir = "sec_models/abc"):
#     """
#     Finds all the files (recursivly) in the given directory
#     Argument: Path to directory to filter through.
#     Returns: A list off all sub-directories, paths(?) and files in directory
#     """

#     contents = os.listdir(start_dir)
#     tmp_list_files = []

#     for index in range(len(contents)):

#         file = contents[index]

#         file_path = os.path.join(start_dir, file)

#         if os.path.isdir(file_path):
#             testList = fileTraversal(file_path)
#             tmp_list_files.append(testList)

#         else:
#             tmp_list_files.append(file_path)
#     print(tmp_list_files)
#     return tmp_list_files

# fileTraversal("/Users/0x/Documents/GitHub/SecurityModels/sec_models/test_dir")


def fileTraversal(start_dir="sec_models/abc"):
    """
    Finds all the files (recursivly) in the given directory.
    Argument: Path to directory to filter through.
    Returns: A list off all sub-directories, paths(?) and files in directory
    """

    files_list = []
    try:
        for item in os.listdir(start_dir):
            item_path = os.path.join(start_dir, item)
            if os.path.isfile(item_path):
                files_list.append(item_path)
            elif os.path.isdir(item_path):
                files_list.extend(fileTraversal(item_path))
    except OSError as e:
        print(f"Error: {e}")
    return files_list