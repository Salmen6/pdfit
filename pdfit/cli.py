import argparse
import os
import sys
import subprocess
import questionary
import time
from pdfit.scanner import scan_directory
from pdfit.filter import should_include_file
from pdfit.reader import read_file
from pdfit.pdf import generate_pdf
from pdfit.markdown import generate_md

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Convert code project to PDF or Markdown',
        prog='pdfit'
    )
    
    parser.add_argument(
        'paths',
        nargs='+',
        default='.',
        help='Convert one Directory or multiple into one Document'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output filename'
    )
    
    parser.add_argument(
        '-e', '--extensions',
        nargs='*',
        help='File extensions to include (e.g., py js html)'
    )
    
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Interactively choose which files to include'
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
        help='Convert files to a markdown file'
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
    
    return result.stdout.strip().split('\n')

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
    
    for path in args.paths:
        if not os.path.exists(path):
            print(f"Error: Path {os.path.abspath(path)} does not exist")
            sys.exit(1)
    
    abs_paths = [os.path.abspath(p) for p in args.paths]
    
    # Determine output filename
    if args.output:
        output_filename = args.output
    else:
        output_filename = os.path.basename(abs_paths[0]) if len(abs_paths) == 1 else 'combined'
    
    output_filename += '.md' if args.md else '.pdf'
    
    config = {
        'excluded_dirs': ['__pycache__', 'node_modules', 'venv', '.venv', '.git', 'dist', 'build', 'target'],
        'excluded_files': ['.env', '.DS_Store', 'package-lock.json', 'yarn.lock', '.gitignore'],
        'excluded_extensions': ['.pyc', '.exe', '.dll', '.log', '.png', '.jpg', '.pdf'],
        'included_extensions': args.extensions or []
    }
    
    if args.exclude: config['excluded_dirs'].extend(args.exclude)
    if args.exclude_ext: config['excluded_extensions'].extend(args.exclude_ext)
    
    projects_data = []
    stats = {'files_count': 0, 'total_lines': 0}
    
    for path in args.paths:
        project_name = os.path.basename(os.path.abspath(path))
        candidates = []
        
        # 1. Scan for candidates
        if args.git:
            files_to_scan = get_git_files(path) or list(scan_directory(path))
        else:
            files_to_scan = list(scan_directory(path))
        
        for f in files_to_scan:
            if should_include_file(f, config):
                candidates.append(f)

        # 2. Interactive Selection
        if args.interactive and candidates:
            print(f"\n[Tip] Use the Arrow Keys to navigate, SPACE to check/uncheck, and ENTER to confirm.")
            print(f"Loading files for '{project_name}'...")
            
            time.sleep(2)
            selected_files = questionary.checkbox(
                f"Select files for project '{project_name}':",
                choices=[questionary.Choice(c, checked=True) for c in candidates]
            ).ask()
            if selected_files is None: return 0 # User cancelled
        else:
            selected_files = candidates

        # 3. Process Selection
        project_files = []
        for file_rel_path in selected_files:
            full_path = os.path.join(path, file_rel_path)
            content = read_file(full_path)
            if content is not None:
                project_files.append({'path': file_rel_path, 'content': content})
                stats['files_count'] += 1
                stats['total_lines'] += len(content.splitlines())
                print(f"  ✓ Added: {file_rel_path}")
        
        projects_data.append({'project_name': project_name, 'files': project_files})
    
    if not projects_data[0]['files']:
        print("No files selected. Exiting.")
        return 0

    if args.md:
        generate_md(projects_data, output_filename)
    else:
        generate_pdf(projects_data, output_filename)
        
    display_summary(stats, projects_data, output_filename)
    return 0

if __name__ == "__main__":
    sys.exit(main())