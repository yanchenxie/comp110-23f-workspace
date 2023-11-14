"""Practicing importing from other modules"""

from lessons import my_functions 

from lessons.my_functions import addition

print(my_functions.addition(1,2))

print(my_functions.my_variable)

