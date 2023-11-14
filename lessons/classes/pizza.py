"""Defining a class"""

from __future__ import annotations

"""
Think of a class definition as a roadmap for objects that belong in the class
"""

class Pizza: 

    #attributes
    # Think of these as the variables each instance of my class will have
    #<name> : <type>
    size : str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        """My constructor"""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf
        # returns a pizza object, no need to return, no need since we are using init
    
    def price(self) -> float:
        """Calculate price of pizza within the pizza type"""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += 0.75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    

    def add_topping(self, num_toppings: int):
        """Add toppings to existing pizza"""
        self.toppings += num_toppings

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza: 
        """Make a new pizza with exisiting pizza's properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    
    def __str__ (self) -> str:
        """Return strings in class"""
        pizza_info: str = f"PIZZA ORDER: size {self.size}, toppings: {self.toppings}, GF: {self.gluten_free}"
        return pizza_info
    

my_pizza: Pizza = Pizza("medium", 3, False)
print(my_pizza)

sals_pizza: Pizza = Pizza("medium", 1, False)
print(sals_pizza)
