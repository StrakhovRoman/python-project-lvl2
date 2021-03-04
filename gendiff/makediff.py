"""Difference generator."""

from collections import namedtuple

ADDED = 'added'
CHANGED = 'changed'
DELETED = 'deleted'
PARENT = 'parent'
UNCHANGED = 'unchanged'


Node = namedtuple('Node', 'name value status')


def get_difference(first_data, second_data):  # noqa: WPS210
    common_keys = first_data.keys() & second_data.keys()
    added_keys = second_data.keys() - first_data.keys()
    deleted_keys = first_data.keys() - second_data.keys()
    diff = []

    for key in common_keys:
        add_common_keys_node(diff, key, first_data, second_data)

    for added_key in added_keys:
        add_node(diff, added_key, second_data, ADDED)

    for deleted_key in deleted_keys:
        add_node(diff, deleted_key, first_data, DELETED)

    return diff


def add_node(tree, name, input_data, node_status):
    tree.append(Node(name, input_data[name], node_status))


def add_common_keys_node(tree, name, previous_data, current_data):
    previous_value = previous_data[name]
    current_value = current_data[name]
    if isinstance(previous_value, dict) and isinstance(current_value, dict):
        node_value = get_difference(previous_value, current_value)
        tree.append(Node(name, node_value, PARENT))
    elif previous_value == current_value:
        tree.append(Node(name, previous_value, UNCHANGED))
    else:
        tree.append(Node(name, (previous_value, current_value), CHANGED))
