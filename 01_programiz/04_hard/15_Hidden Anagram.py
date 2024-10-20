'''
Write a function to find a hidden anagram in a given string.

Define a function that takes two strings as input: the first one is the text
to search and the second one is the anagram to find.
Inside the function, iterate over the text and check if a substring of the
first string is an anagram of the second string.
Return the first found anagram. If no anagram is found, return 'Anagram not
found'.
'''


def find_anagram(text, word):
    text_split = text.split()
    for sub_text in text_split:
        sub_text_sorted = []
        for letter in sub_text:
            sub_text_sorted.append(letter.lower())
        sub_text_sorted.sort()

        sub_word_sorted = []
        for letter in word:
            sub_word_sorted.append(letter.lower())
        sub_word_sorted.sort()

        if sub_text_sorted == sub_word_sorted:
            print(sub_text.lower())
            return sub_text.lower()
    print("Anagram not found")
    return "Anagram not found"


find_anagram('The quick brown fox jumps over the lazy dog', 'aaa')
