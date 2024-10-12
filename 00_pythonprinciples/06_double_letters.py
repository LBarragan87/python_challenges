'''
The goal of this challenge is to analyze a string to check if it contains two
of the same letter in a row. For example, the string "hello" has l twice in a
row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The
parameter is a string. Your function must return True if there are two
identical letters in a row in the string, and False otherwise.
'''
import os


def double_letters(text):
    text_len = len(text)

    this_index = 1
    while this_index < text_len:
        this_letter = text[this_index]
        if this_letter == text[this_index-1]:
            status = True
            print(True)
            return True
        else:
            status = False
        this_index += 1
    print(status)
    return status


os.system("cls")
double_letters("hello")
double_letters("nnono")
