"""Default output format."""
from gendiff.status import status_keys

INDENT = '  '


def make_string(indent, status, name, value):  # noqa: WPS110
    return ('{0}{1} {2}: {3}'.format(
        indent,
        status_keys[status],
        name,
        value,
    )
    )


def stylish(diff, depth=1):
    output = []
    indent = INDENT * depth

    for node in diff:
        if node.parent:
            output.append(make_string(indent, node.status, node.name, '{'))
            output.append(stylish(node.value, depth + 2))
            output.append('{0}{1}'.format(indent + INDENT, '}'))
        else:
            output.append(make_string(
                indent, node.status, node.name, convert(node.value),
            ),
            )
    if depth == 1:
        output = ['{'] + output + ['}']
    return '\n'.join(output)


def convert(node_value):
    if node_value is None:
        return 'null'
    elif node_value is True:
        return 'true'
    elif node_value is False:
        return 'false'
    return node_value
