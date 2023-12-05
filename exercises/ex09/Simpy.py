"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730566761"


class Simpy:
    """Simpy Class."""
    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]) -> None:
        """Class constructor to instantianize variables."""
        self.values = values
        return None
    
    def __str__(self) -> str:
        """Converts the Simpy object to a string displaying values."""
        output: str = f"Simpy({self.values})"
        return output
    
    def fill(self, list_val: float, number_vals: int) -> None:
        """Fill Simpy values with specific number of repeating values."""
        self.values = [list_val] * number_vals
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in values attribute with range of values."""
        assert step != 0
        val = start
        while val != stop:
            self.values.append(val)
            val += step

    def sum(self) -> float:
        """Compute and return sum of all items in values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add Simpy + Simpy or Simpy + float."""
        idx: int = 0
        new_values: list[float] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            while idx < len(self.values):
                new_values.append(self.values[idx] + rhs.values[idx])
                idx += 1
        else:
            while idx < len(self.values):
                new_values.append(self.values[idx] + rhs)  # type: ignore
                idx += 1
        new_simpy: Simpy = Simpy(new_values)
        return new_simpy
            
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponent between Simpy ** Simpy or Simpy ** float."""
        idx: int = 0
        new_values: list[float] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            while idx < len(self.values):
                new_values.append(self.values[idx] ** rhs.values[idx])
                idx += 1
        else:
            while idx < len(self.values):
                new_values.append(self.values[idx] ** rhs)  # type: ignore
                idx += 1
        new_simpy: Simpy = Simpy(new_values)
        return new_simpy
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:  # type: ignore
        """List of bool if values are equal to eachother for float or Simpy."""
        idx: int = 0
        new_list: list[bool] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            while idx < len(self.values):
                if self.values[idx] == rhs.values[idx]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                idx += 1
        else:
            while idx < len(self.values):
                if self.values[idx] == rhs:
                    new_list.append(True)
                else:
                    new_list.append(False)
                idx += 1
        return new_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:  # type: ignore
        """List of bool if values are greater than on another for float or Simpy."""
        idx: int = 0
        new_list: list[bool] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            while idx < len(self.values):
                if self.values[idx] > rhs.values[idx]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                idx += 1
        else:
            while idx < len(self.values):
                if self.values[idx] > rhs:  # type: ignore
                    new_list.append(True)
                else:
                    new_list.append(False)
                idx += 1
        return new_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:  # type: ignore
        """Only shows numbers that meet requirements."""
        if type(rhs) is list[bool]:
            for element in rhs:
                if element is False:
                    rhs.pop(element)