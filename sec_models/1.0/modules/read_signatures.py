import os


def read_signatures(db_path="/Users/0x/Documents/GitHub/SecurityModels/sec_models/1.0/assets/signatures.db"):
    """
    Read signatures from a database and return them in a dictionary as bytes
    Argument: db_path -- path to the database.
    Returns: a dictionary with the signatures as keys and the corresponding signatures as values
    """

    signatures = {}
    try:
        if os.path.exists(db_path):
            with open(db_path, "r") as file:
                for line in file:
                    name, signature = line.strip().split("=")
                    modified_name = name
                    if len(name) > 32:
                        print(
                            f"{name} has a name exceeding 32 characters: {len(name)}")

                        modified_name += '****'

                    signatures[modified_name] = bytes.fromhex(signature)

    except OSError as e:
        print(f"Error: {e}")

    return signatures
