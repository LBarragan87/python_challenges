'''
Write a function to swap  0s and 1s from the binary representation of a number.
Define a function that takes an integer as input.
Inside the function, convert the integer to binary, swap the 0s  and 1s , and
then convert it back to an integer.
'''


def binary_toggle(n):
    binary_input = bin(n)[2::]
    toggled = []
    for number in binary_input:
        if number == "0":
            toggled.append("1")
        else:
            toggled.append("0")
    toggled_bin = "".join(toggled)
    toggled_int = int(toggled_bin, 2)
    print(toggled_int)
    return toggled_int


binary_toggle(200)
