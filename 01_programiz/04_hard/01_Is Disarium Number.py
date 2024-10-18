'''
Write a function to check if a number is Disarium or not.

A number is considered Disarium when the sum of its digits, each raised to the
power of their respective positions, equals the number itself.
For example, consider the number "175" . Here,
1^1 + 7^2 + 5^3 = 175
'''


def is_disarium_number(num):
    number_as_list = list(str(num))

    current_pow = 1
    current_sum = 0
    for number in number_as_list:
        value = int(number) ** current_pow
        current_pow += 1
        current_sum += value
    if current_sum == num:
        print(f"{num} is disarium number")
        return True
    else:
        return False


for number in range(10, 1000000):
    is_disarium_number(number)
