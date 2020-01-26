import os
import shutil
import tempfile
from regex_search import parse_args, get_file_names_list, find_regex_in_txt_files, execute_script


class TestRegexSearchNoFiles:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()

    def teardown_method(self):
        try:
            shutil.rmtree(self.test_dir)
        except Exception as e:
            print('Impossible to remove: ' + str(e))

    def test_get_file_names_list(self):
        assert get_file_names_list(self.test_dir) == []

    def test_find_regex_in_txt_files(self):
        assert find_regex_in_txt_files(r'\d{3}', self.test_dir) == {}

    def test_execute_script(self):
        assert execute_script(['-r', r'\d{3}', '-p', self.test_dir]) == ''


class TestRegexSearchNoFilesDefaultDir:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def teardown_method(self):
        # Change current working directory one level up before deleting it:
        os.chdir(os.path.join(os.getcwd(), ".."))
        try:
            shutil.rmtree(self.test_dir)
        except Exception as e:
            print('Impossible to remove: ' + str(e))

    def test_get_file_names_list(self):
        assert get_file_names_list('.') == []

    def test_find_regex_in_txt_files(self):
        assert find_regex_in_txt_files(r'\d{3}', '.') == {}

    def test_execute_script(self):
        assert execute_script(['-r', r'\d{3}']) == ''


class TestRegexSearch:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
        with open(os.path.join(self.test_dir, 'text1.txt'), 'w') as f:
            f.write('Write a program that opens all .txt files in a folder 123')
        with open(os.path.join(self.test_dir, 'text2.txt'), 'w') as f:
            f.write('Program searches for any line that matches a user-supplied regular expression 456 789')
        with open(os.path.join(self.test_dir, 'text3.txt'), 'w') as f:
            f.write('666 The results should be printed to the screen 997')

    def teardown_method(self):
        try:
            shutil.rmtree(self.test_dir)
        except Exception as e:
            print('Impossible to remove: ' + str(e))

    def test_parse_args(self):
        assert parse_args([]) == (r'\d{3}', '.', 0, 'regex_search_log.txt')
        assert parse_args(['-r', r'\w', '-p', r'First_lvl_dir\Second_lvl_dir', '-v', '1',
                           '-n', 'logger.txt']) == (r'\w', r'First_lvl_dir\Second_lvl_dir', 1, 'logger.txt')

    def test_get_file_names_list(self):
        assert get_file_names_list(self.test_dir) == ['text1.txt', 'text2.txt', 'text3.txt']

    def test_find_regex_in_txt_files(self):
        assert find_regex_in_txt_files(r'\d{3}', self.test_dir) == {'text1.txt': ['123'], 'text2.txt': ['456', '789'],
                                                                    'text3.txt': ['666', '997']}
        assert find_regex_in_txt_files(r'\d{4}', self.test_dir) == {'text1.txt': [], 'text2.txt': [], 'text3.txt': []}

    def test_execute_script(self):
        assert execute_script(['-r', r'\d{3}', '-p',
                               self.test_dir]) == 'In file named "text1.txt" there were following occurrence: 123 \n' \
                                                  'In file named "text2.txt" there were following occurrence: 456 \n' \
                                                  'In file named "text2.txt" there were following occurrence: 789 \n' \
                                                  'In file named "text3.txt" there were following occurrence: 666 \n' \
                                                  'In file named "text3.txt" there were following occurrence: 997 \n'

    def test_verbosity_deactivation(self):
        # default verbosity => lvl 0 => no messages
        execute_script(['-r', r'\d{3}',
                        '-p', self.test_dir,
                        '-n', 'regex_search_log_1.txt'])
        with open(os.path.join(self.test_dir, 'regex_search_log_1.txt'), 'r') as f:
            assert f.read() == ""

        # verbosity lvl 1 => messages are errors and critical
        execute_script(['-r', r'\d{3}',
                        '-p', self.test_dir,
                        '-v', '1',
                        '-n', 'regex_search_log_2.txt'])
        with open(os.path.join(self.test_dir, 'regex_search_log_2.txt'), 'r') as f:
            assert f.read() == "ERROR - Following file has a visible ERROR messages\n" \
                               "CRITICAL - Following file has a visible CRITICAL messages\n"


class TestRegexSearchDefaultDir:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)
        with open('text1.txt', 'w') as f:
            f.write('Write a program that opens all .txt files in a folder 123')
        with open('text2.txt', 'w') as f:
            f.write('Program searches for any line that matches a user-supplied regular expression 456 789')
        with open('text3.txt', 'w') as f:
            f.write('666 The results should be printed to the screen 997')

    def teardown_method(self):
        # Change current working directory one level up before deleting it:
        os.chdir(os.path.join(os.getcwd(), ".."))
        try:
            shutil.rmtree(self.test_dir)
        except Exception as e:
            print('Impossible to remove: ' + str(e))

    def test_get_file_names_list(self):
        assert get_file_names_list('.') == ['text1.txt', 'text2.txt', 'text3.txt']

    def test_find_regex_in_txt_files(self):
        assert find_regex_in_txt_files(r'\d{3}', '.') == {'text1.txt': ['123'], 'text2.txt': ['456', '789'],
                                                          'text3.txt': ['666', '997']}
        assert find_regex_in_txt_files(r'\d{4}', '.') == {'text1.txt': [], 'text2.txt': [], 'text3.txt': []}

    def test_execute_script(self):
        assert execute_script(['-r', r'\d{3}']) == 'In file named "text1.txt" there were following occurrence: 123 \n' \
                                                   'In file named "text2.txt" there were following occurrence: 456 \n' \
                                                   'In file named "text2.txt" there were following occurrence: 789 \n' \
                                                   'In file named "text3.txt" there were following occurrence: 666 \n' \
                                                   'In file named "text3.txt" there were following occurrence: 997 \n'
