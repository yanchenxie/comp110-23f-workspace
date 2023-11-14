"""EX04 - Utils."""

__author__ = "730233103"


def all(list_integers: list[int], integer: int) -> bool:
    """Given a list of ints and an int, all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    if len(list_integers) == 0:
        raise ValueError("max() arg is an empty List")
    list_index: int = 0
    return_value: bool = True
    while list_index <= len(list_integers) - 1:
        if integer != list_integers[list_index]:
            return_value = False
        list_index += 1
    return return_value


print(all([1, 1, 1], 2))


def max(list_integers: list[int]) -> int:
    """Given a list of ints, max should return the largest in the List."""
    if len(list_integers) == 0:
        raise ValueError("max() arg is an empty List")
    list_index: int = 1
    max_value: int = list_integers[0]
    while list_index <= len(list_integers) - 1:
        if list_integers[list_index] >= list_integers[list_index - 1] and list_integers[list_index] >= max_value:
            max_value = list_integers[list_index]
        list_index += 1
    return max_value


print(max([3, 5, 3, 4, 1]))


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    if len(list1) == 0 or len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    list1_index: int = 0
    list2_index: int = 0
    return_value: bool = True
    while list1_index <= len(list1) - 1:
        if list2[list1_index] != list1[list1_index]:
            return_value = False
        list1_index += 1

    while list2_index <= len(list2) - 1:
        if list2[list2_index] != list1[list2_index]:
            return_value = False
        list2_index += 1    
    return return_value


print(is_equal([1, 1, 1], [1, 0, 1]))