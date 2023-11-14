"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730233103"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")

while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again:")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_index: int = 0
word_index_emoji: str = ""

while word_index < len(secret):
    
    if guess[word_index] == secret[word_index]:
        word_index_emoji = word_index_emoji + GREEN_BOX
    else:
        exist_elsewhere: bool = False
        alternate_index: int = 0   
        while not exist_elsewhere and alternate_index < len(secret):
            if guess[word_index] == secret[alternate_index]:
                exist_elsewhere = True
            else: 
                alternate_index = alternate_index + 1
        if exist_elsewhere is True:
            word_index_emoji = word_index_emoji + YELLOW_BOX
        else: 
            word_index_emoji = word_index_emoji + WHITE_BOX
    word_index = word_index + 1

print(word_index_emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    
    
