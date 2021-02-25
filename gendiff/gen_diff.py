"""Files difference generator."""

from collections import namedtuple

ADDED, CHANGED_ADD = 'added', 'changed_add'
DELETED, CHANGED_DEL = 'deleted', 'changed_del'
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

    diff.sort(key=lambda node: node.name)
    return diff


def add_node(tree, name, input_file, node_status):
    tree.append(Node(name, input_file[name], node_status))


def add_intersection_node(tree, name, previous, current):
    if isinstance(previous[name], dict) and isinstance(current[name], dict):
        node_value = get_difference(previous[name], current[name])
        tree.append(Node(name, node_value, PARENT))
    elif previous[name] == current[name]:
        add_node(tree, name, previous, UNCHANGED)
    else:
        add_node(tree, name, previous, CHANGED_DEL)
        add_node(tree, name, current, CHANGED_ADD)
