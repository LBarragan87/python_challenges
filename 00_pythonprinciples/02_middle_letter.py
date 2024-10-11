'''
Middle letter
Write a function named mid that takes a string as its parameter. Your function
should extract and return the middle letter. If there is no middle letter,
your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""
'''
import math


def mid(text):
    text_len = len(text)
    if text_len % 2 == 0:
        middle_letter = ""
    else:
        middle_letter = text[math.ceil((text_len/2)-1)]
    print(middle_letter)
    return middle_letter


mid("testing")
