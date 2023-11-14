def mimic(my_words:str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

print(mimic("hey its xyc"))
mimic("hey its xyc")

my_words: str = "hey its xyc"
response: str = mimic(my_words)
print(response)

def mimic_letter(my_words:str, letter_idx:int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return "Too high of an index"
    else:
        return my_words[letter_idx]
    
print(mimic_letter("hello",6))