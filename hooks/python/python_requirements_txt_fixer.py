import argparse
import sys
from typing import IO
from typing import List
from typing import Optional
from typing import Sequence

PASS = 0
FAIL = 1


class Requirement:
    def __init__(self) -> None:
        self.value: Optional[bytes] = None
        self.comments: List[bytes] = []

    @property
    def name(self) -> bytes:
        if self.value is None:
            raise RuntimeError(self.value)
        for egg in (b'#egg=', b'&egg='):
            if egg in self.value:  # pylint: disable=unsupported-membership-test
                return self.value.lower().partition(egg)[-1]

        return self.value.lower().partition(b'==')[0]

    def __lt__(self, requirement: 'Requirement') -> int:
        # \n means top of file comment, so always return True,
        # otherwise just do a string comparison with value.
        if self.value is None:
            raise RuntimeError(self.value)
        if self.value == b'\n':
            return True
        if requirement.value == b'\n':
            return False
        return self.name < requirement.name


def fix_requirements(file: IO[bytes]) -> int:  # pylint: disable=too-many-branches
    requirements: List[Requirement] = []
    before = list(file)
    after: List[bytes] = []

    before_string = b''.join(before)

    # adds new line in case one is missing
    # AND a change to the requirements file is needed regardless:
    if before and not before[-1].endswith(b'\n'):
        before[-1] += b'\n'

    # If the file is empty (i.e. only whitespace/newlines) exit early
    if before_string.strip() == b'':
        return PASS

    for line in before:
        # If the most recent requirement object has a value, then it's
        # time to start building the next requirement object.

        if not requirements or requirements[-1].value is not None:
            requirements.append(Requirement())

        requirement = requirements[-1]

        # If we see a newline before any requirements, then this is a
        # top of file comment.
        if len(requirements) == 1 and line.strip() == b'':
            if (requirement.comments and requirement.comments[0].startswith(b'#')):
                requirement.value = b'\n'
            else:
                requirement.comments.append(line)
        elif line.startswith(b'#') or line.strip() == b'':
            requirement.comments.append(line)
        else:
            requirement.value = line

    # if a file ends in a comment, preserve it at the end
    if requirements[-1].value is None:
        rest = requirements.pop().comments
    else:
        rest = []

    # find and remove pkg-resources==0.0.0
    # which is automatically added by broken pip package under Debian
    requirements = [req for req in requirements if req.value != b'pkg-resources==0.0.0\n']

    for requirement in sorted(requirements):
        after.extend(requirement.comments)
        if not requirement.value:
            raise RuntimeError(requirement.value)
        after.append(requirement.value)
    after.extend(rest)

    after_string = b''.join(after)

    if before_string == after_string:
        return PASS
    file.seek(0)
    file.write(after_string)
    file.truncate()
    return FAIL


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = PASS

    for arg in args.filenames:
        with open(arg, 'rb+') as file_obj:
            ret_for_file = fix_requirements(file_obj)

            if ret_for_file:
                print(f'Sorting {arg}')

            retv |= ret_for_file

    return retv


if __name__ == '__main__':
    sys.exit(main())
