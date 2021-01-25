"""Run programm modules."""
from gendiff.data_processing import read_file
from gendiff.formats import stylish
from gendiff.gen_diff import get_difference

formats = {
    'stylish': stylish.stylish,
    # 'plain': plain
}


def generate_diff(first_file, second_file, _format='stylish'):

    try:  # noqa: WPS229
        previous_file = read_file(first_file)
        current_file = read_file(second_file)

    except FileNotFoundError as error:
        print(str(error)[10:])

    except KeyError as error:
        print('Sorry, {0} file type is not supported.'.format(error))

    else:
        diff = get_difference(previous_file, current_file)
        return formats[_format](diff)
