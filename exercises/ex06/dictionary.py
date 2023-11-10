"""EX06 - Dictionary Functions."""
__author__ = "730566761"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert the keys and values."""
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            raise KeyError("There are multiple of a key!")
        inverted_dict[value] = key
    return (inverted_dict)


def favorite_color(colors: dict[str, str]) -> str:
    """Find the most common color in a list."""
    new_color: dict[str, int] = {}
    for key, value in colors.items():
        if value in new_color:
            new_color[value] += 1
        else:
            new_color[value] = 1
    favorite_color = max(new_color)
    return favorite_color


def count(count_list: list[str]) -> dict[str, int]:
    """Count of the number of times a value appears in the input list."""
    new_dict: dict[str, int] = {}
    for item in count_list:
        if item in new_dict:
            new_dict[item] = new_dict[item] + 1
        else:
            new_dict[item] = 1
    return new_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    result_dict: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in result_dict:
            result_dict[first_letter] = []
        result_dict[first_letter].append(word)
    return result_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update attendance log."""
    if day not in attendance:
        attendance[day] = []
    if student not in attendance[day]:
        attendance[day].append(student)
    return attendance