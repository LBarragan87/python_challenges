'''
Write a function to convert a given string to Spongecase.
Spongecase is a style of text where letters alternately appear in lower and
upper case starting with lowercase.

Spongecase is a style of text where letters alternately appear in lower and
upper case starting with lowercase.
'''


def to_spongecase(text):
    start = "lower"
    new_string = []
    for letter in text:
        if letter == " ":
            new_string.append(letter)
        elif isinstance(letter, int):
            new_string.append(letter)
        else:
            if start == "lower":
                new_string.append(letter.lower())
                start = "upper"
                continue
            if start == "upper":
                new_string.append(letter.upper())
                start = "lower"
    print("".join(new_string))

    return "".join(new_string)


to_spongecase("programizPro123")
to_spongecase("learn to code")
