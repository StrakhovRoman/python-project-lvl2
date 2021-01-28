"""Node status constants."""

ADDED, CHANGED_ADD = 'added', 'changed_add'
DELETED, CHANGED_DEL = 'deleted', 'changed_del'
UNCHANGED = 'unchanged'
PARENT = 'parent'


def get_status_operator(status=UNCHANGED):
    if status in {DELETED, CHANGED_DEL}:
        return '-'
    elif status in {ADDED, CHANGED_ADD}:
        return '+'
    return ' '
