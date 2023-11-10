"""Combining two lists into a dictionary."""
__author__ = "730566761"


def zip(key_list: list[str], value_list: list[int]) -> dict[str, int]:
    """Given keys and values list, create dictionary."""
    my_dict: dict[str, int] = {}
    if len(key_list) != len(value_list):
        return my_dict
    for i in range(len(key_list)):
        my_dict[key_list[i]] = value_list[i]
    return my_dict