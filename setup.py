from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks',
    description='Hooks for pre-commit',
    packages=find_packages('.'),
    install_requires=[],
    entry_points={
        'console_scripts': [],
    },
)
