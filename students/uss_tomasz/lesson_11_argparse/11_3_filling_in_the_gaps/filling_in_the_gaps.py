# Example usages:
# python filling_in_the_gaps.py -f spam
# python filling_in_the_gaps.py -f spam -g 3 -l 4
# python filling_in_the_gaps.py -f spam -p First_lvl_dir\Files_to_rename
# python filling_in_the_gaps.py -f spam -p First_lvl_dir\Files_to_rename -g 3 -l 10

import argparse
import os
import sys


def get_parameters_with_parser(args):
    parser = argparse.ArgumentParser('Taking files from current directory with specified prefix and renaming them. '
                                     'If there are any gaps in numeration, gaps are removed. '
                                     'Additional option - inserting gap with specified length into the numeration.')
    parser.add_argument('-p', action='store', dest='path', default='.',
                        help='Store a path to the dir with files.')
    parser.add_argument('-f', action='store', dest='prefix', default='spam',
                        help='Prefix for files on which will be operated')
    parser.add_argument('-g', action='store', dest='gap_position', default='3', type=int,
                        help='Position on which gap between file names is inserted.')
    parser.add_argument('-l', action='store', dest='gap_length', default='0', type=int,
                        help='Length of a gap between file names during insertion. If this parameter is not mentioned, '
                             'then it means that gap insertion will be not executed.')
    input_parameters = parser.parse_args(args)
    return input_parameters.path, input_parameters.prefix, input_parameters.gap_position, input_parameters.gap_length


def get_numbered_file_names_with_prefix(localisation_path, prefix):
    file_names = [f for f in os.listdir(localisation_path)
                  if os.path.isfile(os.path.join(localisation_path, f)) and f.startswith(prefix)]
    file_names_split = []
    for file_name in file_names:
        extension = file_name[file_name.find('.'):]
        middle_part = file_name.replace(prefix, '').replace(extension, '')
        if middle_part.isdigit():
            file_name_split = {'number': middle_part, 'extension': extension}
            file_names_split.append(file_name_split)
    return file_names_split


def rename_files_with_filling_gaps(localisation_path, prefix):
    file_names_split = get_numbered_file_names_with_prefix(localisation_path, prefix)
    current_number = 0
    for file_name_split in file_names_split:
        current_number += 1
        file_old_name = ''.join([prefix, file_name_split['number'], file_name_split['extension']])
        if int(file_name_split['number']) == current_number:
            print('File {} has a correct number ({})'.format(file_old_name, current_number))
        else:
            file_new_name = ''.join([prefix, str(current_number).zfill(3), file_name_split['extension']])
            os.rename(os.path.join(localisation_path, file_old_name),
                      os.path.join(localisation_path, file_new_name))
            print('File {} renamed. New name: {}'.format(file_old_name, file_new_name))


def insert_gap_into_numbered_files(localisation_path, prefix, gap_position, gap_length=1):
    if gap_length < 1:
        print("Wrong input data. Gap length must be positive")
        return False
    # It is needed to start with highest number, and then rename to lowest:
    file_names_split = reversed(get_numbered_file_names_with_prefix(localisation_path, prefix))
    for file_name_split in file_names_split:
        if int(file_name_split['number']) >= gap_position:
            file_old_name = ''.join([prefix, file_name_split['number'], file_name_split['extension']])
            new_number = str(int(file_name_split['number']) + gap_length).zfill(3)
            file_new_name = ''.join([prefix, new_number, file_name_split['extension']])
            os.rename(os.path.join(localisation_path, file_old_name),
                      os.path.join(localisation_path, file_new_name))
            print('File {} renamed. New name: {}'.format(file_old_name, file_new_name))
        else:
            print('The rest of the files are below gap position ({}). No need to change.'.format(gap_position))
            break


def execute_script(args):
    files_localisation, files_prefix, gap_position_for_insert, gap_length_for_insert = get_parameters_with_parser(args)
    if gap_length_for_insert == 0:
        rename_files_with_filling_gaps(files_localisation, files_prefix)
    else:
        insert_gap_into_numbered_files(files_localisation, files_prefix, gap_position_for_insert, gap_length_for_insert)


if __name__ == '__main__':
    execute_script(sys.argv[1:])
