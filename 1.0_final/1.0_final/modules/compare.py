# ==============================================================================
# Author: Ludwig Sterner
# Email: luse23@student.bth.se
#
# Author: Kevin Deshayes
# Email: kede23@student.bth.se
# ==============================================================================

def compare(files, signatures):
    with open("dv1667.log", "a") as of:
        for file in files:
            lf = str(file).split("/")[-1]
            with open(file, 'rb') as rf:
                data = rf.read()
                for key, values in signatures.items():
                    if values in data:
                        of.write(
                            f"Compromised file: {lf} | Virus: {key} | Compromised file path: {file} \n")
