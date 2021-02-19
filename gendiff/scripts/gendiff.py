#!/usr/bin/env python

"""Gendiff script."""

import argparse

from gendiff.engine import generate_diff
from gendiff.format.formats import DEFAULT_FORMAT


def main():
    """Script launcher."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='first file for diff')
    parser.add_argument('second_file', type=str, help='second file for diff')
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default=DEFAULT_FORMAT,
        help='set format of output',
    )
    args = parser.parse_args()
    try:
        print(generate_diff(args.first_file, args.second_file, args.format))
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
