import os
import shutil


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


if __name__ == '__main__':
    copy_files_with_spec_extension(r'.\source_files', r'.\destination_for_jpg', '.jpg')
    copy_files_with_spec_extension(r'.\source_files', r'.\destination_for_txt', '.txt')
