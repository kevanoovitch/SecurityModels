from modules.read_signatures import read_signatures
from modules.compare import compare
from modules.file_traversal import file_traversal
from modules.utils import utils



db_path, file_path = utils()

signatures = read_signatures(db_path)
files = file_traversal(file_path)

print(signatures)

compare(files,signatures)