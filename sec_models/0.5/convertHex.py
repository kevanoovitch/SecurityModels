from readSignatures import readSignatures

def convertHex(signatures):
    suc_key = []
    for key, value in signatures.items():
        byte_string = bytes.fromhex(value)



        try:
            ascii_string = byte_string.decode('utf-8')
            ascii_string.replace("\n", "")
            print(f"Decoded string: {ascii_string} : {key}")
            suc_key.append(key)
        except UnicodeDecodeError as e:
            print(f"Error decoding: {e} : {key}")

    print(suc_key)
