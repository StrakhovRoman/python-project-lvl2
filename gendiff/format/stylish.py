"""Stylish output format."""
from gendiff.format.converter import convert

from gendiff.gen_diff import (  # isort:skip
    ADDED, CHANGED_ADD, CHANGED_DEL, DELETED, PARENT, UNCHANGED,
)

INDENT = '  '


def stylish(diff, depth=1):
    output = []
    indent = INDENT * depth
    for node in diff:
        line_args = output, indent, node, depth

        if node.status == PARENT:
            get_output_line(*line_args, stylish)

        elif isinstance(node.value, dict):
            get_output_line(*line_args, format_dictionary)

        else:
            output.append(make_string(
                indent, node.name, convert(node.value), node.status,
            ),
            )
    if depth == 1:
        output = ['{'] + output + ['}']
    return '\n'.join(output)


def make_string(indent, name, value, status=UNCHANGED):  # noqa: WPS110
    return ('{0}{1} {2}: {3}'.format(
        indent,
        get_status_operator(status),
        name,
        value,
    )
    )


def get_status_operator(status):
    if status in {DELETED, CHANGED_DEL}:
        return '-'
    elif status in {ADDED, CHANGED_ADD}:
        return '+'
    return ' '


def get_output_line(out, indent, node, depth, func):
    out.append(make_string(indent, node.name, '{', node.status))
    out.append(func(node.value, depth + 2))
    out.append('{0}{1}'.format(indent + INDENT, '}'))
    return out


def format_dictionary(node_value, depth=1):
    out = []
    indent = INDENT * depth
    for key, value in node_value.items():  # noqa: WPS110
        if isinstance(value, dict):
            out.append(make_string(indent, key, '{'))
            out.append(format_dictionary(value, depth + 2))
            out.append('{0}{1}'.format(indent + INDENT, '}'))
        else:
            out.append(make_string(
                indent, key, value,
            ),
            )
    return '\n'.join(out)
