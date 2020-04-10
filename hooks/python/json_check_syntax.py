import argparse
import json
import sys
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, 'rb') as file_handler:
            try:
                json.load(file_handler)
            # TODO: need UnicodeDecodeError?
            except (ValueError, UnicodeDecodeError) as exc:
                print('{}: Failed to json decode ({})'.format(filename, exc))
                retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(main())
