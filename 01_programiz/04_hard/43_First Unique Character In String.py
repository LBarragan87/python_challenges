'''
Write a function to find the first non-repeating character in a string and
return its index.

border-bottom--challenge text-white-shade
'''


def first_unique_char(s):
    string_list = s
    for letter in s:
        counter = s.count(letter)
        if counter == 1:
            letter_index = string_list.index(letter)
            print(letter_index)
            return letter_index
    return -1

first_unique_char('pythonprogramming')
