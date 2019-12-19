import os
import unittest
from filling_in_the_gaps import get_parameters_with_parser, get_numbered_file_names_with_prefix, \
    rename_files_with_filling_gaps, insert_gap_into_numbered_files

FILE_NAMES_AND_CONTENT = {'spam001.txt': 'File 1', 'spam002.txt': 'File 2', 'spam005.txt': 'File 5',
                          'spam006.txt': 'File 6',
                          'spam_without_number.txt': 'This file is needed to test if prefix without number are '
                                                     'eliminated.'}


class TestFillingInTheGaps(unittest.TestCase):
    def setUp(self):
        for file_name, file_content in FILE_NAMES_AND_CONTENT.items():
            with open(file_name, 'w') as f:
                f.write(file_content)

    def tearDown(self):
        for file_name in os.listdir(os.curdir):
            if file_name.startswith('spam'):
                os.remove(file_name)

    def test_get_parameters_with_parser(self):
        self.assertEqual(('spam', 3, 10), get_parameters_with_parser(['-p', 'spam', '-g', '3', '-l', '10']))

    def test_get_numbered_file_names_with_prefix(self):
        self.assertEqual([{'extension': '.txt', 'number': '001'}, {'extension': '.txt', 'number': '002'},
                          {'extension': '.txt', 'number': '005'}, {'extension': '.txt', 'number': '006'}],
                         get_numbered_file_names_with_prefix('spam'), )

    def test_rename_files_with_filling_gaps(self):
        rename_files_with_filling_gaps('spam')
        self.assertEqual(os.listdir(os.curdir),
                         ['filling_in_the_gaps.py', 'spam001.txt', 'spam002.txt', 'spam003.txt', 'spam004.txt',
                          'spam_without_number.txt', 'test_filling_in_the_gaps.py'])

    def test_filling_in_the_gaps(self):
        parameters = get_parameters_with_parser(['-p', 'spam'])
        file_prefix = parameters[0]
        print(file_prefix, type(file_prefix))
        rename_files_with_filling_gaps(file_prefix)
        self.assertEqual(os.listdir(os.curdir),
                         ['filling_in_the_gaps.py', 'spam001.txt', 'spam002.txt', 'spam003.txt', 'spam004.txt',
                          'spam_without_number.txt', 'test_filling_in_the_gaps.py'])

    def test_insert_gap_into_numbered_files(self):
        file_prefix, gap_position_for_insert, gap_length_for_insert = get_parameters_with_parser(['-p', 'spam', '-g',
                                                                                                  '3', '-l', '10'])
        rename_files_with_filling_gaps(file_prefix)
        insert_gap_into_numbered_files(file_prefix, gap_position_for_insert, gap_length_for_insert)
        self.assertEqual(os.listdir(os.curdir),
                         ['filling_in_the_gaps.py', 'spam001.txt', 'spam002.txt', 'spam013.txt', 'spam014.txt',
                          'spam_without_number.txt', 'test_filling_in_the_gaps.py'])


if __name__ == '__main__':
    unittest.main()
