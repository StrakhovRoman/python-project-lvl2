"""Plain format test."""
from gendiff.engine import generate_diff


def test_plain():
    with open('tests/fixtures/complex/expected_plain.txt', 'r') as fixture:
        expected = fixture.read()

    assert expected == generate_diff(
        'tests/fixtures/complex/previous.json',
        'tests/fixtures/complex/current.json',
        _format='plain',
    )

    assert expected == generate_diff(
        'tests/fixtures/complex/previous.yml',
        'tests/fixtures/complex/current.yml',
        _format='plain',
    )
