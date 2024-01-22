# _____________________
import os


def fileTraversal(path):
    files_list = []
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                files_list.append(item_path)
            elif os.path.isdir(item_path):
                files_list.extend(fileTraversal(item_path))
    except OSError as e:
        print(f"Error: {e}")
    print(files_list)
    return files_list


fileTraversal(
    "/home/kevin/Github Repository/AntiVirus/SecurityModels/sec_models/test_dir")
