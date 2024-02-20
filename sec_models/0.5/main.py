from fileTraversal import fileTraversal

print("Input directory")
directory = input()

AllFiles_list = fileTraversal(directory)

# debug
print("------")
print(directory)

for index in range(len(AllFiles_list)):
    print(AllFiles_list[index])
