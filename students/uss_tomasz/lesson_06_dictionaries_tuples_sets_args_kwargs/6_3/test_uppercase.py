import unittest
from uppercase import capitalize


class TestUppercase(unittest.TestCase):
    def test_lower_case_word(self):
        self.assertEqual(capitalize('word'), 'Word')

    def test_already_capitalized(self):
        self.assertEqual(capitalize('Word'), 'Word')

    def test_empty_word(self):
        self.assertEqual(capitalize(''), '')

    def test_wrong_input(self):
        self.assertEqual(capitalize(1234), None)


if __name__ == '__main__':
    unittest.main()
