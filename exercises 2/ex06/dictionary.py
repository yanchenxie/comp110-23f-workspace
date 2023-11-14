"""EX06 - Dictionary Functions."""

__author__ = "730233103"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary that is given."""
    inverted_dict = {}
    for key in input_dict:
        if input_dict[key] in inverted_dict:
            raise KeyError(f"Duplicate value encountered: {input_dict[key]}")
        inverted_dict[input_dict[key]] = key
    return inverted_dict

# print(invert({"a":"b", "c": "a"}))


def count(freq: list[str]) -> dict[str, int]:
    """Count the frequency of each object in the list provided in a dictionary form."""
    storage_dict: dict[str, int] = {}
    for i in freq:
        if i in storage_dict:
            storage_dict[i] += 1
        else:
            storage_dict[i] = 1
    return storage_dict

# print(count(["a", "a", "a", "b", "b", "c"]))


def favorite_color(input_dict: dict[str, str]) -> str:
    """Return the favorite color in a dictionary of color preferences."""
    most_popular_count: int = 0
    most_popular_color: str = "None"
    color_counts: list[str] = []
    for key in input_dict:
        color_counts.append(input_dict[key])
    color_counts_dict: dict[str, int] = count(color_counts)
    for key in color_counts_dict:
        if color_counts_dict[key] > most_popular_count:
            most_popular_color = str(key)
            most_popular_count = color_counts_dict[key]
    return most_popular_color


print(favorite_color({"a": "blue", "c": "green", "d": "green", "e": "blue"}))


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Given a list, out put a dictionary classifying each object in the string with it's first alphabet."""
    output_dict: dict[str, list[str]] = {}
    first_letter: str = ""
    for word in input_list:
        first_letter = word[0].lower()
        if first_letter not in output_dict:
            output_dict[first_letter] = []
        output_dict[first_letter].append(word)
    return output_dict


# print(alphabetizer(["abc", "bca", "ABC"]))


def update_attendance(input_dict: dict[str, list[str]], week_str: str, student_str: str) -> dict[str, list[str]]:
    """Given a attendance log, update it with the new available information."""
    if week_str in input_dict:
        input_dict[week_str].append(student_str)
    else:
        input_dict[week_str] = []
        input_dict[week_str].append(student_str)
    return input_dict


# attendance_log: dict = {"Monday" : ["V", "K"], "Tuesday" : ["A", "Y"]}
# update_attendance(attendance_log, "Tuesday", "Vrinda")
# update_attendance(attendance_log, "Wednesday", "Kaleb")
# print(attendance_log)