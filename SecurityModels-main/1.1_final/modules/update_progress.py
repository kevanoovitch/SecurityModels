import sys

def update_progress(allFiles, checkedFiles):
    total_files = len(allFiles)
    files_checked = len(checkedFiles)

    if total_files == 0:
        print("No files to check.")
        return

    percentage_checked = (files_checked / total_files) * 100
    bar_length = 50
    filled_length = int(bar_length * files_checked // total_files)
    bar = '*' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\rProgress: [{bar}] {percentage_checked:.2f}% Complete')  # Using sys.stdout.write for compatibility
    sys.stdout.flush()

    if files_checked == total_files:
        sys.stdout.write('\n')
        sys.stdout.flush()
