# pdfit

Convert your code projects into clean, readable PDF documents.

## Features

- 🔍 Recursively scans project directories
- 🎯 Smart filtering (exclude node_modules, .git, etc.)
- 📝 Preserves code formatting with monospace fonts
- 🌍 Full Unicode support (emojis, special characters)
- ⚙️ Configurable via command-line options

## Requirements

- Linux or WSL (Windows Subsystem for Linux)
- Python 3.8+
- DejaVu fonts (usually pre-installed on Linux)

## Installation
```bash
pip install pdfit
```

## Usage
```bash
# Convert current directory
pdfit

# Specify a directory
pdfit /path/to/project

# Custom output filename
pdfit /path/to/project -o myproject.pdf

# Include only specific extensions
pdfit . -e py js html

# Exclude additional directories
pdfit . --exclude dist build temp

# Exclude file extensions
pdfit . --exclude-ext log tmp
```

## Examples
```bash
# Python project with only .py files
pdfit ~/myproject -e py -o python_code.pdf

# Web project (HTML, CSS, JS)
pdfit ~/website -e html css js

# Exclude test directories
pdfit . --exclude tests __pycache__
```

## Default Exclusions

The tool automatically excludes:
- **Directories**: `node_modules`, `__pycache__`, `.git`, `.venv`, `venv`, `dist`, `build`
- **Files**: `.env`, `.DS_Store`, `package-lock.json`, `yarn.lock`
- **Extensions**: `.pyc`, `.log`, `.tmp`, `.exe`, `.dll`

## License

MIT License - See LICENSE file for details

## Contributing

Issues and pull requests welcome!

## Note

Currently supports Linux/WSL only. Windows support is planned for future releases.
