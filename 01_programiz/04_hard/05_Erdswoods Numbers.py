'''
Write a function to determine if a number is an Erdswoods number.

An Erdswoods number is a positive integer that cannot be written as the sum of
the squares of two integers.
Return True if the number is an Erdswoods number, False otherwise.
'''


def is_erdswoods(n):
    for number in range(1, n):
        for sub_number in range(1, n):
            powed_numbers = (number ** 2) + (sub_number ** 2)
            if powed_numbers == n:
                return False
    print(f"{n} is erdwoods number")
    return True


for number in range(1, 100):
    is_erdswoods(number)
# is_erdswoods(3)
# is_erdswoods(13)
