"""Stylish output format."""
from gendiff.format.converter import convert
from gendiff.format.sorting import diff_sort
from gendiff.gen_diff import ADDED, CHANGED, DELETED, PARENT

INDENT = '  '
OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'


def stylish(diff, depth=1):
    output = []
    indent = INDENT * depth
    diff_sort(diff)

    for node in diff:
        if node.status == PARENT:
            output.append('{0}{1} {2}: {3}'.format(
                indent, get_sign(node.status), node.name, OPEN_BRACKET,
            ),
            )
            output.append(stylish(node.value, depth + 2))
            output.append('{0}{1}'.format(indent + INDENT, CLOSE_BRACKET))

        elif node.status == CHANGED:
            previous_value, current_value = node.value
            output.append(get_output_strings(
                node.name, previous_value, DELETED, indent, depth,
            ),
            )
            output.append(get_output_strings(
                node.name, current_value, ADDED, indent, depth,
            ),
            )

        else:
            output.append(get_output_strings(*node, indent, depth))

    if depth == 1:
        output = [OPEN_BRACKET] + output + [CLOSE_BRACKET]
    return '\n'.join(output)


def get_sign(status):
    if status == DELETED:
        return '-'
    elif status == ADDED:
        return '+'
    return ' '


def format_dictionary(node_value, depth=1):
    strings = []
    indent = INDENT * depth
    for key, value in node_value.items():  # noqa: WPS110
        if isinstance(value, dict):
            strings.append('{0}  {1}: {2}'.format(
                indent, key, OPEN_BRACKET,
            ),
            )
            strings.append(format_dictionary(value, depth + 2))
            strings.append('{0}{1}'.format(indent + INDENT, CLOSE_BRACKET))
        else:
            strings.append('{0}  {1}: {2}'.format(
                indent, key, value,
            ),
            )
    return '\n'.join(strings)


def get_output_strings(name, value, status, indent, depth):  # noqa: WPS110
    strings = []
    if isinstance(value, dict):
        strings.append('{0}{1} {2}: {3}'.format(
            indent, get_sign(status), name, OPEN_BRACKET,
        ),
        )
        strings.append(format_dictionary(value, depth + 2))
        strings.append('{0}{1}'.format(indent + INDENT, CLOSE_BRACKET))
    else:
        strings.append('{0}{1} {2}: {3}'.format(
            indent, get_sign(status), name, convert(value),
        ),
        )
    return '\n'.join(strings)
