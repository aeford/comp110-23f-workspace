"""Quiz 02 Practice."""
__author__ = "730566761"

def odd_and_even(list_1: list[int]) -> list[int]: #type: ignore
    "Returns new list with elements that are odd and have an even index."
    i: int = 0
    list_2: list[int] = []

    while i < len(list_1):
        if i % 2 == 0 and list_1[i] % 2 == 1:
            list_2.append(list_1[i])
            return list_2
        i += 1