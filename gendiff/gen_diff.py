"""Files difference generator."""

from collections import namedtuple

from gendiff import status

Node = namedtuple('Node', 'name value status')


def get_difference(first_file, second_file):  # noqa: WPS210
    intersection = [key for key in first_file if key in second_file]
    addition = [key for key in second_file if key not in first_file]
    deletion = [key for key in first_file if key not in second_file]
    diff = []

    for key in intersection:
        add_intersection_node(diff, key, first_file, second_file)

    for added_key in addition:
        add_node(diff, added_key, second_file, status.ADDED)

    for deleted_key in deletion:
        add_node(diff, deleted_key, first_file, status.DELETED)

    diff.sort(key=lambda node: node.name)
    return diff


def add_node(tree, name, input_file, node_status):
    tree.append(Node(name, input_file[name], node_status))


def add_intersection_node(tree, name, previous, current):
    if isinstance(previous[name], dict) and isinstance(current[name], dict):
        node_value = get_difference(previous[name], current[name])
        tree.append(Node(name, node_value, status.PARENT))
    elif previous[name] == current[name]:
        add_node(tree, name, previous, status.UNCHANGED)
    else:
        add_node(tree, name, previous, status.CHANGED_DEL)
        add_node(tree, name, current, status.CHANGED_ADD)
