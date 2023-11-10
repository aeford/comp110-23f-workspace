"""EX07 - 'dict' Unit Tests."""
__author__ = "730566761"


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_length_1():
    """Tests invert of keys and values for a dictionary of length=1."""
    test_dict: dict[str, str] = {"happy": "good"}
    assert invert(test_dict) == {"good": "happy"}


def test_invert_empty_dict():
    """Returns an empty dictionary when given an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_length_multiple():
    """For longer dictionary, invert is correct."""
    test_dict: dict[str, str] = {"happy": "good", "cool": "fun", "great": "awesome"}
    assert invert(test_dict) == {"good": "happy", "fun": "cool", "awesome": "great"}


def test_invert_keyerror():
    """For multiples of a key in a dictionary, raise KeyError."""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(test_dict)


def test_color_tie():
    """If there is a tie, return the first color in the dictionary."""
    test_dict: dict[str, str] = {"chris": "green", "adam": "blue", "amanda": "blue", "chelsea": "green"}
    assert favorite_color(test_dict) == "green"


def test_color_empty():
    """If given an empty dictionary, return a ValueError."""
    with pytest.raises(ValueError):
        test_dict: dict[str, str] = {}
        favorite_color(test_dict)


def test_color_max():
    """Finds the most common color in a list."""
    test_dict: dict[str, str] = {"chris": "green", "sam": "green", "charity": "blue", "connie": "green"}
    assert favorite_color(test_dict) == "green"


def test_count_length_1():
    """Given a list of length=1, return the value appears once."""
    test_list: list[str] = ["happy"]
    assert count(test_list) == {'happy': 1}


def test_count_empty():
    """Given an empty list, return an empty dictionary."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_longer_list():
    """Given a longer list, returns dictionary of appropriate count."""
    test_list: list[str] = ["happy", "done", "check", "check", "check", "done", "great"]
    assert count(test_list) == {"happy": 1, "done": 2, "check": 3, "great": 1}


def test_alphabetizer_length_1():
    """Given a list of length 1, return dictionary of length 1."""
    test_list: list[str] = ["cat"]
    assert alphabetizer(test_list) == {'c': ['cat']}


def test_alphabetizer_empty():
    """Given an empty list, return an empty dictionary."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_alphabetizer_multiple_keys():
    """Given a list with multiple unique starting letters, return a dictionary where a value is a list of words."""
    test_list: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(test_list) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_update_attendance_regular():
    """Given an attendance log, update the log accordingly."""
    test_attendance: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(test_attendance, "Tuesday", "Kaleb") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Kaleb"]}


def test_update_attendance_empty():
    """Given an empty dictionary and empty strings, return an empty dictionary."""
    test_attendance: dict[str, list[str]] = {}
    assert update_attendance(test_attendance, "", "") == {"": [""]}


def test_update_attendance_no_update():
    """Given dictionary and empty strings, don't update the attendance log."""
    test_attendance: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(test_attendance, "", "") == {"": [""], "Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}