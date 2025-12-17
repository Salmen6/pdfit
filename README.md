# pdfit

Convert your code projects into clean, readable PDF documents.

## Features

- 🔍 Recursively scans project directories
- 🎯 Smart filtering (exclude node_modules, .git, etc.)
- 📝 Preserves code formatting with monospace fonts
- 🌍 Full Unicode support (emojis, special characters)
- ⚙️ Configurable via command-line options
- 📚 **Multi-repository support** - Combine multiple projects into one PDF
- 📑 **Table of contents** - Auto-generated file listing per project

## Requirements

- Linux or WSL (Windows Subsystem for Linux)
- Python 3.8+
- DejaVu fonts (usually pre-installed on Linux)

## Installation

### From Source
```bash
git clone https://github.com/Salmen6/pdfit.git
cd pdfit
pip install . --break-system-packages
```

### From PyPI (Coming Soon)
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
pdfit /path/to/project -o myproject

# Multiple projects (creates combined PDF)
pdfit /path/to/project1 /path/to/project2

# Include only specific extensions
pdfit . -e py js html

# Exclude additional directories
pdfit . --exclude dist build temp

# Exclude file extensions
pdfit . --exclude-ext log tmp

# Combine multiple projects with filters
pdfit ~/frontend ~/backend -e py js html -o fullstack
```

## Examples
```bash
# Python project with only .py files
pdfit ~/myproject -e py -o python_code

# Web project (HTML, CSS, JS)
pdfit ~/website -e html css js

# Exclude test directories
pdfit . --exclude tests __pycache__

# Combine multiple repositories for code review
pdfit ~/api ~/frontend ~/backend -o full_codebase

# Multiple microservices in one document
pdfit ~/service1 ~/service2 ~/service3 -e py -o microservices
```

## Multi-Repository Support

When processing multiple projects, pdfit creates a well-organized PDF with:
- **Project headers** - Clear visual separation between projects
- **Table of contents** - List of all files per project
- **Grouped content** - All files from each project together

Perfect for:
- Code reviews across multiple repos
- Documentation of related projects
- AI-assisted analysis of multi-repo codebases
- Portfolio presentations

## Default Exclusions

The tool automatically excludes:
- **Directories**: `node_modules`, `__pycache__`, `.git`, `.venv`, `venv`, `dist`, `build`, `.idea`, `.vscode`
- **Files**: `.env`, `.DS_Store`, `package-lock.json`, `yarn.lock`, `.npmrc`, `.yarnrc`, `Thumbs.db`
- **Extensions**: `.pyc`, `.pyo`, `.class`, `.o`, `.exe`, `.dll`, `.so`, `.log`, `.tmp`, `.swp`, `.bak`

## Output Files

- Single directory: `<directory_name>.pdf`
- Multiple directories: `combined.pdf`
- Custom output: Use `-o filename` (`.pdf` extension added automatically)

## License

MIT License - See LICENSE file for details

## Contributing

Issues and pull requests welcome!

## Author

**Salmen Makki**
- GitHub: [@Salmen6](https://github.com/Salmen6)
- Email: salmenmakki.dev@gmail.com

## Note

Currently supports Linux/WSL only. Windows support is planned for future releases.
