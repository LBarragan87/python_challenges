'''
Write a function to type the given string using a broken keyboard.

The broken keyboard toggles the case of letters every time a vowel is pressed.
So, the case changes every time a vowel is encountered.
Return the string as typed by the keyboard.
Note:

 Assume that the keyboard starts from lowercase.
'''


def type_with_broken_keyboard(word):
    vowels = ["a", "e", "i", "o", "u"]
    start = "lower"
    new_text = []
    for letter in word.lower():
        if letter in vowels:
            if start == "lower":
                new_text.append(letter.upper())
                start = "upper"
                continue
            else:
                new_text.append(letter.lower())
                start = "lower"
        else:
            if start == "lower":
                new_text.append(letter.lower())
            else:
                new_text.append(letter.upper())

    print("".join(new_text))
    return "".join(new_text)


type_with_broken_keyboard("mississippi")
type_with_broken_keyboard("xyz")
type_with_broken_keyboard("oooooooo")
type_with_broken_keyboard("abc")
