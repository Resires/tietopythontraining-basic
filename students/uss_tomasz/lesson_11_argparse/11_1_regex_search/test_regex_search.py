import os
import shutil
import tempfile
import unittest
from regex_search import parse_args, get_file_names_list, find_regex_in_txt_files, execute_script


class TestRegexSearchNoFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_get_file_names_list(self):
        self.assertEqual([], get_file_names_list(self.test_dir))

    def test_find_regex_in_txt_files(self):
        self.assertEqual({}, find_regex_in_txt_files(r'\d{3}', self.test_dir))

    def test_execute_script(self):
        self.assertEqual('', execute_script(['-r', r'\d{3}', '-p', self.test_dir]))


class TestRegexSearchNoFilesDefaultDir(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def test_get_file_names_list(self):
        self.assertEqual([], get_file_names_list('.'))

    def test_find_regex_in_txt_files(self):
        self.assertEqual({}, find_regex_in_txt_files(r'\d{3}', '.'))

    def test_execute_script(self):
        self.assertEqual('', execute_script(['-r', r'\d{3}']))


class TestRegexSearch(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        with open(os.path.join(self.test_dir, 'text1.txt'), 'w') as f:
            f.write('Write a program that opens all .txt files in a folder 123')
        with open(os.path.join(self.test_dir, 'text2.txt'), 'w') as f:
            f.write('Program searches for any line that matches a user-supplied regular expression 456 789')
        with open(os.path.join(self.test_dir, 'text3.txt'), 'w') as f:
            f.write('666 The results should be printed to the screen 997')

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_parse_args(self):
        self.assertEqual((r'\d{3}', '.'), parse_args([]))
        self.assertEqual((r'\w', r'First_lvl_dir\Second_lvl_dir'),
                         parse_args(['-r', r'\w', '-p', r'First_lvl_dir\Second_lvl_dir']))

    def test_get_file_names_list(self):
        self.assertEqual(['text1.txt', 'text2.txt', 'text3.txt'],
                         get_file_names_list(self.test_dir))

    def test_find_regex_in_txt_files(self):
        self.assertEqual({'text1.txt': ['123'], 'text2.txt': ['456', '789'], 'text3.txt': ['666', '997']},
                         find_regex_in_txt_files(r'\d{3}', self.test_dir),)
        self.assertEqual({'text1.txt': [], 'text2.txt': [], 'text3.txt': []},
                         find_regex_in_txt_files(r'\d{4}', self.test_dir))

    def test_execute_script(self):
        self.assertEqual('In file named "text1.txt" there were following occurrence: 123 \n'
                         'In file named "text2.txt" there were following occurrence: 456 \n'
                         'In file named "text2.txt" there were following occurrence: 789 \n'
                         'In file named "text3.txt" there were following occurrence: 666 \n'
                         'In file named "text3.txt" there were following occurrence: 997 \n',
                         execute_script(['-r', r'\d{3}', '-p', self.test_dir]))


class TestRegexSearchDefaultDir(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)
        with open('text1.txt', 'w') as f:
            f.write('Write a program that opens all .txt files in a folder 123')
        with open('text2.txt', 'w') as f:
            f.write('Program searches for any line that matches a user-supplied regular expression 456 789')
        with open('text3.txt', 'w') as f:
            f.write('666 The results should be printed to the screen 997')

    def test_get_file_names_list(self):
        self.assertEqual(['text1.txt', 'text2.txt', 'text3.txt'], get_file_names_list('.'))

    def test_find_regex_in_txt_files(self):
        self.assertEqual({'text1.txt': ['123'], 'text2.txt': ['456', '789'], 'text3.txt': ['666', '997']},
                         find_regex_in_txt_files(r'\d{3}', '.'),)
        self.assertEqual({'text1.txt': [], 'text2.txt': [], 'text3.txt': []},
                         find_regex_in_txt_files(r'\d{4}', '.'))

    def test_execute_script(self):
        self.assertEqual('In file named "text1.txt" there were following occurrence: 123 \n'
                         'In file named "text2.txt" there were following occurrence: 456 \n'
                         'In file named "text2.txt" there were following occurrence: 789 \n'
                         'In file named "text3.txt" there were following occurrence: 666 \n'
                         'In file named "text3.txt" there were following occurrence: 997 \n',
                         execute_script(['-r', r'\d{3}']))


if __name__ == '__main__':
    unittest.main()
