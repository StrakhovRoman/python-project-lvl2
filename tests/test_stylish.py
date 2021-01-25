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


def test_stylish_recursive():
    with open('tests/fixtures/recursive/expected.txt', 'r') as fixture:
        expected = fixture.read()

    assert expected == generate_diff(
        'tests/fixtures/recursive/recursive_previous.json',
        'tests/fixtures/recursive/recursive_current.json',
    )

    assert expected == generate_diff(
        'tests/fixtures/recursive/recursive_previous.yml',
        'tests/fixtures/recursive/recursive_current.yml',
    )
