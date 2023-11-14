"""EX07 - Dictionary Test."""

__author__ = "730233103"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import count 
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_invert_empty_dic() -> None:
    """Edge case: Invert of empty dic should be blank."""
    assert invert({}) == {}


def test_invert_dic() -> None:
    """Use case: Invert dictionary of 2 key value pair should yield the inverted dic."""
    test_dic: dict[str, str] = {"a": "b", "c": "a"}
    assert invert(test_dic) == {"b": "a", "a": "c"}


def test_invert_int_dic() -> None:
    """Use case: Invert dictionary of 2 key value pair but with one accidental integer input should yield the inverted dic."""
    test_dic: dict[str, str] = {"a": "1", "c": "a"}
    assert invert(test_dic) == {"1": "a", "a": "c"}


def test_count_empty_list() -> None:
    """Edge case: Count of empty list should be an empty dic."""
    assert count([]) == {}


def test_count_list() -> None:
    """Use case: Count of non-empty list should be an non empty dic with a key value pair representing how many times a key has appeared."""
    test_list: list[str] = ["a", "a", "a", "b", "b", "c"]
    assert count(test_list) == {"a": 3, "b": 2, "c": 1}


def test_count_one_list() -> None:
    """Use case: Count of non-empty list with the same value should be an non empty dic with one key value pair representing how many times a key has appeared."""
    test_list: list[str] = ["a", "a", "a"]
    assert count(test_list) == {"a": 3}


def test_fav_color_empty_dict() -> None:
    """Edge case: Return of an empty dic for fav color function should be "None"."""
    assert favorite_color({}) == 'None'


def test_fav_color_dic() -> None:
    """Use case: Return value of a dic for fav color function should be the one with the most occurence of color for the key values."""
    test_dic: dict[str, str] = {"c": "green", "d": "green", "e": "blue"}
    assert favorite_color(test_dic) == "green"


def test_fav_color__tie_dic() -> None:
    """Use case: Return value of a dic for fav color function should be the one with the most occurence of color for the key values, with the added requirement that in case of a tie, the color that appeared first is returned."""
    test_dic: dict[str, str] = {"b": "blue", "c": "green", "d": "green", "e": "blue"}
    assert favorite_color(test_dic) == "blue"


def test_alpha_empty_list() -> None:
    """Edge case: Alphabetizer of empty list should be an empty dic."""
    assert alphabetizer([]) == {}


def test_alpha_list() -> None:
    """Use case: Count of non-empty list of strings should be an non empty dic with a key being the first letter of the strings in the list and the value being lists of the original strings with the same starting letter."""
    test_list: list[str] = ["abc", "bca", "aBC"]
    assert alphabetizer(test_list) == {'a': ['abc', 'aBC'], 'b': ['bca']}


def test_alpha_upper_lower_list() -> None:
    """Use case: Count of non-empty list of strings should be an non empty dic with a key being the first letter of the strings in the list and the value being lists of the original strings with the same starting letter, with the added requirement that upper and lower case of first letter are all classified as the lower case."""
    test_list: list[str] = ["abc", "bca", "ABC"]
    assert alphabetizer(test_list) == {'a': ['abc', 'ABC'], 'b': ['bca']}


def test_empty_week_student_str() -> None:
    """Edge case: Input of blank week and student string would output the same input dictionary of attendance log with no changes."""
    attendance_log: dict = {"Monday": ["V", "K"], "Tuesday": ["A", "Y"]}
    assert update_attendance(attendance_log, "", "") == {"Monday": ["V", "K"], "Tuesday": ["A", "Y"]}


def test_week_student_str() -> None:
    """Use case: Input of week of day that is already in dictionary  and student string would output the same input dictionary of attendance log with updated element of the same key value pair as the week of day given."""
    attendance_log: dict = {"Monday": ["V", "K"], "Tuesday": ["A", "Y"]}
    assert update_attendance(attendance_log, "Tuesday", "D") == {"Monday": ["V", "K"], "Tuesday": ["A", "Y", "D"]}


def test_different_week_student_str() -> None:
    """Use case: Input of week of day that is not already in dictionary  and student string would output the same input dictionary of attendance log with a new key value pair representing the new day for in the input."""
    attendance_log: dict = {"Monday": ["V", "K"], "Tuesday": ["A", "Y"]}
    assert update_attendance(attendance_log, "Wednesday", "E") == {"Monday": ["V", "K"], "Tuesday": ["A", "Y"], "Wednesday": ["E"]}