import os


def get_numbered_file_names_with_prefix(prefix):
    file_names = [f for f in os.listdir(os.curdir) if os.path.isfile(f) and f.startswith(prefix)]
    file_names_split = []
    for file_name in file_names:
        extension = file_name[file_name.find('.'):]
        middle_part = file_name.replace(prefix, '').replace(extension, '')
        if middle_part.isdigit():
            file_name_split = {'number': middle_part, 'extension': extension}
            file_names_split.append(file_name_split)
    return file_names_split


def rename_files_with_filling_gaps(prefix):
    file_names_split = get_numbered_file_names_with_prefix(prefix)
    current_number = 0
    for file_name_split in file_names_split:
        current_number += 1
        file_old_name = ''.join([prefix, file_name_split['number'], file_name_split['extension']])
        if int(file_name_split['number']) == current_number:
            print('File {} has a correct number ({})'.format(file_old_name, current_number))
        else:
            file_new_name = ''.join([prefix, str(current_number).zfill(3), file_name_split['extension']])
            os.rename(file_old_name, file_new_name)
            print('File {} renamed. New name: {}'.format(file_old_name, file_new_name))


def insert_gap_into_numbered_files(prefix, gap_position, gap_length=1):
    if gap_length < 1:
        print("Wrong input data. Gap length must be positive")
        return False
    file_names_split = reversed(get_numbered_file_names_with_prefix(prefix))    # It is needed to start with highest
    for file_name_split in file_names_split:                                    # number, and then rename to lowest
        if int(file_name_split['number']) >= gap_position:
            file_old_name = ''.join([prefix, file_name_split['number'], file_name_split['extension']])
            new_number = str(int(file_name_split['number']) + gap_length).zfill(3)
            file_new_name = ''.join([prefix, new_number, file_name_split['extension']])
            os.rename(file_old_name, file_new_name)
            print('File {} renamed. New name: {}'.format(file_old_name, file_new_name))
        else:
            print('The rest of the files are below gap position ({}). No need to change.'.format(gap_position))
            break


rename_files_with_filling_gaps('spam')
input('Removing gaps finished. In order to inserting gap press enter.')
insert_gap_into_numbered_files('spam', 3, 2)
