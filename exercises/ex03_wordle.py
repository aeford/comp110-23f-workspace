"""Ex03 - Structured Wordle!"""
__author__ = "730566761"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# when given two strings, the first of any length, the second a single character, it will return True if the single character of the second string is found at any index of the first string, and return False otherwise
def contains_char(word: str, char: str) -> bool:
    """Will see if the character is in the word.""" 
    assert len(char) == 1
    if char in word:
        return True
    else:
        return False


# given two strings of equal length, the first a guess and the second a secret, it will return a string of emoji whose color codifies the same as you previously implemented in EX02
def emojified(guess: str, secret: str) -> str:
    """Checking guess to pair emojis."""
    assert len(guess) == len(secret)
    emoji: str = ""
    word_idx: int = 0
    while word_idx < len(secret):
        if contains_char(secret, guess[word_idx]) is True and guess[word_idx] != secret[word_idx]:
            emoji = emoji + YELLOW_BOX
        if contains_char(secret, guess[word_idx]) is True and guess[word_idx] == secret[word_idx]:
            emoji = emoji + GREEN_BOX
        if contains_char(secret, guess[word_idx]) is False:
            emoji = emoji + WHITE_BOX
        word_idx = word_idx + 1
    return emoji 


# given an integer “expected length” of a guess as a parameter, it will prompt the user for a guess and continue prompting them until they provide a guess of the expected length.
def input_guess(expected_length: int) -> str:
    """Making sure the user's guess is the same length as the secret word."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        if len(user_guess) != expected_length:
            user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


# connects all functions to perform as a game
def main() -> None:
    """The entrypoint of the program and main game loop.""" 
    secret: str = "codes"
    guess: str = " "
    turn: int = 1  
    while guess != secret:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if turn <= 6 and guess != secret:
            turn = turn + 1
        if turn >= 1 and guess == secret:
            print(f"You won in {turn}/6 turns!")
            guess = secret
        if turn == 7:
            print("X/6 - Sorry, try again tomorrow!")
            guess = secret


if __name__ == "__main__":
    main()