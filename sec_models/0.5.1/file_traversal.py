import os



def file_traversal(path="/Users/0x/Documents/GitHub/SecurityModels/sec_models/test_dir"):
    """
    Finds all the files in the given directory.
    Argument: Path with files to be traversed.
    Returns: List of all files in the given directory.
    """

    all_files = []
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                all_files.append(item_path)
            elif os.path.isdir(item_path):
                all_files.extend(file_traversal(item_path))
    except OSError as e:
        print(f"Error: {e}")
    return all_files