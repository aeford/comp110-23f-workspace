"""CQ07 - Intro to object Oriented Programming."""
from __future__ import annotations
__author__ = "730566761"


class Point:
    """Class that is a representation of a point on an (x, y) coordinate."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method that belongs to Point class and mutates a Point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Method that belongs to the Point class and creates a new point instead of mutating."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Print x and y in a more readable way."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int) -> Point:
        """Multiply point by a factor."""
        new_point: Point = Point(self.x, self.y) * factor
        return new_point