'''
instructions
return "true" if the number is divisible by 5. otherwise, return "false"
'''
import os
os.system("cls")


def is_divisible_by_five(n):
    '''
    determinate if gived number is divisible by 5
    '''
    return n % 5 == 0


print(is_divisible_by_five(7))
print(is_divisible_by_five(715))
