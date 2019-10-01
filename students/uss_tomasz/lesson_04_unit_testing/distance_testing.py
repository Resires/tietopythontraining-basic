import unittest
from distance import distance


class TestDistanceFunction(unittest.TestCase):
    def test_wrong_type_calling_on_none(self):
        with self.assertRaises(TypeError):
            distance(None, None, None, None)

    def test_wrong_type_calling_on_string(self):
        with self.assertRaises(TypeError):
            distance('string1', 'string2', 'string3', 'string4')

    def test_zero_length(self):
        self.assertEqual(distance(0, 1, 0, 1), 0)

    def test_negative_coordinates(self):
        self.assertEqual(distance(-1, -1, -4, -5), 5)

    def test_only_vertical_distance(self):
        self.assertEqual(distance(1, 1, 1, 4), 3)

    def test_only_horizontal_distance(self):
        self.assertEqual(distance(1, 1, 4, 1), 3)

    def test_difference_on_both_coordinates(self):
        self.assertAlmostEqual(distance(1, 2, 3, 4), 2.8284271247461903)

    def test_order_of_operation(self):
        self.assertEqual(distance(1, 2, 3, 4), distance(4, 3, 2, 1))


if __name__ == '__main__':
    unittest.main()
