import os

# def fileTraversal(start_dir = "sec_models/abc"):
#     """
#     Finds all the files (recursivly) in the given directory
#     Argument: Path to directory to filter through.
#     Returns: A list off all sub-directories, paths(?) and files in directory
#     """

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
