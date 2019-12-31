import os
import shutil
import tempfile
import unittest
from filling_in_the_gaps import get_parameters_with_parser, get_numbered_file_names_with_prefix, \
    rename_files_with_filling_gaps, insert_gap_into_numbered_files, execute_script

FILE_NAMES_AND_CONTENT = {'spam001.txt': 'File 1', 'spam002.txt': 'File 2', 'spam005.txt': 'File 5',
                          'spam006.txt': 'File 6',
                          'spam_without_number.txt': 'This file is needed to test if prefix without number are '
                                                     'eliminated.'}


class TestFillingInTheGapsNoFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_get_numbered_file_names_with_prefix(self):
        self.assertEqual([], get_numbered_file_names_with_prefix(self.test_dir, 'spam'))

    def test_rename_files_with_filling_gaps(self):
        rename_files_with_filling_gaps(self.test_dir, 'spam')
        self.assertEqual([], os.listdir(self.test_dir))

    def test_filling_in_the_gaps(self):
        parameters = get_parameters_with_parser(['-p', 'spam'])
        file_prefix = parameters[0]
        rename_files_with_filling_gaps(self.test_dir, file_prefix)
        self.assertEqual([], os.listdir(self.test_dir))

    def test_insert_gap_into_numbered_files(self):
        files_localisation, file_prefix, gap_position_for_insert, gap_length_for_insert \
            = get_parameters_with_parser(['-p', 'self.test_dir', '-f' 'spam', '-g', '3', '-l', '10'])
        rename_files_with_filling_gaps(self.test_dir, file_prefix)
        insert_gap_into_numbered_files(self.test_dir, file_prefix, gap_position_for_insert, gap_length_for_insert)
        self.assertEqual([], os.listdir(self.test_dir))

    def test_execute_script_removing_gap(self):
        execute_script(['-p', self.test_dir, '-f', 'spam'])
        self.assertEqual([], os.listdir(self.test_dir))

    def test_execute_script_creating_gap(self):
        execute_script(['-p', self.test_dir, '-f', 'spam', '-g', '3', '-l', '10'])
        self.assertEqual([], os.listdir(self.test_dir))


class TestFillingInTheGaps(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        os.mkdir(os.path.join(self.test_dir, 'spam001'))  # This directory should not be taken during file renaming.
        for file_name, file_content in FILE_NAMES_AND_CONTENT.items():
            with open(os.path.join(self.test_dir, file_name), 'w') as f:
                f.write(file_content)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_get_parameters_with_parser(self):
        self.assertEqual(('.', 'spam', 3, 0), get_parameters_with_parser([]))
        self.assertEqual(('self.test_dir', 'spam', 3, 10), get_parameters_with_parser(['-p', 'self.test_dir', '-f',
                                                                                       'spam', '-g', '3', '-l', '10']))

    def test_get_numbered_file_names_with_prefix(self):
        self.assertEqual([{'extension': '.txt', 'number': '001'}, {'extension': '.txt', 'number': '002'},
                          {'extension': '.txt', 'number': '005'}, {'extension': '.txt', 'number': '006'}],
                         get_numbered_file_names_with_prefix(self.test_dir, 'spam'))

    def test_rename_files_with_filling_gaps(self):
        rename_files_with_filling_gaps(self.test_dir, 'spam')
        self.assertEqual(['spam001', 'spam001.txt', 'spam002.txt', 'spam003.txt', 'spam004.txt',
                          'spam_without_number.txt'],
                         os.listdir(self.test_dir))

    def test_filling_in_the_gaps(self):
        parameters = get_parameters_with_parser(['-p', 'spam'])
        file_prefix = parameters[0]
        rename_files_with_filling_gaps(self.test_dir, file_prefix)
        self.assertEqual(['spam001', 'spam001.txt', 'spam002.txt', 'spam003.txt', 'spam004.txt',
                          'spam_without_number.txt'],
                         os.listdir(self.test_dir))

    def test_insert_gap_into_numbered_files(self):
        files_localisation, file_prefix, gap_position_for_insert, gap_length_for_insert \
            = get_parameters_with_parser(['-p', 'self.test_dir', '-f' 'spam', '-g', '3', '-l', '10'])
        rename_files_with_filling_gaps(self.test_dir, file_prefix)
        insert_gap_into_numbered_files(self.test_dir, file_prefix, gap_position_for_insert, gap_length_for_insert)
        self.assertEqual(['spam001', 'spam001.txt', 'spam002.txt', 'spam013.txt', 'spam014.txt',
                          'spam_without_number.txt'],
                         os.listdir(self.test_dir))

    def test_execute_script_removing_gap(self):
        execute_script(['-p', self.test_dir, '-f', 'spam'])
        self.assertEqual(['spam001', 'spam001.txt', 'spam002.txt', 'spam003.txt', 'spam004.txt',
                          'spam_without_number.txt'], os.listdir(self.test_dir))

    def test_execute_script_creating_gap(self):
        execute_script(['-p', self.test_dir, '-f', 'spam', '-g', '3', '-l', '10'])
        self.assertEqual(['spam001', 'spam001.txt', 'spam002.txt', 'spam015.txt', 'spam016.txt',
                          'spam_without_number.txt'], os.listdir(self.test_dir))


if __name__ == '__main__':
    unittest.main()
