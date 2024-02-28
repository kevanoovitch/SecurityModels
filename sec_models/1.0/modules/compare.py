# def compare(files, signatures):
#     f = open("dv1667.txt", "a")

#     for file in files:
#         with open(file, 'rb') as f:
#             data = f.read()
#             for key, values in signatures.items():
#                 if values in data:
#                     #print("MATCH: ", key, "in ", file)
#                     f.write(f"Compromised file: [Filename] | Virus: {key} | Compromised file path: {file} \n")

def compare(files, signatures):
    with open("dv1667.log", "w") as output_file:
        for file in files:

            lf = str(file).split("/")[-1]

            with open(file, 'rb') as read_file:
                data = read_file.read()
                for key, values in signatures.items():
                    if values in data:
                        #print("MATCH: ", key, "in ", file)
                        output_file.write(f"Compromised file: {lf} | Virus: {key} | Compromised file path: {file} \n")
