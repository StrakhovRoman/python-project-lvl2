"""Run programm modules."""
from gendiff import get_data
from gendiff.format.formats import DEFAULT_FORMAT, get_formatter
from gendiff.gen_diff import get_difference


def generate_diff(first_file, second_file, _format=DEFAULT_FORMAT):
    previous_data = get_data.read_file(first_file)
    current_data = get_data.read_file(second_file)
    diff = get_difference(previous_data, current_data)
    formatter = get_formatter(_format)
    return formatter(diff)
