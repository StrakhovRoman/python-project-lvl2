"""JSON format test."""
from gendiff.engine import generate_diff


def test_json():
    with open('tests/fixtures/complex/expected.json', 'r') as fixture:
        expected = fixture.read()

    assert expected == generate_diff(
        'tests/fixtures/complex/previous.json',
        'tests/fixtures/complex/current.json',
        _format='json',
    )

    assert expected == generate_diff(
        'tests/fixtures/complex/previous.yml',
        'tests/fixtures/complex/current.yml',
        _format='json',
    )
