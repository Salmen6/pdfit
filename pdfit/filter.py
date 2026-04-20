from pathlib import Path   

def should_include_file(file_path, config):
    path_obj = Path(file_path)
    
    # Check if any part of the path (e.g., 'node_modules') is in excluded_dirs
    for part in path_obj.parts:
        if part in config['excluded_dirs']:
            return False
            
    # Check if the specific filename is excluded 
    if path_obj.name in config['excluded_files']:
        return False

    # Check if extension is excluded 
    if path_obj.suffix in config['excluded_extensions']:
        return False

    # Check if specific extensions are whitelisted
    if config['included_extensions']:
        # Ensure we check the extension without the leading dot
        if path_obj.suffix.lstrip('.') not in config['included_extensions']:
            return False

    return True