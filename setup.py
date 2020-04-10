#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

scripts = [
    'check-added-large-files',
    'check-ast',
    'check-builtin-literals',
    'check-byte-order-marker',
    'check-docstring-first',
    'check-case-conflict',
    'check-executables-have-shebangs',
    'check-json',
    'check-mailmap',
    'check-merge-conflict',
    'check-symlinks',
    'check-toml',
    'check-vcs-permalinks',
    'check-xml',
    'check-yaml',
    'detect-private-key',
    'debug-statement-hook',
    'double-quote-string-fixer',
    'end-of-file-fixer',
    'fix-encoding-pragma',
    'mixed-line-ending',
    'pretty-format-json',
    'trailing-whitespace-fixer',
]

scripts_paths = [
    'pre_commit_hooks_python.{}:main'.format(script.replace('-', '_')) for script in scripts
]

console_scripts = ['{} = {}'.format(script, path) for script, path in zip(scripts, scripts_paths)]

setup(
    name='pre-commit-hooks',
    description='Hooks for pre-commit',
    packages=find_packages('.'),
    entry_points={'console_scripts': console_scripts},
    install_requires=[
        'ruamel.yaml'
    ]
)
