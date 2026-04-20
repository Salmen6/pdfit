from pathlib import Path

def scan_directory(root_path):
    path_obj = Path(root_path)
    # rglob('*') returns a generator of all files and folders recursively
    for file_path in path_obj.rglob('*'):
        if file_path.is_file():
            try:
                # Provide relative paths to make the UI and PDF/MD output cleaner
                yield str(file_path.relative_to(path_obj))
            except ValueError:
                yield str(file_path)