'''
Write a function to rearrange a string in sorted order of alphabets followed
by the sum of integers.
'''


def rearrange_string(s):
    string_list = list(s)
    letters_list = []
    numbers_list = []
    for letter in string_list:
        try:
            number = int(letter)
            numbers_list.append(number)
        except ValueError:
            letters_list.append(letter)
    letters_list.sort()
    sum_list = sum(numbers_list)
    text_sorted = "".join(letters_list)
    new_text = f"{text_sorted}{sum_list}"
    print(new_text)
    return new_text


rearrange_string('dcba4321')
