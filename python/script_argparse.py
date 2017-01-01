"""
Python Script Template

A simple python 2.7 script template with argument parsing.

Author: Derek Jobst
Email: contact@derekjobst.com


References:
'Python 2.7 Docs: argparse'
https://docs.python.org/2/library/argparse.html
"""

import argparse


def setup():
    ''' Setup argument parser and CLI '''

    parser = argparse.ArgumentParser(
        description='Process some integers.'
    )

    parser.add_argument(
        'integers',
        nargs='+',
        metavar='N',
        type=int,
        help='an integer for the accumulator'
    )
    parser.add_argument(
        '--sum',
        action='store_const',
        dest='accumulate',
        const=sum,
        default=max,
        help='sum the integers (default: find the max)'
    )

    return parser.parse_args()


def main(args):
    print args.accumulate(args.integers)


if __name__ == '__main__':
    main(setup())
