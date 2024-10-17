'''
instructions
return "true" if the number is a multiple of 10, and "false" otherwise
'''
import os
os.system("cls")


def is_multiple_of_ten(n):
    '''
    determine if gived number is multiple of then
    '''
    return n % 10 == 0


print(is_multiple_of_ten(50))
