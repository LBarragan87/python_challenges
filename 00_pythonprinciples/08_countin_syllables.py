'''
Counting syllables
Define a function named count that takes a single parameter. The parameter is
a string. The string will contain a single word divided into syllables by
hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
'''


def count(text):
    sylabes_count = len(text.split("-"))
    print(sylabes_count)
    return sylabes_count


count("ho-tel")
count("cat")
count("met-a-phor")
count("ter-min-a-tor")
