# ==============================================================================
# Author: Ludwig Sterner
# Email: luse23@student.bth.se
#
# Author: Kevin Deshayes
# Email: kede23@student.bth.se
# ==============================================================================
from modules.file_traversal import file_traversal
import gnupg
import os
gpg = gnupg.GPG()


def critical_files():
    # Gets the parent dir
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    critical_files_dir = parent_dir

    critical_files = file_traversal(critical_files_dir)

    # filter out '/directory'
    critical_files = [
        file for file in critical_files if 'assets/directory' not in file]

    # filter out python cache
    critical_files = [
        file for file in critical_files if 'modules/__pycache__' not in file]

    # filter out the log file
    critical_files = [
        file for file in critical_files if 'dv1667.log' not in file]

    # filter out .DS_Store files
    critical_files = [
        file for file in critical_files if not file.endswith('.DS_Store')]

    # filter out existing file signatures
    critical_files = [
        file for file in critical_files if 'assets/file_signatures' not in file]

    return critical_files


# 1. sign all files (and put in a directory)
# ============================


signatures_dir = "assets/file_signatures"
publicKeyPath = "assets/mypublickey.asc"


def import_public_key_if_missing(key_path, email):
    # List all keys in the keyring to check if the required key is already imported
    public_keys = gpg.list_keys()
    key_already_imported = False

    # Assuming you know a unique identifier for your key (e.g., email or key fingerprint)
    key_identifier = email

    for key in public_keys:
        if key_identifier in key['uids'][0]:
            key_already_imported = True
            break

    # If the key is not found in the keyring, import it
    if not key_already_imported:
        with open(key_path, 'rb') as f:
            key_data = f.read()
            import_result = gpg.import_keys(key_data)
            if import_result.count == 1:
                print(f"Public key {key_identifier} imported successfully.")
            else:
                print("Failed to import the public key.")
    else:
        print(f"Public key {key_identifier} is already in the keyring.")


def sign_files(email):
    gpg = gnupg.GPG()

    # Checks that public key is on the keyring
    import_public_key_if_missing(publicKeyPath, email)

    # Checks that signatures directory exists
    os.makedirs(signatures_dir, exist_ok=True)
    if os.listdir(signatures_dir):  # Checks if the directory is not empty
        print("The signatures directory is not empty. Not resigning files")
        return

    for file_path in critical_files():
        with open(file_path, 'rb') as f:
            # Sign the file
            signed_data = gpg.sign_file(f, keyid=email, detach=True)

            # Construct the path for the signature file within the specified directory
            base_name = os.path.basename(file_path)
            sig_path = os.path.join(signatures_dir, f"{base_name}.sig")

            # Save the signature to the .sig file in the specified directory
            with open(sig_path, 'wb') as sig_file:
                sig_file.write(str(signed_data).encode('utf-8'))


# 2. verify files
# ==========================


def sign_verification():

    flag = False

    log = open("dv1667.log", "a")

    for file_path in critical_files():
        base_name = os.path.basename(file_path)
        signature_path = os.path.join(signatures_dir, base_name + '.sig')

        with open(signature_path, 'rb') as sig_file:
            verification = gpg.verify_file(sig_file, file_path)

            if os.path.exists(file_path) == False:
                log.write(f"File does not exist {file_path} \n")

            if verification and verification.valid:
                log.write(f"Signature is valid for {file_path}\n")
            else:
                flag = True
                log.write(
                    f"Verification failed or signature not valid for {file_path}\n")

    log.close()
    if flag is True:
        return print("!!! FILE INTEGRITY COMPROMISED !!!" + "\n Check log file for details")
