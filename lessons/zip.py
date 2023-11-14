"""Combining two lists into a dictionary."""

__author__ = "730233103"


def zip(string: list[str], integers: list[int]) -> dict[str, int]:
    """Return a dictionary from two lists."""
    dictionary: dict[str, int] = {}
    i: int = 0
    if len(string) != len(integers):
        return dictionary
    else:
        for i in range(len(string)):
            dictionary[string[i]] = integers[i]
    return dictionary