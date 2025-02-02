"""File to define River class."""

__author__ = "730233103"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River Class."""
    
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
        """See what are the ages of bears and fishes."""
        survive_bear: list[Bear] = []
        survive_fish: list[Fish] = []
        for bears in self.bears:
            if bears.age <= 5:
                survive_bear.append(bears)

        for fish in self.fish:
            if fish.age <= 3:
                survive_fish.append(fish)     
        self.bears = survive_bear
        self.fish = survive_fish   
        return None

    def bears_eating(self):
        """Bears eating and removing fish from river."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bears.eat(3)
        return None
    
    def check_hunger(self):
        """Checks and remove starving bears."""
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(bear)
        self.bears = full_bears
        return None
        
    def repopulate_fish(self):
        """Increases number of fish in the river."""
        current_amount_fish: int = len(self.fish)
        amount_pairs_fish: int = current_amount_fish // 2
        new_fishes: int = amount_pairs_fish * 4
        for x in range(0, new_fishes):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Increases number of bears in the river."""
        current_amount_bears: int = len(self.bears)
        amount_pairs_bears: int = current_amount_bears // 2
        new_bears: int = amount_pairs_bears * 1
        for x in range(0, new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Print description of river on day x."""
        output: str = f"~~~ Day {self.day}: ~~~\n"
        output += f"Fish population: {len(self.fish)}\n"
        output += f"Bear population: {len(self.bears)}"
        print(output)
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
        """Runs one_river_day 7 times to simulate a week."""
        while self.day < 7:
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Revemoe amount many Fish from River."""
        remove_count: int = 0
        while remove_count < amount:
            self.fish.pop(0)
            remove_count += 1
        return None