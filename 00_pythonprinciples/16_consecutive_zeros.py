'''
The goal of this challenge is to analyze a binary string consisting of only
zeros and ones. Your code should find the biggest number of consecutive
zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which
is the string of zeros and ones. Your function should return the number
described above.
'''


def consecutive_zeros(number):
    str_number = str(number)
    dividing = str_number.split("1")
    counter = []
    for group in dividing:
        group_len = len(group)
        counter.append(group_len)
    max_consecutive_zero = max(counter)
    print(max_consecutive_zero)
    return max_consecutive_zero


consecutive_zeros(1001101000110)
