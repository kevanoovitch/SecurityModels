import os

def readSignatures(db_path = "sec_models/0.5/signatures.db"):
    signatures = {}

    if os.path.exists(db_path):
        with open(db_path, "r") as signatureFile:
            for line in signatureFile:
                name, signature = line.strip().split("=")
                if not len(name) > 32:
                    signatures[name] = signature    
                
    else:
        print("[ERROR]: Signatures can't be located.")

    return signatures

