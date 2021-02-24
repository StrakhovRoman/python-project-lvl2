"""All output formats test."""
import pytest

from gendiff.engine import generate_diff
from gendiff.format.formats import DEFAULT_FORMAT, JSON_FORMAT, PLAIN_FORMAT

PATH_TO_FIXTURES = 'tests/fixtures/'

flat_json_files = ('flat/flat_previous.json', 'flat/flat_current.json')
flat_yml_files = ('flat/flat_previous.yml', 'flat/flat_current.yml')

flat_expected_stylish = 'flat/expected_flat.txt'
flat_expected_plain = 'flat/expected_flat_plain.txt'

complex_json_files = ('complex/previous.json', 'complex/current.json')
complex_yml_files = ('complex/previous.yml', 'complex/current.yml')

complex_expected_stylish = 'complex/expected.txt'
complex_expected_plain = 'complex/expected_plain.txt'
complex_expected_json = 'complex/expected.json'


@pytest.mark.parametrize(
    'path_to_previous, path_to_current, path_to_expected, output_format',
    [
        (*flat_json_files, flat_expected_stylish, DEFAULT_FORMAT),

        (*flat_yml_files, flat_expected_stylish, DEFAULT_FORMAT),

        (*complex_json_files, complex_expected_stylish, DEFAULT_FORMAT),

        (*complex_yml_files, complex_expected_stylish, DEFAULT_FORMAT),

        (*flat_json_files, flat_expected_plain, PLAIN_FORMAT),

        (*flat_yml_files, flat_expected_plain, PLAIN_FORMAT),

        (*complex_json_files, complex_expected_plain, PLAIN_FORMAT),

        (*complex_yml_files, complex_expected_plain, PLAIN_FORMAT),

        (*complex_json_files, complex_expected_json, JSON_FORMAT),
    ])
def test_formats(
    path_to_previous,
    path_to_current,
    path_to_expected,
    output_format,
):
    expected = get_expected(path_to_expected)
    previous = '{0}{1}'.format(PATH_TO_FIXTURES, path_to_previous)
    current = '{0}{1}'.format(PATH_TO_FIXTURES, path_to_current)
    assert expected == generate_diff(previous, current, _format=output_format)


def get_expected(path_to_file):
    with open('{0}{1}'.format(PATH_TO_FIXTURES, path_to_file), 'r') as fixture:
        return fixture.read()
