def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

mimic("Hello!")
print(mimic("Hello!"))
my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)

def mimic_letter(my_words: str, letter_idx: int):
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("Index too high")
    #If we made it here, that means that letter_idx is valid
    return my_words[letter_idx]