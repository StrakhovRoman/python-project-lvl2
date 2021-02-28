"""Files difference generator."""

from collections import namedtuple

ADDED = 'added'
CHANGED = 'changed'
DELETED = 'deleted'
PARENT = 'parent'
UNCHANGED = 'unchanged'


Node = namedtuple('Node', 'name value status')


def get_difference(first_file, second_file):  # noqa: WPS210
    intersection = [key for key in first_file if key in second_file]
    addition = [key for key in second_file if key not in first_file]
    deletion = [key for key in first_file if key not in second_file]
    diff = []

    for key in intersection:
        add_intersection_node(diff, key, first_file, second_file)

    for added_key in addition:
        add_node(diff, added_key, second_file, ADDED)

    for deleted_key in deletion:
        add_node(diff, deleted_key, first_file, DELETED)

    return diff


def add_node(tree, name, input_file, node_status):
    tree.append(Node(name, input_file[name], node_status))


def add_intersection_node(tree, name, previous, current):
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
