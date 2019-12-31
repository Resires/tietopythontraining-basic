# Example usages:
# python selective_copy.py
# python selective_copy.py -s .\First_lvl_dir\source_files -d .\First_lvl_dir\destination_for_txt -x .txt
# python selective_copy.py -s .\First_lvl_dir\source_files -d .\First_lvl_dir\destination_for_jpg -x .jpg
import argparse
import os
import shutil
import sys


def get_parameters_with_parser(args):
    parser = argparse.ArgumentParser('Copying all the files with specific extension from source to destination dir.')
    parser.add_argument('-s', action='store', dest='source_path', default=r'.',
                        help='Input directory path, from which files will be copied.')
    parser.add_argument('-d', action='store', dest='destination_path', default=r'.\destination_for_jpg',
                        help='Input directory path, to which files will be copied.')
    parser.add_argument('-x', action='store', dest='extension', default=r'.jpg',
                        help='Desired files extension.')
    input_parameters = parser.parse_args(args)
    return input_parameters.source_path, input_parameters.destination_path, input_parameters.extension


def copy_files_with_spec_extension(source_path, destination_path, file_extension):
    if os.path.isdir(destination_path):
        print('Destination folder "{}" already exist'.format(destination_path))
    else:
        os.mkdir(destination_path)
    for root, dir_names, file_names in os.walk(source_path, topdown=True):
        for file_name in file_names:
            if file_name.endswith(file_extension):
                if os.path.isfile(os.path.join(destination_path, file_name)):
                    print('Copy FAILED - File "{}" from source localisation "{}" already exist in destination '
                          'folder "{}". '.format(file_name, root, destination_path))
                else:
                    shutil.copy(os.path.join(root, file_name), destination_path)
                    print('COPY SUCCESSFUL - File "{}" from source localisation "{}" copied into destination '
                          'folder "{}".'.format(file_name, root, destination_path))


def execute_script(args):
    source, destination, extension = get_parameters_with_parser(args)
    copy_files_with_spec_extension(source, destination, extension)


if __name__ == '__main__':
    execute_script(sys.argv[1:])
