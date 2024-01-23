from scanDirectory import scanDirectory
def readBinary(file_arr):
    print("[START] Reading binary")
    for file in file_arr:
        if not "DS_Store" in file:
            f = open(file, 'rb')
            data = f.read()
            print(file, ":", data, "\n")
            f.close()

    print("[END] Reading binary")

readBinary(scanDirectory("/Users/0x/Documents/GitHub/SecurityModels/sec_models/test_dir"))