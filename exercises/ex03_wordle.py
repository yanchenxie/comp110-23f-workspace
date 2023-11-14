"""EX03 - Wordle!"""

__author__ = "730233103"


def contains_char(searched_through: str, searched_for: str) -> bool:
    """Returns true if the searched for character is found in any index in the searched through string."""
    assert len(searched_for) == 1
    word_index: int = 0
    found: bool = False
    while word_index < len(searched_through):
        if searched_through[word_index] == searched_for:
            found = True
        word_index = word_index + 1
    return found   


def emojified(guess: str, secret: str) -> str:
    """Returns string of emoji base on whether a character in guess is an exact match, somewhere match, or not in the secret word at all."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    guess_index: int = 0 
    while guess_index < len(secret):
        if guess[guess_index] == secret[guess_index]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[guess_index]) is True:
                emoji = emoji + YELLOW_BOX
            else: 
                emoji = emoji + WHITE_BOX
        guess_index = guess_index + 1
    return (emoji)


def input_guess(expect_length: int) -> str:
    """Prompt user for a guess and continue until the correct length."""
    player_guess: str = input("Enter a " + str(expect_length) + " character word: ")
    while len(player_guess) != expect_length:
        player_guess = input("That wasn't " + str(expect_length) + " chars! Try again: ")
    return player_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    number_turns: int = 6
    current_turn: int = 1
    win: bool = False
    while not win and (current_turn <= number_turns):
        print("=== Turn " + str(current_turn) + "/" + str(number_turns) + " ===")
        guess: str = input_guess(5)
        secret: str = "codes"
        print(emojified(guess, secret))
        if guess == secret:
            print("You won in " + str(current_turn) + "/" + str(number_turns) + " turns!")
            return
        else:
            current_turn = current_turn + 1
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()