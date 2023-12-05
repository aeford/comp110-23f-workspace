"""File to define River class."""
__author__ = "730566761"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Represents the river."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: list[Bear] = [Bear() for _ in range(num_bears)]
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of fish and bears."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self, num_fish: int):
        """Removes fish as bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
            else:
                bear.eat(0)
        return None
    
    def check_hunger(self):
        """Checks hunger score and removes bear."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None
        
    def repopulate_fish(self):
        """Increase fish as they repopulate."""
        offspring = (len(self.fish) // 2) * 4
        self.fish.extend([Fish() for _ in range(offspring)])
        return None
    
    def repopulate_bears(self):
        """Increase bears as they repopulate."""
        offspring = (len(self.bears)) // 2
        self.bears.extend([Bear() for _ in range(offspring)])
        return None
    
    def view_river(self):
        """View river day and animal population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
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
        """River week."""
        for _ in range(6):
            self.one_river_day
        return None
    
    def remove_fish(self, amount: int):
        """Removes fish from river."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
        return None
