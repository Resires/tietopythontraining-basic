import os
import shutil
import tempfile
import unittest
from selective_copy import copy_files_with_spec_extension, get_parameters_with_parser, execute_script


class TestSelectiveCopyNoFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_copy_files_with_txt_extension(self):
        copy_files_with_spec_extension(os.path.join(self.test_dir, 'source_files'),
                                       os.path.join(self.test_dir, 'destination_for_txt'),
                                       r'.txt'),
        self.assertEqual([], os.listdir(os.path.join(self.test_dir, 'destination_for_txt')))

    def test_copy_files_with_jpg_extension(self):
        copy_files_with_spec_extension(os.path.join(self.test_dir, 'source_files'),
                                       os.path.join(self.test_dir, 'destination_for_jpg'),
                                       r'.jpg'),
        self.assertEqual([], os.listdir(os.path.join(self.test_dir, 'destination_for_jpg')))

    def test_selective_copy_txt_files(self):
        source_path = os.path.join(self.test_dir, 'source_files')
        destination_path = os.path.join(self.test_dir, 'destination_for_txt')
        source, destination, extension = get_parameters_with_parser(['-s', source_path, '-d', destination_path,
                                                                     '-x', '.txt'])
        copy_files_with_spec_extension(source, destination, extension)
        self.assertEqual([], os.listdir(destination_path))

    def test_selective_copy_jpg_files(self):
        source_path = os.path.join(self.test_dir, 'source_files')
        destination_path = os.path.join(self.test_dir, 'destination_for_jpg')
        source, destination, extension = get_parameters_with_parser(['-s', source_path, '-d', destination_path,
                                                                     '-x', '.jpg'])
        copy_files_with_spec_extension(source, destination, extension)
        self.assertEqual([], os.listdir(destination_path))

    def test_execute_script_txt(self):
        source_path = os.path.join(self.test_dir, 'source_files')
        destination_path = os.path.join(self.test_dir, 'destination_for_txt')
        execute_script(['-s', source_path, '-d', destination_path, '-x', '.txt'])
        self.assertEqual([], os.listdir(destination_path))

    def test_execute_script_jpg(self):
        source_path = os.path.join(self.test_dir, 'source_files')
        destination_path = os.path.join(self.test_dir, 'destination_for_jpg')
        execute_script(['-s', source_path, '-d', destination_path, '-x', '.jpg'])
        self.assertEqual([], os.listdir(destination_path))


class TestSelectiveCopy(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        os.mkdir(os.path.join(self.test_dir, 'source_files'))
        os.mkdir(os.path.join(self.test_dir, 'source_files', 'Dir1'))
        os.mkdir(os.path.join(self.test_dir, 'source_files', 'Dir2'))
        with open(os.path.join(self.test_dir, 'source_files', 'Dir1', 'text1.txt'), 'w') as f:
            f.write('Content of first txt file.')
        with open(os.path.join(self.test_dir, 'source_files', 'Dir2', 'text1.txt'), 'w') as f:
            f.write('Content of second txt file. This file is redundant, will not be copied.')
        f = open(os.path.join(self.test_dir, 'source_files', 'Dir1', 'picture1.jpg'), 'w')
        f.close()
        f = open(os.path.join(self.test_dir, 'source_files', 'Dir2', 'picture2.jpg'), 'w')
        f.close()
        print(os.listdir(self.test_dir))

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_copy_files_with_txt_extension(self):
        copy_files_with_spec_extension(os.path.join(self.test_dir, 'source_files'),
                                       os.path.join(self.test_dir, 'destination_for_txt'),
                                       r'.txt'),
        self.assertEqual(['text1.txt'],
                         os.listdir(os.path.join(self.test_dir, 'destination_for_txt')))

    def test_copy_files_with_jpg_extension(self):
        copy_files_with_spec_extension(os.path.join(self.test_dir, 'source_files'),
                                       os.path.join(self.test_dir, 'destination_for_jpg'),
                                       r'.jpg'),
        self.assertEqual(['picture1.jpg', 'picture2.jpg'],
                         os.listdir(os.path.join(self.test_dir, 'destination_for_jpg')))

    def test_get_parameters_with_parser(self):
        self.assertEqual(('.', r'.\destination_for_jpg', '.jpg'),
                         get_parameters_with_parser([]))
        self.assertEqual((r'.\source_files', r'.\destination_for_jpg', '.jpg'),
                         get_parameters_with_parser(['-s', r'.\source_files', '-d', r'.\destination_for_jpg',
                                                     '-x', '.jpg']))
        self.assertEqual((r'.\source_files', r'.\destination_for_txt', '.txt'),
                         get_parameters_with_parser(['-s', r'.\source_files', '-d', r'.\destination_for_txt',
                                                     '-x', '.txt']))

    def test_selective_copy_txt_files(self):
        source_path = os.path.join(self.test_dir, 'source_files')
        destination_path = os.path.join(self.test_dir, 'destination_for_txt')
        source, destination, extension = get_parameters_with_parser(['-s', source_path, '-d', destination_path,
                                                                     '-x', '.txt'])
        copy_files_with_spec_extension(source, destination, extension)
        self.assertEqual(['text1.txt'], os.listdir(destination_path))

    def test_selective_copy_jpg_files(self):
        source_path = os.path.join(self.test_dir, 'source_files')
        destination_path = os.path.join(self.test_dir, 'destination_for_jpg')
        source, destination, extension = get_parameters_with_parser(['-s', source_path, '-d', destination_path,
                                                                     '-x', '.jpg'])
        copy_files_with_spec_extension(source, destination, extension)
        self.assertEqual(['picture1.jpg', 'picture2.jpg'], os.listdir(destination_path))

    def test_execute_script_txt(self):
        source_path = os.path.join(self.test_dir, 'source_files')
        destination_path = os.path.join(self.test_dir, 'destination_for_txt')
        execute_script(['-s', source_path, '-d', destination_path, '-x', '.txt'])
        self.assertEqual(['text1.txt'], os.listdir(destination_path))

    def test_execute_script_jpg(self):
        source_path = os.path.join(self.test_dir, 'source_files')
        destination_path = os.path.join(self.test_dir, 'destination_for_jpg')
        execute_script(['-s', source_path, '-d', destination_path, '-x', '.jpg'])
        self.assertEqual(['picture1.jpg', 'picture2.jpg'], os.listdir(destination_path))


if __name__ == '__main__':
    unittest.main()
