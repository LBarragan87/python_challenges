'''
instructions:
if the given number is ood, return "Odd"
if the given number is even, return "even"
'''
import os
os.system("cls")


def odd_even(num):
    '''
    determinate if the gived number is odd or even
    '''
    if num % 2 == 0:
        type_number = "Even"
    else:
        type_number = "Odd"

    return type_number


print(odd_even(3))
print(odd_even(4))
