import os
def fileTraversal(startDir):
    """
    Finds all the files (recursivly) in the given directory 
    Argument: A directory path 
    Returns: a list off all sub directories paths(?) and files in directory
    
    """

    contents = os.listdir(startDir)
    tmp_list_files = []

    for index in range(len(contents)):
        file = contents[index]

        file_path = os.path.join(startDir, file)

        if os.path.isdir(file_path):
            testList = fileTraversal(file_path)
            tmp_list_files.extend(testList)
        
        else:
            tmp_list_files.append(file_path)
    return tmp_list_files
