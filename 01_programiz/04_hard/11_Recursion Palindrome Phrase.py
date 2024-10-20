'''
Write a function to check if a given phrase is a palindrome using recursion.

Define a function that takes a string as input.
Inside the function, use recursion to compare the first and last characters of
the string. If they are equal, call the function again with the string
excluding the first and last characters. If they are not equal, return False.
If all characters have been checked and are equal, return True.
Return True if the input string is a palindrome, otherwise return False.
'''


def is_palindrome(s):
    string_list = list(s)
    string_reverse = string_list
    string_reverse.reverse()
    s_reverse = "".join(string_reverse)
    if s == s_reverse:
        print("True")
        return True
    else:
        print("False")
        return False


is_palindrome('python')
