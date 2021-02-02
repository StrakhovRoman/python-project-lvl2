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
    file_name, file_extension = os.path.splitext(path_to_file)
    with open(path_to_file) as input_file:
        get_dict = extension[file_extension]
        return get_dict(input_file)
