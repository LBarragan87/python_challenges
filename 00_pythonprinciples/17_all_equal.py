'''
Define a function named all_equal that takes a list and checks whether all
elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
'''


def all_equal(list):
    initial = 1
    list_len = len(list)
    while initial < list_len:
        if list[initial] != list[initial-1]:
            return False
            break
        initial += 1
    return True


print(all_equal([0, 1, 1, 1]))
