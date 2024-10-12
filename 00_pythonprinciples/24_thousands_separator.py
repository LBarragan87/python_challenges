'''
Write a function named format_number that takes a non-negativenumber as its
only parameter.

Your function should convert the number to a string and add commas as a
thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
'''

# opcion 1


def format_number(number):
    my_number = "{:,}"
    return my_number.format(number)


print(format_number(1000000))


# opcion 2
def format_number(number):
    return f"{number:,}"


print(format_number(1000000))
