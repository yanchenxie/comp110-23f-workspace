"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730233103"

five_letter_word: str = input("Enter a 5-character word: ")

if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")

if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + five_letter_word)

count_occurance = 0

if five_letter_word[0] == single_character:
    print(single_character + " found at index 0")
    count_occurance = count_occurance + 1
if five_letter_word[1] == single_character:
    print(single_character + " found at index 1")
    count_occurance = count_occurance + 1
if five_letter_word[2] == single_character:
    print(single_character + " found at index 2")
    count_occurance = count_occurance + 1
if five_letter_word[3] == single_character:
    print(single_character + " found at index 3")
    count_occurance = count_occurance + 1
if five_letter_word[4] == single_character:
    print(single_character + " found at index 4") 
    count_occurance = count_occurance + 1

if count_occurance == 0:
    print("No instances of " + single_character + " found in " + five_letter_word)
if count_occurance == 1:
    print(str(count_occurance) + " instance of " + single_character + " found in " + five_letter_word)
if count_occurance > 1:
    print(str(count_occurance) + " instances of " + single_character + " found in " + five_letter_word)