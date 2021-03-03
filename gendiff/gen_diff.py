"""Files difference generator."""

from collections import namedtuple

ADDED = 'added'
CHANGED = 'changed'
DELETED = 'deleted'
PARENT = 'parent'
UNCHANGED = 'unchanged'


Node = namedtuple('Node', 'name value status')


def get_difference(first_file, second_file):  # noqa: WPS210
    common_keys = first_file.keys() & second_file.keys()
    added_keys = second_file.keys() - first_file.keys()
    deleted_keys = first_file.keys() - second_file.keys()
    diff = []

    for key in common_keys:
        add_common_keys_node(diff, key, first_file, second_file)

    for added_key in added_keys:
        add_node(diff, added_key, second_file, ADDED)

    for deleted_key in deleted_keys:
        add_node(diff, deleted_key, first_file, DELETED)

    return diff


def add_node(tree, name, input_file, node_status):
    tree.append(Node(name, input_file[name], node_status))


def add_common_keys_node(tree, name, previous, current):
    previous_value = previous[name]
    current_value = current[name]
    if isinstance(previous_value, dict) and isinstance(current_value, dict):
        node_value = get_difference(previous_value, current_value)
        tree.append(Node(name, node_value, PARENT))
    elif previous_value == current_value:
        tree.append(Node(name, previous_value, UNCHANGED))
    else:
        tree.append(Node(name, (previous_value, current_value), CHANGED))


def diff_sort(diff):
    return diff.sort(key=lambda node: node.name)
