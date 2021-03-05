"""Stylish output format."""
from gendiff.format.sorting import sort_diff
from gendiff.makediff import ADDED, CHANGED, DELETED, PARENT

INDENT = '  '
OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'


def get_stylish(diff):
    return '{0}\n{1}\n{2}'.format(
        OPEN_BRACKET, stylish(diff), CLOSE_BRACKET,
    )


def stylish(diff, depth=1):
    output_lines = []
    indent = INDENT * depth
    sort_diff(diff)

    for node in diff:
        if node.status == PARENT:
            output_lines.append('{0}{1} {2}: {3}'.format(
                indent, get_sign(node.status), node.name, OPEN_BRACKET,
            ),
            )
            output_lines.append(stylish(node.value, depth + 2))
            output_lines.append('{0}{1}'.format(
                indent + INDENT, CLOSE_BRACKET,
            ),
            )

        elif node.status == CHANGED:
            previous_value, current_value = node.value
            output_lines.append(format_line(
                node.name, previous_value, DELETED, indent, depth,
            ),
            )
            output_lines.append(format_line(
                node.name, current_value, ADDED, indent, depth,
            ),
            )

        else:
            output_lines.append(format_line(
                node.name,
                node.value,
                node.status,
                indent,
                depth,
            ),
            )

    return '\n'.join(output_lines)


def get_sign(status):
    if status == DELETED:
        return '-'
    elif status == ADDED:
        return '+'
    return ' '


def format_dictionary(node_value, depth=1):
    lines = []
    indent = INDENT * depth
    for key, value in node_value.items():  # noqa: WPS110
        if isinstance(value, dict):
            lines.append('{0}  {1}: {2}'.format(
                indent, key, OPEN_BRACKET,
            ),
            )
            lines.append(format_dictionary(value, depth + 2))
            lines.append('{0}{1}'.format(indent + INDENT, CLOSE_BRACKET))
        else:
            lines.append('{0}  {1}: {2}'.format(
                indent, key, value,
            ),
            )
    return '\n'.join(lines)


def format_line(name, value, status, indent, depth):  # noqa: WPS110
    lines = []
    if isinstance(value, dict):
        lines.append('{0}{1} {2}: {3}'.format(
            indent, get_sign(status), name, OPEN_BRACKET,
        ),
        )
        lines.append(format_dictionary(value, depth + 2))
        lines.append('{0}{1}'.format(indent + INDENT, CLOSE_BRACKET))
    else:
        lines.append('{0}{1} {2}: {3}'.format(
            indent, get_sign(status), name, format_node_value(value),
        ),
        )
    return '\n'.join(lines)


def format_node_value(node_value):
    if node_value is None:
        return 'null'
    elif isinstance(node_value, bool):
        return str(node_value).lower()
    return str(node_value)
