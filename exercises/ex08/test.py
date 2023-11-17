"""File to define River class."""

__author__ = "730553197"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class and information."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Limits age of Fish and Bear."""
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears
        return None

    def remove_fish(self, amount: int):
        """Remove fish from River."""
        for i in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Modify amount of fish Bear will eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checks hunger_score of Bear."""
        survive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                survive_bears.append(bear)
        self.bears = survive_bears
        return None

    def repopulate_fish(self):
        """Modify number of fish born."""
        n: int = len(self.fish)
        new: int = ((n // 2) * 4)
        for i in range(0, new):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Modify number of bears born."""
        n: int = len(self.bears)
        new: int = (n // 2)
        for i in range(0, new):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Prints descriptions of day, fish, and bear."""
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
        """Changes one_river_day function to a week."""
        while self.day < 7:
            self.one_river_day()