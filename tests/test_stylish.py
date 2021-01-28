"""Stylish format test."""
from gendiff.engine import generate_diff


def test_stylish_flat():
    with open('tests/fixtures/flat/expected_flat.txt', 'r') as fixture:
        expected_flat = fixture.read()

    assert expected_flat == generate_diff(
        'tests/fixtures/flat/flat_previous.json',
        'tests/fixtures/flat/flat_current.json',
    )

    assert expected_flat == generate_diff(
        'tests/fixtures/flat/flat_previous.yml',
        'tests/fixtures/flat/flat_current.yml',
    )


def test_stylish():
    with open('tests/fixtures/complex/expected.txt', 'r') as fixture:
        expected = fixture.read()

    assert expected == generate_diff(
        'tests/fixtures/complex/previous.json',
        'tests/fixtures/complex/current.json',
    )

    assert expected == generate_diff(
        'tests/fixtures/complex/previous.yml',
        'tests/fixtures/complex/current.yml',
    )
