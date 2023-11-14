"""Test my zip function."""

__author__ = "730233103"

from lessons.zip import zip


def test_empty_lists() -> None:
    """Zip of two empty list should be blank."""
    assert zip([], []) == {}


def test_unequal_lists() -> None:
    """Zip of two unequal list should be blank."""
    test_string: list[str] = ["Happy"]
    test_integers: list[int] = [1, 2]
    assert zip(test_string, test_integers) == {}


def test_negative_integer_lists() -> None:
    """Zip of negative integers in integer list should be return negative numbers in dictionary."""
    test_string: list[str] = ["Happy"]
    test_integers: list[int] = [-1]
    assert zip(test_string, test_integers) == {"Happy": -1}
