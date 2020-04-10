from __future__ import print_function
import argparse
import sys


def contains_crlf(filename):
    with open(filename, mode='rb') as file_checked:
        for line in file_checked.readlines():
            if line.endswith(b'\r\n'):
                return True
    return False


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)
    files_with_crlf = filter(contains_crlf, args.filenames)
    return_code = 0
    for file_with_crlf in files_with_crlf:
        print('CRLF end-lines detected in file: {0}'.format(file_with_crlf))
        return_code = 1
    return return_code


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
