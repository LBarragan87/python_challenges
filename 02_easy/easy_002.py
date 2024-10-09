'''
write a function to add the fist and last elements of a list
for this input -> [1, 2, 3, 4, 5]
the result should be -> 6
reson: the firs element in the list is "1" and the las element is "5".
their sum is 6
'''
import os
os.system("cls")


def add_end(numbers):
    '''
    add first and last numbers of list
    '''
    return numbers[0] + numbers[-1]


print(add_end([1, 2, 3, 4, 5]))
