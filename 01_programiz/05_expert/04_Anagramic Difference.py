'''
Write a function to find the difference between the largest and smallest
number possible from a given set of numbers.

example
123
returns
198

smallest number = 123
largest number = 321
diff = 321 - 123 = 198
'''


def anagramic_difference(numbers):
    numbers_list = list(str(numbers))
    smallest = numbers_list.copy()
    smallest.sort()
    bigger = smallest.copy()
    bigger.reverse()
    smallest_int = int("".join(smallest))
    bigger_int = int("".join(bigger))
    difference = bigger_int - smallest_int
    print(difference)
    return difference


anagramic_difference(123)
