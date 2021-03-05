"""JSON output format."""
import json

from gendiff.format.sorting import sort_diff
from gendiff.makediff import CHANGED, PARENT


def get_json(diff):
    return json.dumps(make_diff_as_dict(diff), indent=2)


def make_diff_as_dict(diff):
    sort_diff(diff)
    diff_as_dict = []
    for node in diff:

        if node.status == PARENT:
            diff_as_dict.append({
                'key': node.name,
                'value': make_diff_as_dict(node.value),
                'status': PARENT,
            })
        elif node.status == CHANGED:
            previous_value, current_value = node.value
            diff_as_dict.append({
                'key': node.name,
                'value': {
                    'previous': previous_value,
                    'current': current_value,
                },
                'status': CHANGED,
            })
        else:
            diff_as_dict.append({
                'key': node.name,
                'value': node.value,
                'status': node.status,
            })
    return diff_as_dict
