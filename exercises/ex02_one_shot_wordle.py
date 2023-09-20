"""EX02 - One Shot Wordle"""
__author__ = "730566761"

secret_word = str("python")
guess_word = str(input(f"What is your {len(secret_word)}-letter word? "))
while len(secret_word) != len(guess_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")
if guess_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_idx: int = 0
emoji: str = " "
while word_idx < len(secret_word):
    if guess_word[word_idx] == secret_word[word_idx]:
        emoji = emoji + GREEN_BOX
        word_idx = word_idx + 1
    else:
        alt_idx: int = 0
        in_word: bool = False
        while in_word is not True and alt_idx < len(secret_word):
            if secret_word[alt_idx] == guess_word[word_idx]:
                in_word = True
            else:
                alt_idx = alt_idx + 1
        if in_word is True:
            emoji = emoji + YELLOW_BOX
            word_idx = word_idx + 1
        if in_word is False:
            emoji = emoji + WHITE_BOX
            word_idx = word_idx + 1
print(emoji)