from pathlib import Path
import sys

CONFIG_PATH = Path('.isort.cfg')
DEFAULT_CONTENT = \
r'''[settings]
multi_line_output = 3
include_trailing_comma = True
force_grid_wrap = 0
use_parentheses = True
line_length = 99
'''


def main():
    if not CONFIG_PATH.exists():
        with CONFIG_PATH.open('w') as cfg_fh:
            cfg_fh.write(DEFAULT_CONTENT)
        print(f'{CONFIG_PATH} was created with a default configuration.')
        print('Please add it to your commit.')
        return 1


if __name__ == '__main__':
    sys.exit(main())
