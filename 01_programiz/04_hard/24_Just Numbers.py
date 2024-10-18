'''
Write a function to extract all the numbers from a given string.

 Return None if the string has no numbers.
'''


def extract_numbers(s):
    numbers = []
    for character in s:
        try:
            is_int = (int(character))
            numbers.append(str(is_int))
        except ValueError:
            "do nothing"
    print(numbers)
    if len(numbers) > 0:
        print("".join(numbers))
        return "".join(numbers)
    else:
        return None


extract_numbers('noNumbersHere')
