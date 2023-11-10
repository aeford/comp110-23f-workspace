"""Test my zip function."""
__author__ = "730566761"


from lessons.zip import zip


def test_different_lengths():
    """If lists are different lengths return empty dictionary."""
    test_key: list[str] = ["happy", "chill"]
    test_value: list[int] = [1, 2, 3, 4]
    assert zip(test_key, test_value) == {}


def test_list_length_1():
    """Testing on a list with one element."""
    test_key: list[str] = ["happy"]
    test_values: list[int] = [24]
    assert zip(test_key, test_values) == {"happy": 24}


def test_same_length():
    """Testing on lists with the same length."""
    test_key: list[str] = ["happy", "cool"]
    test_value: list[int] = [1, 2]
    assert zip(test_key, test_value) == {"happy": 1, "cool": 2}