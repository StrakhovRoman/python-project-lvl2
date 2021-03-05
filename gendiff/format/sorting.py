"""Sort diff nodes by name."""


def sort_diff(diff):
    return diff.sort(key=lambda node: node.name)
