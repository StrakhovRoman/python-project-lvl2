"""Get file extension and read file."""
import json
import os

import yaml

extension = {
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
    '.json': json.load,
}


def read_file(path_to_file):
    _, file_extension = os.path.splitext(path_to_file)

    try:
        with open(path_to_file) as input_file:
            get_dict = extension[file_extension]
            return get_dict(input_file)

    except OSError as error:
        raise RuntimeError(
            'The file or folder does not exist!',
        ) from error

    except KeyError as error:
        raise RuntimeError(
            'Sorry, "{0}" file type is not supported.'.format(file_extension),
        ) from error
