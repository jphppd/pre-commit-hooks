import argparse
import ast
import sys
import traceback
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Sequence

DEBUG_STATEMENTS = {'pdb', 'ipdb', 'pudb', 'q', 'rdb', 'rpdb', 'wdb'}


class Debug(NamedTuple):
    line: int
    col: int
    name: str
    reason: str


class DebugStatementParser(ast.NodeVisitor):
    def __init__(self) -> None:
        self.breakpoints: List[Debug] = []

    def visit_Import(self, node: ast.Import) -> None:  # pylint: disable=invalid-name
        for name in node.names:
            if name.name in DEBUG_STATEMENTS:
                statmt = Debug(node.lineno, node.col_offset, name.name, 'imported')
                self.breakpoints.append(statmt)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:  # pylint: disable=invalid-name
        if node.module in DEBUG_STATEMENTS:
            statmt = Debug(node.lineno, node.col_offset, node.module, 'imported')
            self.breakpoints.append(statmt)

    def visit_Call(self, node: ast.Call) -> None:  # pylint: disable=invalid-name
        """python3.7+ breakpoint()"""
        if isinstance(node.func, ast.Name) and node.func.id == 'breakpoint':
            statmt = Debug(node.lineno, node.col_offset, node.func.id, 'called')
            self.breakpoints.append(statmt)
        self.generic_visit(node)


def check_file(filename: str) -> int:
    try:
        with open(filename, 'rb') as file_handler:
            ast_obj = ast.parse(file_handler.read(), filename=filename)
    except SyntaxError:
        print('{} - Could not parse ast'.format(filename))
        print()
        print('\t' + traceback.format_exc().replace('\n', '\n\t'))
        print()
        return 1

    visitor = DebugStatementParser()
    visitor.visit(ast_obj)

    for bkpt in visitor.breakpoints:
        print('{}:{}:{} - {} {}'.format(filename, bkpt.line, bkpt.col, bkpt.name, bkpt.reason))

    return int(bool(visitor.breakpoints))


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        retv |= check_file(filename)
    return retv


if __name__ == '__main__':
    sys.exit(main())
