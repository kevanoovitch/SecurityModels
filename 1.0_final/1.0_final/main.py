# ==============================================================================
# Author: Ludwig Sterner
# Email: luse23@student.bth.se
#
# Author: Kevin Deshayes
# Email: kede23@student.bth.se
# ==============================================================================

from modules.read_signatures import read_signatures
from modules.compare import compare
from modules.file_traversal import file_traversal
from modules.utils import utils
from modules.DigitalSign import sign_files, SignVerification


if __name__ == '__main__':
    db_path, file_path = utils()
    sign_files("kede23@student.bth.se")
    SignVerification()
    signatures = read_signatures(db_path)
    files = file_traversal(file_path)
    compare(files, signatures)
