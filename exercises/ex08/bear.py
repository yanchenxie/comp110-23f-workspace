"""File to define Bear class."""

__author__ = "730233103"


class Bear:
    """Bear class."""
    
    age: int
    hunger_score: int

    def __init__(self, input_age: int = 0, input_hunger_score: int = 0) -> None:
        """Constructs a bear."""
        self.age = input_age
        self.hunger_score = input_hunger_score 
    
    def one_day(self):
        """Increasing bear age."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increase hunger score when bear eat fish."""
        self.hunger_score += num_fish