'''
Write a function to repeat the last character of a string n times.

Return the new string with the repeated character.
'''


def repeat_last_char(string, n):
    last_char = string[-1] * (n-1)
    new_s = string + last_char
    print(new_s)
    return new_s


repeat_last_char("hello", 3)
