"""CQ07 Point Class."""

from __future__ import annotations

__author__ = "730233103"


class Point:
    """Attributes of new class called Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0): 
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scale by method through mutating point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Scale by method through making new point."""
        x = self.x * factor
        y = self.y * factor
        new_point: Point = Point(x, y)
        return new_point
    
    def __str__(self) -> str:
        """Printing out x and y value of points."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operator overload."""
        x = self.x * factor
        y = self.y * factor
        new_point: Point = Point(x, y)
        return new_point

    def __add__(self, factor: int | float) -> Point:
        """Addition operator overload."""    
        x = self.x + factor
        y = self.y + factor
        new_point: Point = Point(x, y)
        return new_point
    

my_point: Point = Point(1.0, 2.0)
# print(my_point)

new_point: Point = my_point + 3.0
print(new_point)

        
