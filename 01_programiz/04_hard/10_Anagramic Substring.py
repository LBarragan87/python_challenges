'''
Write a function to check if an anagram of a string is a substring of another
string.

Define a function that takes two strings as input.
Inside the function, create all possible anagrams of the first string and
check if any of them is a substring of the second string.
Return True if an anagram of the first string is a substring of the second
string, otherwise return False.

'''


def is_anagram_substring(s1, s2):
    for letter in s1:
        if letter not in s2:
            print(False)
            return False
    print(True)
    return True


is_anagram_substring('abc', 'cbade')
