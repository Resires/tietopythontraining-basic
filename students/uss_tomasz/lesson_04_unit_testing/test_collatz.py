import pytest
from collatz import collatz


def test_wrong_type_of_input():
    with pytest.raises(TypeError):
        collatz('string_value')


def test_input_value_8():
    assert collatz(8) == 4


def test_input_value_5():
    assert collatz(5) == 16
