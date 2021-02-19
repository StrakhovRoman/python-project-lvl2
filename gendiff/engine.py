"""Run programm modules."""
from gendiff.data_processing import read_file
from gendiff.format.formats import DEFAULT_FORMAT, get_format_function
from gendiff.gen_diff import get_difference


def generate_diff(first_file, second_file, _format=DEFAULT_FORMAT):
    previous_file = read_file(first_file)
    current_file = read_file(second_file)
    diff = get_difference(previous_file, current_file)
    format_function = get_format_function(_format)
    return format_function(diff)
