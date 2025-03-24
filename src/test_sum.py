import pytest
from src.sum import custom_sum

def test_empty_list():
    assert custom_sum([]) == 0

def test_single_number():
    assert custom_sum([5]) == 5

def test_positive_numbers():
    assert custom_sum([1, 2, 3, 4, 5]) == 15

def test_negative_numbers():
    assert custom_sum([-1, -2, -3]) == -6

def test_mixed_numbers():
    assert custom_sum([-2, 0, 3, -1, 4]) == 4

def test_large_numbers():
    assert custom_sum([1000000, 2000000, 3000000]) == 6000000

def test_decimal_numbers():
    assert custom_sum([1.5, 2.7, 3.2]) == 7.4

def test_zero():
    assert custom_sum([0, 0, 0]) == 0

def test_single_zero():
    assert custom_sum([0]) == 0

def test_repeated_numbers():
    assert custom_sum([2, 2, 2, 2]) == 8

def test_invalid_input():
    with pytest.raises(TypeError):
        custom_sum("not a list")

def test_list_with_non_numbers():
    with pytest.raises(TypeError):
        custom_sum([1, "2", 3])

def test_none_input():
    with pytest.raises(TypeError):
        custom_sum(None)
