from setuptools import setup, find_packages

# Read README for long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pdfit',
    version='1.0.0',
    description='Convert code projects to PDF documents',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Salmen Makki',  
    author_email='salmenmakki.dev@gmail.com', 
    url='https://github.com/salmen6/pdfit', 
    license='MIT',
    license_files=('LICENSE',),
    packages=find_packages(),
    install_requires=[
        'fpdf2>=2.7.0',
    ],
    entry_points={
        'console_scripts': [
            'pdfit=pdfit.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.8',
    keywords='pdf code converter cli documentation',
    project_urls={
        'Bug Reports': 'https://github.com/Salmen6/pdfit/issues',
        'Source': 'https://github.com/Salmen6/pdfit',
    },
)
