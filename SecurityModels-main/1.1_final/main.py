# ==============================================================================
# Author: Ludwig Sterner
# Email: luse23@student.bth.se
#
# Author: Kevin Deshayes
# Email: kede23@student.bth.se
# ==============================================================================

from modules.utils import install_package

# Dependency check
install_package('python-gnupg')

if __name__ == '__main__':
    from modules.digital_sign import sign_files, sign_verification
    from modules.read_signatures import read_signatures
    from modules.compare import compare
    from modules.file_traversal import file_traversal
    from modules.utils import utils, install_package

    db_path, file_path = utils()
    sign_files("kede23@student.bth.se")
    sign_verification()
    signatures = read_signatures(db_path)
    files = file_traversal(file_path)
    compare(files, signatures)
