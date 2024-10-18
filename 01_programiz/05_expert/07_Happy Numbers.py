'''
Write a function to determine if a number is a happy number.

Return True if the number is happy, otherwise return False.
A happy number is defined by the following process: Starting with any positive
integer, replace the number by the sum of the squares of its digits in
base-ten, and repeat the process until either the number equals 1 (where it
will stay), or it loops endlessly in a cycle that does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
'''


def is_happy(n):
    n_len = 5
    numbers_str_list = list(str(n))
    while n_len != 1:
        start_number = []
        for number in numbers_str_list:
            start_number.append(int(number))
        n_len = len(list(str(n)))

        suma = 0
        for number in start_number:
            suma += number**2

        numbers_str_list = list(str(suma))
        n_len = len(list(str(suma)))
        # print(suma)
    if suma == 1:
        print(f"{n} in happy number")
        return True
    else:
        print(f"{n} is not happy number")
        return False


for n in range(11, 99):
    is_happy(n)
