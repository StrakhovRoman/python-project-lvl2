"""Data of formats."""
from gendiff.format import json_format, plain, stylish

formats = {
    'stylish': stylish.stylish,
    'plain': plain.plain,
    'json': json_format.get_json,
}

DEFAULT_FORMAT = 'stylish'


def get_format_function(file_format):
    try:
        return formats[file_format]
    except KeyError as error:
        raise RuntimeError(
            'Sorry, "{0}" output format is not correct.'.format(file_format),
        ) from error
