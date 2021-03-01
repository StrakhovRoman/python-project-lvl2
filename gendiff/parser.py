"""Argument parser."""

import argparse

from gendiff.format.formats import DEFAULT_FORMAT, formats


def get_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='first file for diff')
    parser.add_argument('second_file', type=str, help='second file for diff')
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        help='set format of output',
        default=DEFAULT_FORMAT,
        choices=formats.keys(),
    )
    return parser
