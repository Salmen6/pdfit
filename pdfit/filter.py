
from pathlib import Path   

def should_include_file(root_path,config):
    path_obj = Path(root_path)
    
    file_name = path_obj.name
    file_extension = path_obj.suffix
    #parent_directory = str(Path(root_path))
    #Check if file is in excluded directory → return False
    for dir in path_obj.parts:
        if dir in config['excluded_dirs']:
            return False
    #Check if the filename is excluded 
    if file_name in config['excluded_files']:
        return False

    # check if extension is excluded 
    if file_extension in config['excluded_extensions']:
        return False

    #check if file extensions are included 

    if config['included_extensions']:
        if file_extension.lstrip('.') not in config['included_extensions']:
            return False

    return True
