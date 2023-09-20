"""EX02 - One Shot Wordle"""
__author__ = "730566761"

secret: str = "python"
word_len = len(secret)
guess: str = input(f"What is your {word_len}-letter guess? ")
guess_len = len(guess)

while word_len == guess_len:
    print("Not quite. Play again soon!")
while word_len != guess_len:
    input(f"That was not {word_len} letters! Try again: ")
if guess == secret:
    print("Woo! You got it!")
