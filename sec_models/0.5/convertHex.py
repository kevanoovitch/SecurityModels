from readSignatures import readSignatures

def convertHex(signatures):
    for key, value in signatures.items():
         bytes_data = bytes.fromhex(value)
         print(key, ":",value, ":", bytes_data)

convertHex(readSignatures())
