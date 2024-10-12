'''
Write a function named capital_indexes. The function takes a single parameter,
which is a string. Your function should return a list of all the indexes in
the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''
import os


def capital_indexes(text):
    letters_list = []
    letter_index = 0
    for letter in text:
        if letter.isupper():
            letters_list.append(letter_index)
        letter_index += 1
    print(letters_list)
    return letters_list


os.system("cls")
capital_indexes("HeLlO")
