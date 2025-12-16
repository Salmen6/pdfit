from pathlib import Path


def scan_directory(root_path):
    path_obj = Path(root_path) #it transforms root_path to a path
    path_obj.rglob('*') #rglob('*') returns all items recursively
    for file_path in path_obj.rglob('*'):
        if file_path.is_file():
            yield str(file_path)
