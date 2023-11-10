"""Odd and Even part 2"""

def odd_and_even(og: list[int]) -> list[int]: #type: ignore
    new_list: list[int] = []
    i: int = 0
    while i < len(og):
        if i % 2 == 0 and og[i] % 2 == 1:
            new_list.append(og[i])
            return new_list
        i += 1
