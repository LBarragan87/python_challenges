'''
Write a function to check if a number is a Harshad number or not.

Return True if the number is a Harshad number, else return False.
A Harshad number in a given number base is an integer that is divisible by the
sum of its digits when written in that base.
'''


def is_harshad(n):
    number_to_string = list(str(n))
    sum = 0
    for number in number_to_string:
        sum += int(number)
    if n % sum == 0:
        print(f"{n} is harshad number")
        return True
    else:
        return False


# is_harshad(18)
for number in range(1, 1000):
    is_harshad(number)
