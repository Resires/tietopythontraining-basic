import os
import shutil
import unittest
from selective_copy import copy_files_with_spec_extension, get_parameters_with_parser


class TestSelectiveCopy(unittest.TestCase):
    def setUp(self):
        os.mkdir(r'.\source_files\.')
        os.mkdir(r'.\source_files\Dir1\.')
        os.mkdir(r'.\source_files\Dir2\.')
        f = open(r'.\source_files\Dir1\picture1.jpg', 'w')
        f.close()
        f = open(r'.\source_files\Dir1\picture2.jpg', 'w')
        f.close()
        f = open(r'.\source_files\Dir1\text1.txt', 'w')
        f.close()
        f = open(r'.\source_files\Dir2\picture2.jpg', 'w')
        f.close()

    def tearDown(self):
        shutil.rmtree(r'.\source_files\.')

    def test_copy_files_with_txt_extension(self):
        copy_files_with_spec_extension(r'.\source_files', r'.\destination_for_txt', r'.txt'),
        self.assertEqual(['text1.txt'],
                         os.listdir(os.path.dirname(r'.\destination_for_txt\.')))
        shutil.rmtree(r'.\destination_for_txt\.')

    def test_copy_files_with_jpg_extension(self):
        copy_files_with_spec_extension(r'.\source_files', r'.\destination_for_jpg', r'.jpg'),
        self.assertEqual(['picture1.jpg', 'picture2.jpg'],
                         os.listdir(os.path.dirname(r'.\destination_for_jpg\.')))
        shutil.rmtree(r'.\destination_for_jpg\.')

    def test_get_parameters_with_parser_txt(self):
        source, destination, extension = get_parameters_with_parser(['-s', r'.\source_files', '-d',
                                                                     r'.\destination_for_txt', '-x', '.txt'])
        self.assertEqual(r'.\source_files', source)
        self.assertEqual(r'.\destination_for_txt', destination)
        self.assertEqual('.txt', extension)

    def test_get_parameters_with_parser_jpg(self):
        source, destination, extension = get_parameters_with_parser(['-s', r'.\source_files', '-d',
                                                                     r'.\destination_for_jpg', '-x', '.jpg'])
        self.assertEqual(r'.\source_files', source)
        self.assertEqual(r'.\destination_for_jpg', destination)
        self.assertEqual('.jpg', extension)

    def test_selective_copy_txt_files(self):
        source, destination, extension = get_parameters_with_parser(['-s', r'.\source_files', '-d',
                                                                     r'.\destination_for_txt', '-x', '.txt'])
        copy_files_with_spec_extension(source, destination, extension)
        self.assertEqual(['text1.txt'], os.listdir(os.path.dirname(r'.\destination_for_txt\.')))
        shutil.rmtree(r'.\destination_for_txt\.')

    def test_selective_copy_jpg_files(self):
        source, destination, extension = get_parameters_with_parser(['-s', r'.\source_files', '-d',
                                                                     r'.\destination_for_jpg', '-x', '.jpg'])
        copy_files_with_spec_extension(source, destination, extension)
        self.assertEqual(['picture1.jpg', 'picture2.jpg'], os.listdir(os.path.dirname(r'.\destination_for_jpg\.')))
        shutil.rmtree(r'.\destination_for_jpg\.')


if __name__ == '__main__':
    unittest.main()
