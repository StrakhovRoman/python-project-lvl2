"""JSON output format."""
import json

from gendiff.format.converter import convert
from gendiff.format.sorting import diff_sort
from gendiff.makediff import CHANGED, PARENT

INDENT = ' '
OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'


def get_json(diff, depth=1):  # noqa: WPS210
    output = []
    indent = INDENT * depth
    diff_sort(diff)

    for index, node in enumerate(diff):
        if node.status == PARENT:
            output.append(
                '{0} "{1}": {2}"status": "{3}", "value": {4}'.format(
                    indent, node.name, OPEN_BRACKET, node.status, OPEN_BRACKET,
                ),
            )
            output.append(get_json(node.value, depth + 2))
            string = format_string('{0}{1}{2}', index, len(diff))
            output.append(string.format(
                indent + INDENT, CLOSE_BRACKET, CLOSE_BRACKET,
            ),
            )
        elif node.status == CHANGED:
            previous_value, current_value = node.value
            string = format_string(
                '{0} "{1}": {2}"status": "{3}", "old": {4}, "new": {5}{6}',
                index,
                len(diff),
            )
            output.append(
                string.format(
                    indent,
                    node.name,
                    OPEN_BRACKET,
                    node.status,
                    format_value(previous_value),
                    format_value(current_value),
                    CLOSE_BRACKET,
                ),
            )
        else:
            string = format_string(
                '{0} "{1}": {2}"status": "{3}", "value": {4}{5}',
                index,
                len(diff),
            )
            output.append(
                string.format(
                    indent,
                    node.name,
                    OPEN_BRACKET,
                    node.status,
                    format_value(node.value),
                    CLOSE_BRACKET,
                ),
            )
    if depth == 1:
        output = [OPEN_BRACKET] + output + [CLOSE_BRACKET]
    return '\n'.join(output)


def format_string(string, index, length):
    if index < length - 1:
        return '{0}{1}'.format(string, ',')
    return string


def format_value(node_value):
    if isinstance(node_value, dict):
        return json.dumps(node_value)
    if isinstance(node_value, str):
        return '"{0}"'.format(node_value)
    return convert(node_value)
