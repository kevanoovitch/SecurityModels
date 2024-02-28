import os
import sys
from io import StringIO


def utils():
    sys.stdin = StringIO("assets/signatures.db")
    user_input = input("Input signature path (absolute or relative): ")

    if os.path.exists(user_input):
        print("Signature exists")
    print(user_input)
    sys.stdin = StringIO("assets/directory")
    user_input2 = input("Input file path (absolute or relative): ")

    if os.path.exists(user_input2):
        print("FIles exists")
    print(user_input2)

    return user_input, user_input2
