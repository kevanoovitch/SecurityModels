# ==============================================================================
# Author: Ludwig Sterner
# Email: luse23@student.bth.se
#
# Author: Kevin Deshayes
# Email: kede23@student.bth.se
# ==============================================================================

import os
import sys
from io import StringIO
import os
import subprocess


def install_package(package):
    # Checks that the python-gnup pip package is installed
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def dir_check(directory_input):
    if os.path.exists(directory_input) and os.path.isdir(directory_input):
        print("Folder exists, going to next step")
    else:
        print("Folder does not exist or is not a directory.")
        newInput = input("Try a new directory path: ")
        dir_check(newInput)


def sign_check(signature_input):
    if os.path.exists(signature_input) and os.path.isfile(signature_input):
        print("Signature file found, going to next step.")
    else:
        print("Signature file does not exist or is not a file.")
        newInput = input("Try a new signature file path: ")
        sign_check(newInput)  # Recursively call sign_check with the new input


def utils():

    print("Welcome to KELU Antivirus.")

    print("Input directory path (absolute or relative):")
    directory_input = input()
    dir_check(directory_input)

    print("Input signature path (absolute or relative):")
    signature_input = input()
    sign_check(signature_input)

    return signature_input, directory_input
