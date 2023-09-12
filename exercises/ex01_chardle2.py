"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730566761"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    exit("Error: Word must contain 5 characters")
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    exit("Error: Character must be a single character.")
print("Searching for " + single_character + " in " + five_character_word)
if single_character == five_character_word[0]:
    print(single_character + " found at index 0")
if single_character == five_character_word[1]:
    print(single_character + " found at index 1")
if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
if single_character == five_character_word[3]:
    print(single_character + " found at index 3")
if single_character == five_character_word[4]:
    print(single_character + " found at index 4")
counter = 0
for s in five_character_word:
    if s == single_character:
        counter += 1
print(counter, " instances of ", single_character, " found in ", five_character_word)

