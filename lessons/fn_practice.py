"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value of two numbers"""
    if number1 >= number2:
        return number1
    else: # number 1 < number2
        return number2
    
max_number: int = my_max(10,6)
other_max_number: int = my_max(11,3)
print(max_number)