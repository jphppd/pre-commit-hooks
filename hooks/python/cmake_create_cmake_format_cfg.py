from pathlib import Path
import sys

CONFIG_PATH = Path('.cmake-format.yaml')
DEFAULT_CONTENT = \
r'''---

format:
  _help_max_lines_hwrap:
    - If a candidate layout is wrapped horizontally but it exceeds
    - this many lines, then reject the layout.
  max_lines_hwrap: 2
  _help_keyword_case:
    - Format keywords consistently as 'lower' or 'upper' case
  keyword_case: uppet
  _help_max_subgroups_hwrap:
    - If an argument group contains more than this many sub-groups
    - (parg or kwarg groups) then force it to a vertical layout.
  max_subgroups_hwrap: 2
  _help_max_pargs_hwrap:
    - If a positional argument group contains more than this many
    - arguments, then force it to a vertical layout.
  max_pargs_hwrap: 2
'''

def main():
    if not CONFIG_PATH.exists():
        with CONFIG_PATH.open('w') as cfg_fh:
            cfg_fh.write(DEFAULT_CONTENT)
        print(f'{CONFIG_PATH} was created with a default configuration.')
        print('Please add it to your commit.')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
