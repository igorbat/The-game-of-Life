from thegameoflife_fortests import modeling
import sys
import argparse

parser = argparse.ArgumentParser(description='Info for modelling')

parser.add_argument('--fr', help='file to read (default: stdin)',
                    default='stdin')
parser.add_argument('--fw', help='file to write (default: stdout',
                    default='stdout')

args = parser.parse_args()
t = 1
q = 1
if not args.fr == 'stdin':
    sys.stdin = open(args.fr, 'r')
else:
    t = 0

if not args.fw == 'stdout':
    sys.stdout = open(args.fw, 'w')
else:
    q = 0

modeling(t, q)

if t:
    sys.stdin.close()
if q:
    sys.stdout.close()

