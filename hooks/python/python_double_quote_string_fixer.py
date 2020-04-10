import argparse
import io
import re
import sys
import tokenize
from typing import List
from typing import Optional
from typing import Sequence

START_QUOTE_RE = re.compile('^[a-zA-Z]*"')


def handle_match(token_text: str) -> str:
    if '"""' in token_text or "'''" in token_text:
        return token_text

    match = START_QUOTE_RE.match(token_text)
    if match is not None:
        meat = token_text[match.end():-1]
        if '"' in meat or "'" in meat:
            return token_text
        return match.group().replace('"', "'") + meat + "'"
    return token_text


def get_line_offsets_by_line_no(src: str) -> List[int]:
    # Padded so we can index with line number
    offsets = [-1, 0]
    for line in src.splitlines(True):
        offsets.append(offsets[-1] + len(line))
    return offsets


def fix_strings(filename: str) -> int:  # pylint: disable=too-many-locals
    with open(filename, encoding='UTF-8', newline='') as file_handler:
        contents = file_handler.read()
    line_offsets = get_line_offsets_by_line_no(contents)

    # Basically a mutable string
    splitcontents = list(contents)

    # Iterate in reverse so the offsets are always correct
    tokens_l = list(tokenize.generate_tokens(io.StringIO(contents).readline))
    tokens = reversed(tokens_l)
    for token_type, token_text, (srow, scol), (erow, ecol), _ in tokens:
        if token_type == tokenize.STRING:
            new_text = handle_match(token_text)
            splitcontents[line_offsets[srow] + scol:line_offsets[erow] + ecol] = new_text

    new_contents = ''.join(splitcontents)
    if contents != new_contents:
        with open(filename, 'w', encoding='UTF-8', newline='') as file_handler:
            file_handler.write(new_contents)
        return 1
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        return_value = fix_strings(filename)
        if return_value != 0:
            print(f'Fixing strings in {filename}')
        retv |= return_value

    return retv


if __name__ == '__main__':
    sys.exit(main())
