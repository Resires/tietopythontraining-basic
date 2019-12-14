import os


def big_files_finder(source_destination, max_file_size):
    for root, dir_names, file_names in os.walk(source_destination):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            if file_size > max_file_size:
                print('Detected file with size bigger than {} bytes ({} bytes). '
                      'File location: {}'.format(max_file_size, file_size, file_path))


if __name__ == '__main__':
    big_files_finder(r'.\localisation_with_files', 100)
    print()
    big_files_finder(r'.\localisation_with_files', 300)
    print()
    big_files_finder(r'.\localisation_with_files', 500)
