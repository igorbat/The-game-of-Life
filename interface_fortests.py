from thegameoflife_fortests import modeling
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='Info for modelling')

    parser.add_argument('--fr', help='file to read (default: sys.stdin)',
                        default='sys.stdin')
    parser.add_argument('--fw', help='file to write (default: sys.stdout)',
                        default='sys.stdout')

    args = parser.parse_args()

    FileRead = sys.stdin
    FileWrite = sys.stdout

    if not args.fr == 'sys.stdin':
        FileRead = open(args.fr, 'r')

    if not args.fw == 'sys.stdout':
        FileWrite = open(args.fw, 'w')

    modeling(FileRead, FileWrite)

    if not args.fr == 'sys.stdin':
        FileRead.close()
    if not args.fw == 'sys.stdout':
        FileWrite.close()


if __name__ == '__main__':
    main()
