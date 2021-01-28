"""Difference generator test."""
from gendiff import gen_diff
from gendiff.data_processing import read_file


def test_gen_diff():
    with open('tests/fixtures/flat/expected_diff.txt', 'r') as fixture:
        expected = fixture.read()
    previous_file = read_file('tests/fixtures/flat/flat_previous.json')
    current_file = read_file('tests/fixtures/flat/flat_current.json')
    assert expected == str(
        gen_diff.get_difference(previous_file, current_file),
    )
