"""Files difference generator."""

from collections import namedtuple

from gendiff.status import ADDED, CHANGED_ADD, CHANGED_DEL, DELETED, UNCHANGED

Node = namedtuple(
    'Node', 'name value status parent', defaults=(UNCHANGED, False),
)


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


def add_node(tree, key, input_file, status):
    if isinstance(input_file[key], dict):
        node_value = get_difference(input_file[key], input_file[key])
        tree.append(Node(key, node_value, status, parent=True))
    else:
        tree.append(Node(key, input_file[key], status))


def add_intersection_node(tree, key, file1, file2):
    if isinstance(file1[key], dict) and isinstance(file2[key], dict):
        node_value = get_difference(file1[key], file2[key])
        tree.append(Node(key, node_value, parent=True))
    elif file1[key] == file2[key]:
        tree.append(Node(key, file1[key]))
    else:
        add_node(tree, key, file1, CHANGED_DEL)
        add_node(tree, key, file2, CHANGED_ADD)
