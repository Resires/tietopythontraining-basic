import pytest
from fibonacci import fib


def test_wrong_type_input():
    with pytest.raises(TypeError):
        fib('string')


def test_missing_type_input():
    with pytest.raises(TypeError):
            fib(None)


def test_correct_result():
    assert fib(5) == 5


def test_incorrect_result():
    assert fib(5) != 6


def test_negative_input():
    assert not fib(-1)


def test_fibonacci_property():
    assert fib(10) + fib(11) == fib(12)
