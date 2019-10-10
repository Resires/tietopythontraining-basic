import unittest
from numbers_filter import strings_list_to_integers_list


class TestNumbersFilter(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(strings_list_to_integers_list(['2', '0', '8', '3'], range(3)), [8, 3])

    def test_redundant_elements(self):
        """Additional '2' should be removed twice, but additional '8' should stay because it is out of range"""
        self.assertEqual(strings_list_to_integers_list(['2', '0', '8', '3', '2', '8'], range(3)), [8, 3, 8])


if __name__ == '__main__':
    unittest.main()
