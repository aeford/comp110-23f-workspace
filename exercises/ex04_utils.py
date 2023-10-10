"""EX04 - 'list' Utility Functions."""
__author__ = "730566761"


def all(numbers: list[int], number: int) -> bool:
    """Given a list of ints and an int, all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    for n in numbers:
        if n != number:
            return False
    if len(numbers) == 0:
        return False
    return True


def max(numbers: list[int]) -> int:
    """The max function is given a list of ints, max should return the largest in the List."""
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty list")
    largest_number = numbers[0]
    for n in numbers:
        if n > largest_number:
            largest_number = n
    return largest_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    if len(list_1) != len(list_2):
        return False
    for i in range(len(list_2)):
        if list_1[i] != list_2[i]:
            return False
    return True