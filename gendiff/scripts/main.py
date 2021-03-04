#!/usr/bin/env python

"""Gendiff script."""


from gendiff.cli_argparser import get_parser
from gendiff.engine import generate_diff


def main():
    args = get_parser().parse_args()
    try:
        print(generate_diff(args.first_file, args.second_file, args.format))
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
