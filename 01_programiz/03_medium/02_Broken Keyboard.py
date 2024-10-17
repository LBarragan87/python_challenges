'''
Write a function to check if a given string can be typed using a broken
keyboard.

The broken keyboard can only type certain characters.
The function takes two strings as input. The first string represents the
working keys, and the second string is the word to be typed. Check if
each character in the word is present in the working keys.

Return "True" if the word can be typed with the existing keys, otherwise,
return "False"
'''


def can_type(keys, word):
    for letter in word:
        if letter not in keys:
            print(False)
            return False
    print(True)
    return True


can_type("abc", "bad")
can_type("abcdefg", "bag")
