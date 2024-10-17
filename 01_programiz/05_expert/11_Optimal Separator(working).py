'''
Write a function to identify the best separators for the longest substrings in
a string.

An optimal separator is a list of separators that yield the longest possible
substrings, starting and ending with the separator, and not containing it in
between.
For example, The optimal separator for the string "abcbdbe" is "b"
This means that using "b"  as a separator yields the longest possible
substrings that start and end with "b"  and do not contain "b"  in between.
'''


def longest_substring_separators(s):
    string_set = list(set(s))
    string_set.sort()

    letters = []
    for letter in string_set:
        if s.count(letter) > 1:
            letters.append(letter)

    substrings = []
    for letter in letters:
        substring = s.split(letter)
        substring.pop(0)
        substring.pop(-1)
        substrings.append(substring)
        print(substrings)

    best_separators = []
    for letter in letters:
        pass
    print(best_separators)


longest_substring_separators("laboratory")
