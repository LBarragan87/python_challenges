'''
write a function to convert a number into a string of dashes equal
to the number

example
for this input -> 5
the result should be -> "-----"
'''
import os
os.system("cls")


def number_to_dashes(n):
    '''
    convert number to dashes
    '''
    return "-" * n


print(number_to_dashes(10))
