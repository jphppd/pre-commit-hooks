import argparse
import re
import sys
from typing import Optional
from typing import Sequence

GITHUB_NON_PERMALINK = re.compile(br'https://github.com/[^/ ]+/[^/ ]+/blob/master/[^# ]+#L\d+', )


def _check_filename(filename: str) -> int:
    retv = 0
    with open(filename, 'rb') as f:
        for i, line in enumerate(f, 1):
            if GITHUB_NON_PERMALINK.search(line):
                sys.stdout.write(f'{filename}:{i}:')
                sys.stdout.flush()
                sys.stdout.buffer.write(line)
                retv = 1
    return retv


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        retv |= _check_filename(filename)

    if retv:
        print()
        print('Non-permanent github link detected.')
        print('On any page on github press [y] to load a permalink.')
    return retv


if __name__ == '__main__':
    exit(main())
