import unittest
from comma_code import list_to_string


class TestCommaCode(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(list_to_string([]), '')

    def test_one_element(self):
        self.assertEqual(list_to_string(['apples']), 'apples')

    def test_two_elements(self):
        self.assertEqual(list_to_string(['apples', 'bananas']), 'apples and bananas')

    def test_typical(self):
        self.assertEqual(list_to_string(['apples', 'bananas', 'tofu', 'cats']), 'apples, bananas, tofu and cats')

    def test_integers(self):
        self.assertEqual(list_to_string([1, 3]), '1 and 3')

    def test_none_arguments(self):
        self.assertEqual(list_to_string([None, None]), 'None and None')


if __name__ == '__main__':
    unittest.main()
