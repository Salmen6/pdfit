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
- 🔗 **Git integration** - Only include Git-tracked files

## Requirements

- Linux or WSL (Windows Subsystem for Linux)
- Python 3.8+
- DejaVu fonts (usually pre-installed on Linux)
- Git (optional, for `--git` flag)

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

# Only Git-tracked files
pdfit . --git

# Include only specific extensions
pdfit . -e py js html

# Exclude additional directories
pdfit . --exclude dist build temp

# Exclude file extensions
pdfit . --exclude-ext log tmp

# Combine multiple projects with filters
pdfit ~/frontend ~/backend -e py js html -o fullstack

# Git-tracked files with extension filter
pdfit . --git -e py js
```

## Examples
```bash
# Python project with only .py files
pdfit ~/myproject -e py -o python_code

# Web project (HTML, CSS, JS)
pdfit ~/website -e html css js

# Exclude test directories
pdfit . --exclude tests __pycache__

# Only committed files (Git-tracked)
pdfit . --git -o clean_codebase

# Multiple repos, only Git-tracked Python files
pdfit ~/api ~/frontend --git -e py -o backend_code

# Combine multiple repositories for code review
pdfit ~/api ~/frontend ~/backend -o full_codebase

# Multiple microservices in one document
pdfit ~/service1 ~/service2 ~/service3 -e py -o microservices
```

## Git Integration

The `--git` flag enables Git-aware scanning:

### How it Works
- **Scans only Git-tracked files** - Ignores untracked and gitignored files
- **Clean output** - Only includes files committed or staged in Git
- **Automatic fallback** - If a directory isn't a Git repository, falls back to normal scanning with a warning

### Use Cases
- **Code reviews** - Only show committed code, not temporary files
- **Documentation** - Generate docs from production code only
- **Clean snapshots** - Exclude build artifacts, logs, and local config files
- **Multi-repo** - Works seamlessly with multiple repositories

### Example Workflow
```bash
# Your working directory has uncommitted experiments
pdfit . -o messy.pdf              # Includes everything

# Only committed code
pdfit . --git -o clean.pdf        # Only Git-tracked files

# Multiple repos, only committed Python code
pdfit ~/api ~/worker --git -e py
```

**Note**: Requires Git to be installed and the directory to be a Git repository. Non-Git directories will show a warning and use normal scanning.

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
- **Directories**: `node_modules`, `__pycache__`, `.git`, `.venv`, `venv`, `dist`, `build`, `.idea`, `.vscode`, `.pytest_cache`, `.mypy_cache`, `.npm`, `.gradle`, `.cache`
- **Files**: `.env`, `.DS_Store`, `package-lock.json`, `yarn.lock`, `.gitignore`, `.gitattributes`, `nohup.out`
- **Extensions**: `.pyc`, `.pyo`, `.class`, `.o`, `.exe`, `.dll`, `.so`, `.log`, `.tmp`, `.swp`, `.bak`, `.cache`, `.png`, `.jpg`, `.zip`, `.tar`, `.gz`, `.mp4`, `.mp3`, `.ttf`, `.pdf`

## Output Files

- Single directory: `<directory_name>.pdf`
- Multiple directories: `combined.pdf`
- Custom output: Use `-o filename` (`.pdf` extension added automatically)

## Command-Line Options

| Option | Description |
|--------|-------------|
| `paths` | One or more directories to convert (positional) |
| `-o`, `--output` | Custom output filename |
| `-e`, `--extensions` | Include only specific file extensions |
| `--exclude` | Exclude additional directories or files |
| `--exclude-ext` | Exclude specific file extensions |
| `--git` | Only include Git-tracked files |

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