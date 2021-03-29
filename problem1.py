"""
A program that translates user input words to
pig latin by calling the piggify function.   
"""

# vowel bank
vowels = 'aeiou'

def piggify(word):
    # checks if first letter is a vowel
    if word[0] in vowels:
        piggified_word = word + "yay"
    else:
        # iterates through letters in input String
        for i in range(0, len(word)):
            # checks for the location of the fist vowel
            if word[i] in vowels:
                # uses index slicing to form reorganized word
                piggified_word = word[i:] + word[:i] + "ay"
                break
            # if no vowels simply adds "ay"
            else:
                piggified_word = word + "ay"
    return piggified_word

looping = True
while looping:
    word = input("What word would you like to piggify? ")
    if word == ".":
        looping = False
    else:
        print(piggify(word))
 
