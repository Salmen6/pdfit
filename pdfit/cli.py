import argparse
import os
import sys
from pdfit.scanner import scan_directory
from pdfit.filter import should_include_file
from pdfit.reader import read_file
from pdfit.pdf import generate_pdf
from pdfit.markdown import generate_md
import subprocess


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Convert code project to PDF',
        prog='pdfit'
    )
    
    parser.add_argument(
        'paths',
        nargs='+',
        default='.',
        help='Convert one Directory or multiple into one Pdf Document'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output PDF filename'
    )
    
    parser.add_argument(
        '-e', '--extensions',
        nargs='*',
        help='File extensions to include (e.g., py js html)'
    )
    
    parser.add_argument(
        '--exclude',
        nargs='*',
        help='Directories or files to exclude'
    )
    
    parser.add_argument(
        '--exclude-ext',
        nargs='*',
        help='File extensions to exclude'
    )
    
    parser.add_argument(
        '--git',
        action='store_true',
        help='Convert only the files tracked by Git'
    )
    
    parser.add_argument(
        '--md',
        action='store_true',
        help='convert files to a markdown file'
    )
    
    return parser.parse_args()


def get_git_files(project_path):
    result = subprocess.run(
        ['git', 'ls-files'],
        cwd=project_path,
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        return None
    
    relative_files = result.stdout.strip().split('\n')
    
    absolute_files = []
    for rel_file in relative_files:
        abs_file = os.path.join(project_path, rel_file)
        absolute_files.append(abs_file)
    
    return absolute_files


def format_file_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        kb = size_bytes / 1024
        return f"{kb:.1f} KB"
    else:
        mb = size_bytes / (1024 * 1024)
        return f"{mb:.1f} MB"


def display_summary(stats, projects_data, output_filename):
    file_size = os.path.getsize(output_filename)
    
    print("\nSummary:")
    print(f"  Projects processed: {len(projects_data)}")
    print(f"  Files included: {stats['files_count']}")
    print(f"  Total lines of code: {stats['total_lines']:,}")
    print(f"  Output size: {format_file_size(file_size)}")


def main():
    args = parse_arguments()
    
    paths = args.paths
    for path in paths:
        if os.path.exists(path) and not os.path.isdir(path):
            print(f"path {os.path.abspath(path)} exists but it's not a folder")
            sys.exit(1)
        elif not os.path.exists(path):
            print(f"path {os.path.abspath(path)} does not exist")
            sys.exit(1)
        elif os.path.isdir(path):
            print(f"path {os.path.abspath(path)} exits and it's a folder")
    
    abs_paths = [os.path.abspath(p) for p in paths]
    current_directories = [os.path.basename(absp) for absp in abs_paths]
    
    if args.output is not None:
        output_filename = args.output
    else:
        if len(paths) == 1:
            output_filename = current_directories[0]
        else:
            output_filename = 'combined'
    
    if not args.md:
        output_filename += '.pdf'
    else:
        output_filename += '.md'
    
    config = {
        'excluded_dirs': [
            '__pycache__', 'node_modules', 'venv', '.venv', 'env',
            '.git', '.hg', '.svn',
            '.idea', '.vscode', '.settings',
            'dist', 'build', 'out', '.output', 'target',
            '.pytest_cache', '.mypy_cache', '.ruff_cache',
            '.npm', '.yarn', '.pnpm-store',
            '.gradle', '.tox', '.cache', '.coverage',
            '__MACOSX', '.metadata'
        ],
        'excluded_files': [
            '.env', '.env.local', '.env.development', '.env.production',
            '.DS_Store', 'Thumbs.db',
            '.npmrc', '.yarnrc', '.editorconfig',
            'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml',
            'poetry.lock', 'Pipfile.lock', 'composer.lock',
            '.gitignore', '.gitattributes', '.gitmodules',
            'nohup.out'
        ],
        'excluded_extensions': [
            '.pyc', '.pyo', '.class', '.o', '.a',
            '.exe', '.dll', '.so', '.dylib',
            '.zip', '.tar', '.gz', '.bz2', '.7z', '.rar',
            '.log', '.tmp', '.swp', '.bak', '.cache',
            '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico', '.webp',
            '.mp4', '.mov', '.avi', '.mkv',
            '.mp3', '.wav', '.ogg',
            '.ttf', '.otf', '.woff', '.woff2',
            '.pdf'
        ],
        'included_extensions': []
    }
    
    user_excludes = args.exclude or []
    config['excluded_dirs'].extend(user_excludes)
    user_excludes_ext = args.exclude_ext or []
    config['excluded_extensions'].extend(user_excludes_ext)
    user_includes = args.extensions or []
    config['included_extensions'].extend(user_includes)
    
    print("\nCollecting files...")
    projects_data = []
    stats = {'files_count': 0, 'total_lines': 0}
    
    for path in paths:
        project_name = os.path.basename(os.path.abspath(path))
        project_files = []
        
        if args.git:
            files_to_scan = get_git_files(path)
            if files_to_scan is None:
                print(f"Warning: {path} is not a git repository, scanning all files")
                files_to_scan = scan_directory(path)
        else:
            files_to_scan = scan_directory(path)
        
        for file_path in files_to_scan:
            if should_include_file(file_path, config):
                content = read_file(file_path)
                if content is not None:
                    project_files.append({
                        'path': file_path,
                        'content': content
                    })
                    
                    
                    stats['files_count'] += 1
                    stats['total_lines'] += len(content.splitlines())
                    
                    print(f"  ✓ Added: {file_path}")
        
        projects_data.append({
            'project_name': project_name,
            'files': project_files
        })
    
    if not args.md:
        print(f"\nGenerating PDF: {output_filename}")
        generate_pdf(projects_data, output_filename)
        print(f"✓ PDF created successfully: {output_filename}")
    else:
        print(f"\nGenerating Markdown: {output_filename}")
        generate_md(projects_data, output_filename)
        print(f"✓ Markdown created successfully: {output_filename}")
    
    display_summary(stats, projects_data, output_filename)
    
    return 0
