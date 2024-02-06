import os

def readSignatures(db_path = "sec_models/0.5/signatures.db"):
    """ Return signatures as a dictionary of virus database.
        Argument: Path to 'signature.db' (has default).
        Returns: Dictionary of signatures with name and value.
    """
    signatures = {}
    try:
        if os.path.exists(db_path):
            with open(db_path, "r") as signatureFile:
                for line in signatureFile:
                    name, signature = line.strip().split("=")
                    if not len(name) > 32:
                        signatures[name] = signature.hex()
    except OSError as e:
        print(f"Error: {e}")

    return signatures
