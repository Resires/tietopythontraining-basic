import unittest
from fibonacci import fib


class TestFibonacciFunction(unittest.TestCase):

    def test_wrong_type_input(self):
        with self.assertRaises(TypeError):
            fib('string')

    def test_missing_type_input(self):
        with self.assertRaises(TypeError):
            fib(None)

    def test_correct_result(self):
        self.assertEqual(fib(5), 5)

    def test_incorrect_result(self):
        self.assertNotEqual(fib(5), 6)

    def test_negative_input(self):
        self.assertFalse(fib(-1))

    def test_fibonacci_property(self):
        self.assertEqual(fib(10) + fib(11), fib(12))


if __name__ == '__main__':
    unittest.main()
