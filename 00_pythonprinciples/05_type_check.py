'''
Write a function named only_ints that takes two parameters. Your function
should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling
only_ints("a", 1) should return False.
'''
import os


def only_ints(val1, val2):
    value1_is_int = isinstance(val1, int)
    value1_is_bool = isinstance(val1, bool)

    value2_is_int = isinstance(val2, int)
    value2_is_bool = isinstance(val2, bool)

    if (value1_is_int and (value1_is_bool is False)) and (value2_is_int and (
                                                            value2_is_bool is
                                                            False)):
        print(True)
        return True
    else:
        print(False)
        return False


os.system("cls")
only_ints(1, "b")
