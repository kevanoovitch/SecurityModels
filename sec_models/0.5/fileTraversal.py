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

"""
    find_files(path):

    
    # Lista hela innehållet på nuvarande directory
    contents = os.listdir(path)
    tmp_files_list = []

    for index in range(len(contents)):
        file = contents[index]

        # Kommer ge sökvägen för objektet 'file'
        file_path = path + "/" + file

        # Om det är en ett sub-directory anropa funktionen igen med nuvarande mappens sökväg
        if os.path.isdir(file_path):
            testList = find_files(file_path)
            tmp_files_list.extend(testList)

        # Om det är en fil lägg till filens sökväg i tmp_files_listan
        else:
            tmp_files_list.append(file_path)

    return tmp_files_list


"""