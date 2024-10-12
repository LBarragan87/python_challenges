'''
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the
letters.

Write a function named is_anagram that takes two strings as its parameters.
Your function should return True if the strings are anagrams, and False
otherwise.

For example, the call is_anagram("typhoon", "opython") should return True
while the call is_anagram("Alice", "Bob") should return False.
'''


def is_anagram(text_1, text_2):
    list_1 = []
    for letter in text_1:
        list_1.append(letter.upper())
    list_1.sort()

    list_2 = []
    for letter in text_2:
        list_2.append(letter.upper())
    list_2.sort()

    print(list_1 == list_2)
    return list_1 == list_2


is_anagram("typhoon", "opython")
is_anagram("Alice", "Bob")
