"""Plain output format."""
from gendiff.format.sorting import sort_diff
from gendiff.makediff import ADDED, CHANGED, DELETED, PARENT

CHANGED_LINE = "Property '{0}{1}' was updated. From {2} to {3}"
ADDED_LINE = "Property '{0}{1}' was added with value: {2}"
DELETED_LINE = "Property '{0}{1}' was removed"


def plain(diff, path=''):
    output = []
    sort_diff(diff)

    for node in diff:
        if node.status == PARENT:
            output.append(
                plain(node.value, '{0}{1}.'.format(path, node.name)),
            )

        if node.status == CHANGED:
            previous_value, current_value = node.value
            output.append(CHANGED_LINE.format(
                path,
                node.name,
                format_value(previous_value),
                format_value(current_value),
            ),
            )

        if node.status == ADDED:
            output.append(ADDED_LINE.format(
                path,
                node.name,
                format_value(node.value),
            ),
            )

        if node.status == DELETED:
            output.append(DELETED_LINE.format(
                path,
                node.name,
                format_value(node.value),
            ),
            )
    return '\n'.join(output)


def format_value(node_value):
    if isinstance(node_value, dict):
        return '[complex value]'
    if isinstance(node_value, str):
        return "'{0}'".format(node_value)
    if node_value is None:
        return 'null'
    if isinstance(node_value, bool):
        return str(node_value).lower()
    return str(node_value)
