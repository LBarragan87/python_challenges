'''
Write a function to move all the zeros in an integer to the end.

Return the resulting integer with all zeroes moved to the end.
'''


def move_zeroes_to_end(n):
    number_list = list(str(n))
    up_to_zero = []
    zero = []
    for number in number_list:
        if int(number) == 0:
            zero.append(number)
        else:
            up_to_zero.append(number)

        new_number = up_to_zero+zero
    print("".join(new_number))
    return "".join(new_number)


move_zeroes_to_end(1020304050)
