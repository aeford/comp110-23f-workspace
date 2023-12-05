"""Dictionary related utility functions."""

__author__ = "730566761"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(data: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in data:
        #  append every value under key header.
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table as a list of rows into a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table wiht on the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for key in table.keys():
        value = table[key]
        first_vals = []
        for item in range(min(rows, len(value))):
            first_vals.append(value[item])
        result[key] = first_vals
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset fo the original columns."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = table[name]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result


def count(vals: list[str]) -> dict[str, int]:
    """Each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    idx: int = 0
    for name in vals:
        if name in result:
            result[vals[idx]] += 1
            idx += 1
        else:
            result[vals[idx]] = 1
            idx += 1
    return result