#!/usr/bin/env python3
"""
Check if any email address is associated with more than one name.

Example:
  John Doe <jdoe@example.com>
  jdoe <jdoe@example.com>

The above example can be fixed by adding these two lines to .mailmap file:
  John Doe <jdoe@example.com> John Doe <jdoe@example.com>
  John Doe <jdoe@example.com> jdoe <jdoe@example.com>
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  How we want it to appear    How it appears in git commit

See git-shortlog(1) for more details.
"""
from collections import defaultdict
from subprocess import check_output
import sys


def get_git_mail_map():
    """Construct mail mapping, as dict {email: [names]}."""
    separator = '::-::'
    mail_map = defaultdict(set)

    for line in check_output(
        ['git', 'log', '--use-mailmap', '--pretty=%aN{}%aE'.format(separator)],
        universal_newlines=True
    ).splitlines():
        if line:
            name, email = line.split(separator)
            email = email.lower()
            mail_map[email] |= {name}

    return mail_map


def main():
    """Run."""
    exit_val = 0
    for email, names in get_git_mail_map().items():
        if len(names) > 1:
            exit_val = 1
            print('The following email address is associated with more than one name:')
            print(email)
            print('- ' + '\n- '.join(sorted(names)) + '\n')
            print('Please create and fill .mailmap file.')
            print('See https://git-scm.com/docs/git-check-mailmap for details.')

    return exit_val


if __name__ == '__main__':
    sys.exit(main())
