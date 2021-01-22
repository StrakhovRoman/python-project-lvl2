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
        previous_file_extension, previous_file = read_file(first_file)
        current_file_extension, current_file = read_file(second_file)

    except FileNotFoundError as error:
        print(str(error)[10:])

    except KeyError as error:
        print('Sorry, {0} file type is not supported.'.format(error))

    else:

        if previous_file_extension == current_file_extension:
            diff = get_difference(previous_file, current_file)
            print(formats[_format](diff))
        else:
            print(
                'Sorry, but files must be of the same type.',
            )
