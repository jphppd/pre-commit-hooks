#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

SCRIPTS = [
    'git-check-mailmap',
    'git-check-added-large-files',
    'git-check-merge-conflict',
    'git-commit-msg',
    'generic-check-byte-order-marker',
    'generic-check-case-conflict',
    'generic-check-executables-have-shebangs',
    'generic-check-symlinks',
    'generic-check-vcs-permalinks',
    'generic-detect-private-key',
    'generic-end-of-file-fixer',
    'generic-trailing-whitespace-fixer',
    'generic-crlf-forbid',
    'generic-crlf-remove',
    'generic-tabs-forbid',
    'generic-tabs-remove',
    'c-create-clang-format-cfg',
    'cmake-create-cmake-format-cfg',
    'html-validate',
    'html-detect-missing-css-classes',
    'html-attributes-blacklist',
    'html-forbid-img-without-alt-text',
    'html-forbid-non-std-attributes',
    'html-tags-blacklist',
    'json-check-syntax',
    'json-pretty-format',
    'python-check-ast',
    'python-check-builtin-literals',
    'python-check-docstring-first',
    'python-debug-statement-hook',
    'python-double-quote-string-fixer',
    'python-fix-encoding-pragma',
    'python-requirements-txt-fixer',
    'python-safety-checks',
    'python-isort-config',
    'python-pylint-config',
    'rst-linter',
    'toml-check-syntax',
    'xml-check-syntax',
    'yaml-check-syntax',
]

SCRIPTS_PATHS = ['python.{}:main'.format(script.replace('-', '_')) for script in SCRIPTS]

CONSOLE_SCRIPTS = ['{} = {}'.format(script, path) for script, path in zip(SCRIPTS, SCRIPTS_PATHS)]

setup(
    name='pre-commit-hooks',
    description='Hooks for pre-commit',
    package_dir={'': 'hooks'},
    packages=find_packages('hooks'),
    entry_points={'console_scripts': CONSOLE_SCRIPTS},
)
