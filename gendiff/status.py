"""Node status constants."""

ADDED, CHANGED_ADD = ('added',) * 2
DELETED, CHANGED_DEL = ('deleted',) * 2
UNCHANGED = 'unchanged'


status_keys = {
    'deleted': '-',
    'added': '+',
    'unchanged': ' ',
}
