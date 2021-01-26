"""Default output format."""
from gendiff.status import status_keys

INDENT = '  '


def stylish(diff, depth=1):
    output = []
    indent = INDENT * depth
    for node in diff:
        if node.parent:
            get_output(output, indent, node, depth, stylish)
        elif isinstance(node.value, dict):
            get_output(output, indent, node, depth, format_dictionary_value)
        else:
            output.append(make_string(
                indent, node.name, convert(node.value), node.status,
            ),
            )
    if depth == 1:
        output = ['{'] + output + ['}']
    return '\n'.join(output)


def make_string(indent, name, value, status='unchanged'):  # noqa: WPS110
    return ('{0}{1} {2}: {3}'.format(
        indent,
        status_keys[status],
        name,
        value,
    )
    )


def get_output(out, indent, node, depth, func):
    out.append(make_string(indent, node.name, '{', node.status))
    out.append(func(node.value, depth + 2))
    out.append('{0}{1}'.format(indent + INDENT, '}'))
    return out


def format_dictionary_value(node_value, depth=1):
    out = []
    indent = INDENT * depth
    for key, value in node_value.items():  # noqa: WPS110
        if isinstance(value, dict):
            out.append(make_string(indent, key, '{'))
            out.append(format_dictionary_value(value, depth + 2))
            out.append('{0}{1}'.format(indent + INDENT, '}'))
        else:
            out.append(make_string(
                indent, key, value,
            ),
            )
    return '\n'.join(out)


def convert(node_value):
    if node_value is None:
        return 'null'
    elif isinstance(node_value, bool):
        return str(node_value).lower()
    return node_value
