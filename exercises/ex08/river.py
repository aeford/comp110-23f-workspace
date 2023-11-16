"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: list[Bear] = [Bear() for _ in range(num_bears)]
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        
        return None
    
    def check_hunger(self):
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
    
    def view_river(self):
        num_fish = len(self.fish)
        num_bears = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {num_fish}")
        print(f"Bear population: {num_bears}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        for _ in range(7):
            self.one_river_day
        return None
    
    def remove_fish(self, amount: int):
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
        return None
