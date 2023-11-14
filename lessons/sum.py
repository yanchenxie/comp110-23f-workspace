"""Summing the elements of a list using different loops."""

_author_ = "730233103"


def w_sum(vals: list[float]) -> float:
    """Use a while loop to return sum of numbers in val list."""
    i: int = 0
    sum: float = 0.0
    while (i < len(vals)):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Use a for loop to return sum of numbers in val list."""
    sum: float = 0.0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Use a for in range loop to return sum of numbers in val list."""
    sum: float = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum
