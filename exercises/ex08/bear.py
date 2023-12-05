"""File to define Bear class."""
__author__ = "730566761"


class Bear:
    """Represents bears in the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initiate variables."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        """Increase age each day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increase hunger score by amount of fish eaten."""
        self.hunger_score += num_fish
        return None