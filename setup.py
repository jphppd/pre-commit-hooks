#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

scripts = [
    'git-check-mailmap',
    'git-check-added-large-files',
    'git-check-merge-conflict',
    'generic-check-byte-order-marker',
    'generic-check-case-conflict',
    'generic-check-executables-have-shebangs',
    'generic-check-symlinks',
    'generic-check-vcs-permalinks',
    'generic-detect-private-key',
    'generic-end-of-file-fixer',
    'generic-trailing-whitespace-fixer',
    'json-check-syntax',
    'json-pretty-format',
    'python-check-ast',
    'python-check-builtin-literals',
    'python-check-docstring-first',
    'python-debug-statement-hook',
    'python-double-quote-string-fixer',
    'python-fix-encoding-pragma',
    'python-requirements-txt-fixer',
    'toml-check-syntax',
    'xml-check-syntax',
    'yaml-check-syntax',
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
