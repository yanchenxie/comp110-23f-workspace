"""File to define Bear class"""

class Bear:
    
    age: int
    hunger_score: int

    def __init__(self, input_age: int = 0, input_hunger_score: int = 0) -> None:
        """Constructs a bear."""
        self.age = input_age
        self.hunger_score = input_hunger_score 
    
    def one_day(self):
        return None