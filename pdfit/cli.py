import argparse
import os
import sys
from pdfit.scanner import scan_directory
from pdfit.filter import should_include_file
from pdfit.reader import read_file
from pdfit.pdf import generate_pdf


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Convert code project to PDF',
        prog='pdfit'
    )
    
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Project directory to convert'
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
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # Print for testing
#    print(f"Path: {args.path}")
#    print(f"Output: {args.output}")
#    print(f"Extensions: {args.extensions}")
#    print(f"Exclude: {args.exclude}")
#    print(f"Exclude-ext: {args.exclude_ext}")


    path = args.path
    if os.path.exists(path) and not os.path.isdir(path):
        print(f"path {path}  exists but it's not a folder")
        sys.exit(1)
    elif not os.path.exists(path):
        print(f"path {path} does not exist")
        sys.exit(1)
    elif os.path.isdir(path):
        print(f"path {path} exits and it's a folder")

    abs_path = os.path.abspath(path)
    current_directory = os.path.basename(abs_path)


    if args.output is None:
        output_filename= current_directory + '.pdf'
    else:
        output_filename = args.output + '.pdf'
    print(output_filename)

    config = {
    'excluded_dirs': [
        '__pycache__','node_modules','venv','.venv','env',
        '.git','.hg','.svn',
        '.idea','.vscode','.settings',
        'dist','build','out','.output','target',
        '.pytest_cache','.mypy_cache','.ruff_cache',
        '.npm','.yarn','.pnpm-store',
        '.gradle','.tox','.cache','.coverage',
        '__MACOSX','.metadata'
    ],
    'excluded_files': [
        '.env','.env.local','.env.development','.env.production',
        '.DS_Store','Thumbs.db',
        '.npmrc','.yarnrc','.editorconfig',
        'package-lock.json','yarn.lock','pnpm-lock.yaml',
        'poetry.lock','Pipfile.lock','composer.lock',
        '.gitignore','.gitattributes','.gitmodules',
        'nohup.out'
    ],
    'excluded_extensions': [
        '.pyc','.pyo','.class','.o','.a',
        '.exe','.dll','.so','.dylib',
        '.zip','.tar','.gz','.bz2','.7z','.rar',
        '.log','.tmp','.swp','.bak','.cache',
        '.png','.jpg','.jpeg','.gif','.bmp','.svg','.ico','.webp',
        '.mp4','.mov','.avi','.mkv',
        '.mp3','.wav','.ogg',
        '.ttf','.otf','.woff','.woff2',
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

    # for file_path in scan_directory(path):
    #     print(file_path)


    # print("\nFiltered files:")
    # for file_path in scan_directory(path):
    #     if should_include_file(file_path, config):
    #         print(f"  ✓ Include: {file_path}")
        
    # print("\nReading files:")
    # for file_path in scan_directory(path):
    #     if should_include_file(file_path, config):
    #         content = read_file(file_path)
    #         if content is not None:
    #             print(f"  ✓ Read: {file_path} ({len(content)} chars)")
    #         else:
    #             print(f"  ✗ Failed to read: {file_path}")

    print("\nCollecting files...")
    files_data = []
    for file_path in scan_directory(path):
        if should_include_file(file_path, config):
            content = read_file(file_path)
            if content is not None:
                files_data.append({
                    'path': file_path,
                    'content': content
                })
                print(f"  ✓ Added: {file_path}")

    print(f"\nGenerating PDF: {output_filename}")
    generate_pdf(files_data, output_filename)
    print(f"✓ PDF created successfully: {output_filename}")

    return 0
