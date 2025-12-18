def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                return file.read()
        except:
            return None
    except (FileNotFoundError, PermissionError):
        print(f"Cannot read file: {file_path}")
        return None
    except Exception:
        print(f"An unexpected error occurred while reading file: {file_path}")
        return None
