import fileTraversal

print("Input directory")
directory = input()

AllFiles = fileTraversal(directory)

# debug
print("------")
print(directory)

for index in range(len(AllFiles)):
    print(AllFiles[index])
