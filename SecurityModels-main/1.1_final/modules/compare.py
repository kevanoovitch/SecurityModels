# ==============================================================================
# Author: Ludwig Sterner
# Email: luse23@student.bth.se
#
# Author: Kevin Deshayes
# Email: kede23@student.bth.se
# ==============================================================================
import os
import time
from modules.update_progress import update_progress


def compare(files, signatures):
    user = os.getlogin()
    allFiles = files
    checkedFiles = []

    with open("dv1667.log", "a") as of:
        for file in files:
            checkedFiles.append(file)
            update_progress(allFiles, checkedFiles)
            time.sleep(0.1)

            lf = str(file).split("/")[-1]
            with open(file, 'rb') as rf:
                data = rf.read()
                for key, values in signatures.items():
                    if values in data:
                        of.write(
                            f"\nName of compromised file: {lf}\nVirus: {key}\nPath of compromised path: {file}\nInfected user: {user}\n")
