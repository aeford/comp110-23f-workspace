"""Quiz 02 Value Exists Practice."""
__author__ = "730566761"

def value_exists(my_dict: dict[str, int], value: int) -> bool:
    exists: bool = False
    for elem in my_dict:
        if my_dict[elem] == value:
            exists = True
    return exists