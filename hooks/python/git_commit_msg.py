#!/usr/bin/env python3
# pylint: disable=invalid-name
"""
An example hook script to check the commit log message.
Called by "git commit" with one argument, the name of the file
that has the commit message.  The hook should exit with non-zero
status after issuing an appropriate message if it wants to stop the
commit.  The hook is allowed to edit the commit message file.
"""

from pathlib import Path
import re
import sys

COMMIT_RE = re.compile(r'\[\+?\*?-?~?\^?\]')


def main():
    """Inspect the commit message."""

    with Path(sys.argv[1]).open() as commit_msg_fh:
        commit_msg = commit_msg_fh.read().strip()

    if bool(COMMIT_RE.match(commit_msg)):
        return 0

    print(
        '[commit-msg hook] Please make sure your commit message matches the regex: ^{}$'.
        format(COMMIT_RE)
    )
    print('[commit-msg hook] Message: \'{}\''.format(commit_msg))
    return 1


if __name__ == '__main__':
    sys.exit(main())
