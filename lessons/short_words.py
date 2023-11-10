"""Short words quiz 02 practice."""
__author__ = "730566761"

def short_words(list_1: list[str]) -> list[str]: #type: ignore
    "Return list of words that are shorter than 5 characters."
    new_list: list[str] = []
    for element in list_1:
        if len(element) < 5:
            new_list.append(element)
        else:
            print(f"{element} is too long!")
    return new_list