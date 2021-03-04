"""Data of formats."""
from gendiff.format import json, plain, stylish

formats = {
    'stylish': stylish.get_stylish,
    'plain': plain.plain,
    'json': json.get_json,
}

DEFAULT_FORMAT = 'stylish'
PLAIN_FORMAT = 'plain'
JSON_FORMAT = 'json'


def get_formatter(diff_format):
    try:
        return formats[diff_format]
    except KeyError as error:
        raise RuntimeError(
            'Sorry, "{0}" output format is not correct.'.format(diff_format),
        ) from error
