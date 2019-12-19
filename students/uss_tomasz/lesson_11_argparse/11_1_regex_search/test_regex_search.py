import os
import unittest
from regex_search import parse_args, get_file_names_list, find_regex_in_txt_files


class TestRegexSearch(unittest.TestCase):
    def setUp(self):
        with open('text1.txt', 'w') as f:
            f.write('Write a program that opens all .txt files in a folder 123')
        with open('text2.txt', 'w') as f:
            f.write('Program searches for any line that matches a user-supplied regular expression 456 789')
        with open('text3.txt', 'w') as f:
            f.write('666 The results should be printed to the screen 997')

    def tearDown(self):
        os.remove('text1.txt')
        os.remove('text2.txt')
        os.remove('text3.txt')

    def test_parse_args(self):
        self.assertEqual(r'\d{3}', parse_args(['-r', r'\d{3}']))

    def test_get_file_names_list(self):
        self.assertEqual(['text1.txt', 'text2.txt', 'text3.txt'], get_file_names_list())

    def test_finding_regex(self):
        self.assertEqual({'text1.txt': ['123'], 'text2.txt': ['456', '789'], 'text3.txt': ['666', '997']},
                         find_regex_in_txt_files(r'\d{3}'),)

    def test_regex_search_with_argparse(self):
        self.assertEqual({'text1.txt': ['123'], 'text2.txt': ['456', '789'], 'text3.txt': ['666', '997']},
                         find_regex_in_txt_files(parse_args(['-r', r'\d{3}'])))


if __name__ == '__main__':
    unittest.main()
