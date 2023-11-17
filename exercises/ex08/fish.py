"""File to define Fish class."""

__author__ = "730233103"


class Fish:
    """Fish Class."""
    
    age: int

    def __init__(self, input_age: int = 0):
        """Constructor making a fish."""
        self.age = input_age
        return None
    
    def one_day(self):
        """Increaisng fish age."""
        self.age += 1
        return None