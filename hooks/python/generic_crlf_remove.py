import argparse
import sys


def contains_crlf(filename):
    with open(filename, mode='rb') as file_checked:
        for line in file_checked.readlines():
            if line.endswith(b'\r\n'):
                return True
    return False


def removes_crlf_in_file(filename):
    with open(filename, mode='rb') as file_processed:
        lines = file_processed.readlines()
    lines = [line.replace(b'\r\n', b'\n') for line in lines]
    with open(filename, mode='wb') as file_processed:
        for line in lines:
            file_processed.write(line)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)
    files_with_crlf = list(filter(contains_crlf, args.filenames))
    for file_with_crlf in files_with_crlf:
        print('Removing CRLF end-lines in: {}'.format(file_with_crlf))
        removes_crlf_in_file(file_with_crlf)
    if files_with_crlf:
        print('')
        print('CRLF end-lines have been successfully removed. Now aborting the commit.')
        print('You can check the changes made. Then simply "git add --update ." and re-commit')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
