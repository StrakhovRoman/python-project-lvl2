"""Plain output format."""
from gendiff.format.converter import convert
from gendiff.gen_diff import ADDED, CHANGED_ADD, CHANGED_DEL, DELETED, PARENT

templates = {
    CHANGED_ADD: "Property '{0}{1}' was updated. From {2} to {3}",
    ADDED: "Property '{0}{1}' was added with value: {2}",
    DELETED: "Property '{0}{1}' was removed",
}


def plain(diff, path=''):
    output = []
    for node in diff:

        if node.status == PARENT:
            output.append(
                plain(node.value, '{0}{1}.'.format(path, node.name)),
            )

        if node.status in {ADDED, DELETED}:
            output_line = path, node.name, get_value(node.value)
            output.append(templates[node.status].format(*output_line))

        if node.status == CHANGED_DEL:
            previous = get_value(node.value)

        if node.status == CHANGED_ADD:
            output.append(templates[CHANGED_ADD].format(
                path, node.name, previous, get_value(node.value),
            ),
            )

    return '\n'.join(output)


def get_value(node_value):
    if isinstance(node_value, dict):
        return '[complex value]'
    elif isinstance(node_value, str):
        return "'{0}'".format(node_value)
    return convert(node_value)
