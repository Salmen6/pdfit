from datetime import datetime
import os

def detect_language_from_extension(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    return {
        '.py': 'python',
        '.pyw': 'python',
        '.ipynb': 'python',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.cxx': 'cpp',
        '.h': 'c',
        '.hpp': 'cpp',
        '.html': 'html',
        '.htm': 'html',
        '.css': 'css',
        '.scss': 'scss',
        '.less': 'less',
        '.xml': 'xml',
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.md': '',
        '.txt': '',
        '.csv': '',
        '.sh': 'bash',
        '.bat': 'batch',
        '.ps1': 'powershell',
        '.sql': 'sql',
        '.rb': 'ruby',
        '.php': 'php',
        '.go': 'go',
        '.rs': 'rust',
        '.kt': 'kotlin',
        '.swift': 'swift',
        '.m': 'objectivec',
        '.ini': '',
        '.cfg': '',
        '.toml': '',
        '.dockerfile': 'dockerfile',
        '.makefile': 'makefile',
        '.gradle': 'groovy',
        '.bat': 'batch',
        
    }.get(ext, '')


def generate_md(projects_data, output_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    num_projects = len(projects_data)
    total_files = sum(len(project['files']) for project in projects_data)

    title = projects_data[0]['project_name'] if num_projects == 1 else "Combined Projects"

    with open(output_path, "w", encoding="utf-8") as f:
        # Header
        f.write(f"# {title}\n\n")
        f.write(f"**Generated on**: {timestamp}\n")
        f.write(f"**Total projects**: {num_projects}\n")
        f.write(f"**Total files**: {total_files}\n\n")
        f.write("---\n\n")

        # Table of Contents
        f.write("## Table of Contents\n\n")
        for project in projects_data:
            f.write(f"### Project: {project['project_name']}\n")
            for file in project['files']:
                anchor = file['path'].lower().replace(' ', '-').replace('/', '-').replace('\\', '-').replace('.', '-')
                f.write(f"- [{file['path']}](#{anchor})\n")
            f.write("\n")

        f.write("---\n\n")

        # File Contents
        for project in projects_data:
            f.write(f"## Project: {project['project_name']}\n\n")
            for file in project['files']:
                f.write(f"### File: {file['path']}\n\n")

                # Detect language
                language = detect_language_from_extension(file['path'])
                file_content = file['content']
                f.write(f"```{language}\n")
                f.write(file_content)
                f.write("\n```\n\n")
                f.write("---\n\n")
