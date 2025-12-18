# pdfit

Convert your code projects into clean, shareable documents — PDF or Markdown.

## Features

- 🔍 Recursively scans project directories
- 🎯 Smart filtering (exclude node_modules, .git, etc.)
- 📄 **Dual format support** - Generate PDF or Markdown
- 📝 Preserves code formatting with syntax highlighting
- 🌍 Full Unicode support (emojis, special characters)
- ⚙️ Configurable via command-line options
- 📚 **Multi-repository support** - Combine multiple projects into one document
- 📑 **Table of contents** - Auto-generated file listing per project
- 🔗 **Git integration** - Only include Git-tracked files

## Output Formats

### PDF (Default)
**Best for**: Presentations, portfolios, printing, sharing with humans

- Professional formatting with monospace fonts
- Print-ready documents
- Portable and consistent rendering
- Requires DejaVu fonts (pre-installed on most Linux systems)

### Markdown (with `--md` flag)
**Best for**: AI code review, ChatGPT/Claude, quick sharing, version control

- Native syntax highlighting
- Lightweight and searchable
- Easy copy-paste to AI tools
- Git-friendly (text-based, diffable)
- No font dependencies

## Requirements

- Linux or WSL (Windows Subsystem for Linux)
- Python 3.8+
- DejaVu fonts (for PDF output, usually pre-installed on Linux)
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
# Convert to PDF (default)
pdfit .

# Convert to Markdown
pdfit . --md

# Specify output filename
pdfit /path/to/project -o myproject        # Creates myproject.pdf
pdfit /path/to/project -o mycode --md      # Creates mycode.md

# Multiple projects
pdfit /path/to/project1 /path/to/project2

# Only Git-tracked files
pdfit . --git

# Include only specific extensions
pdfit . -e py js html

# Exclude directories
pdfit . --exclude dist build temp

# Exclude file extensions
pdfit . --exclude-ext log tmp

# Combine multiple features
pdfit ~/frontend ~/backend --git -e py js --md -o fullstack
```

## Examples

### PDF Output
```bash
# Python project documentation
pdfit ~/myproject -e py -o python_docs

# Web project with HTML, CSS, JS
pdfit ~/website -e html css js

# Professional portfolio
pdfit ~/portfolio --git -o showcase
```

### Markdown Output (For AI Review)
```bash
# Send to ChatGPT/Claude for review
pdfit . --md -o codebase
# Upload codebase.md to AI tool

# Only committed Python code for AI analysis
pdfit . --git -e py --md -o review

# Multi-repo codebase for AI
pdfit ~/api ~/frontend ~/backend --md -o full_project

# Quick code snapshot for sharing
pdfit . --git --md -o current_state
```

### Advanced Usage
```bash
# Exclude test directories
pdfit . --exclude tests __pycache__

# Only committed files (clean output)
pdfit . --git -o clean_codebase

# Multiple repos, only Git-tracked Python files
pdfit ~/api ~/frontend --git -e py --md

# Microservices documentation
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
- **AI analysis** - Send only production code to AI tools

### Example Workflow
```bash
# Your working directory has uncommitted experiments
pdfit .              # Includes everything

# Only committed code
pdfit . --git        # Only Git-tracked files

# For AI review: committed code as markdown
pdfit . --git --md -o review
```

**Note**: Requires Git to be installed and the directory to be a Git repository. Non-Git directories will show a warning and use normal scanning.

## Multi-Repository Support

When processing multiple projects, pdfit creates well-organized documents with:
- **Project headers** - Clear visual separation between projects
- **Table of contents** - List of all files per project  
- **Grouped content** - All files from each project together

Perfect for:
- Code reviews across multiple repos
- Documentation of related projects
- AI-assisted analysis of multi-repo codebases
- Portfolio presentations
- Microservices documentation

## Default Exclusions

The tool automatically excludes:
- **Directories**: `node_modules`, `__pycache__`, `.git`, `.venv`, `venv`, `dist`, `build`, `.idea`, `.vscode`, `.pytest_cache`, `.mypy_cache`, `.npm`, `.gradle`, `.cache`
- **Files**: `.env`, `.DS_Store`, `package-lock.json`, `yarn.lock`, `.gitignore`, `.gitattributes`, `nohup.out`
- **Extensions**: `.pyc`, `.pyo`, `.class`, `.o`, `.exe`, `.dll`, `.so`, `.log`, `.tmp`, `.swp`, `.bak`, `.cache`, `.png`, `.jpg`, `.zip`, `.tar`, `.gz`, `.mp4`, `.mp3`, `.ttf`, `.pdf`

## Output Files

### PDF Format (Default)
- Single directory: `<directory_name>.pdf`
- Multiple directories: `combined.pdf`
- Custom: `-o filename` creates `filename.pdf`

### Markdown Format (with `--md`)
- Single directory: `<directory_name>.md`
- Multiple directories: `combined.md`
- Custom: `-o filename --md` creates `filename.md`

## Command-Line Options

| Option | Description |
|--------|-------------|
| `paths` | One or more directories to convert (positional) |
| `-o`, `--output` | Custom output filename (extension added automatically) |
| `-e`, `--extensions` | Include only specific file extensions |
| `--exclude` | Exclude additional directories or files |
| `--exclude-ext` | Exclude specific file extensions |
| `--git` | Only include Git-tracked files |
| `--md` | Generate Markdown instead of PDF |

## Use Case Guide

**Choose PDF when**:
- Presenting to stakeholders or clients
- Creating portfolio documentation
- Printing physical copies
- Formal code reviews

**Choose Markdown when**:
- Sending code to AI tools (ChatGPT, Claude, etc.)
- Quick code sharing with developers
- Version controlling documentation
- Lightweight file size needed

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