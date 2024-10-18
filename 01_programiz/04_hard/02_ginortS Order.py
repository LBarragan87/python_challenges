'''
Write a function to sort a string in ginortS order.

In ginortS, all sorted lowercase letters are ahead of uppercase letters, all
sorted uppercase letters are ahead of digits, and all sorted odd digits are
ahead of sorted even digits.
'''


# from curses.ascii import islower, isupper


def ginortS(s):
    lower_case = []
    upper_case = []
    odd_number = []
    even_number = []

    for letter in s:
        try:
            letter = int(letter)
        except ValueError:
            letter = letter

        if isinstance(letter, str):
            if letter.isupper():
                upper_case.append(str(letter))
            elif letter.islower():
                lower_case.append(str(letter))
        elif isinstance(letter, int):
            if letter % 2 == 0:
                even_number.append(str(letter))
            else:
                odd_number.append(str(letter))
    lower_case.sort()
    upper_case.sort()
    odd_number.sort()
    even_number.sort()
    master_list = lower_case + upper_case + odd_number + even_number
    new_text = "".join(master_list)
    print(new_text)


ginortS('Sorting1234')
