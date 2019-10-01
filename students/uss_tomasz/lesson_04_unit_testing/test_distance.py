import pytest
from distance import distance


def test_wrong_type_calling_on_none():
    with pytest.raises(TypeError):
        distance(None, None, None, None)


def test_wrong_type_calling_on_string():
    with pytest.raises(TypeError):
        distance('string1', 'string2', 'string3', 'string4')


def test_zero_length():
    assert distance(1, 2, 1, 2) == 0


def test_negative_coordinates():
    assert distance(-1, -1, -4, -5) == 5


def test_only_vertical_distance():
    assert distance(1, 1, 1, 5) == 4


def test_only_horizontal_distance():
    assert distance(1, 1, 5, 1) == 4


def test_difference_on_both_coordinates():
    assert pytest.approx(distance(1, 2, 3, 4), 2.8284271247461903)


def test_order_of_operations():
    assert distance(1, 2, 3, 4) == distance(4, 3, 2, 1)


'''
class TestDistanceFunction(unittest.TestCase):
    def test_wrong_type_calling_on_none(self):
        with self.assertRaises(TypeError):
            distance(None, None, None, None)

    def test_wrong_type_calling_on_string(self):
        with self.assertRaises(TypeError):
            distance('string1', 'string2', 'string3', 'string4')
'''
