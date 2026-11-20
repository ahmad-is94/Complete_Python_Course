def scream(word):
    return word.upper()
# Default function for making text lowercase
def spell(word):
    return word.lower()
# A third function that work as a high order function
def speak(funct):
    # Storing the function in a variable in high order function
    speaking = funct("Hello ")
    print(speaking)
# Printing text in uppercase
speak(scream)
# Printing text in lowercase
speak(spell)