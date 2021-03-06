import argparse
import json
import math
import os
import sys
from typing import Optional
from typing import Sequence
from typing import Set

from python.util import added_files
from python.util import CalledProcessError
from python.util import cmd_output


def lfs_files() -> Set[str]:
    try:
        # Introduced in git-lfs 2.2.0, first working in 2.2.1
        lfs_ret = cmd_output('git', 'lfs', 'status', '--json')
    except CalledProcessError:  # pragma: no cover (with git-lfs)
        lfs_ret = '{"files":{}}'

    return set(json.loads(lfs_ret)['files'])


def find_large_added_files(filenames: Sequence[str], maxkb: int) -> int:
    # Find all added files that are also in the list of files pre-commit tells
    # us about
    retv = 0
    for filename in (added_files() & set(filenames)) - lfs_files():
        kbytes = int(math.ceil(os.stat(filename).st_size / 1024))
        if kbytes > maxkb:
            print('{} ({} KB) exceeds {} KB.'.format(filename, kbytes, maxkb))
            retv = 1

    return retv


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--maxkb',
        type=int,
        default=500,
        help='Maxmimum allowable KB for added files',
    )

    args = parser.parse_args(argv)
    return find_large_added_files(args.filenames, args.maxkb)


if __name__ == '__main__':
    sys.exit(main())
