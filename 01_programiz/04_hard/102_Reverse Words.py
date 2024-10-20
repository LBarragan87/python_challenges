'''
Write a function to reverse the order of words in a given string.
'''


def reverse_words(s):
    s_reversed = (s.split(" "))
    s_reversed.reverse()
    new_string = " ".join(s_reversed)
    print(new_string)
    return new_string


reverse_words('Hello World')
