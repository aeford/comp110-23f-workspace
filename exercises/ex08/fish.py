"""File to define Fish class."""
__author__ = "730566761"


class Fish:
    """Represents fish in the river."""

    age: int

    def __init__(self):
        """Initiate variable."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Increase age each day."""
        self.age += 1
        return None