"""
missing tasks :
py.test unit tests better way to test (it's easier than you think)
"""
import unittest
from collatz import collatz


class TestCollatzFunction(unittest.TestCase):

    def test_wrong_type_of_input(self):
        with self.assertRaises(TypeError):
            collatz('string_value')

    def test_input_value_4(self):
        self.assertEqual(collatz(8), 4)

    def test_input_value_16(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
