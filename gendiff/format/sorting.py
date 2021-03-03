"""Sort diff nodes by name."""


def diff_sort(diff):
    return diff.sort(key=lambda node: node.name)
