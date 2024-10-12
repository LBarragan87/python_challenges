'''
Flatten a list
Write a function that takes a list of lists and flattens it into a
one-dimensional list.

Name your function flatten. It should take a single parameter and return a
list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]
'''


def flatten(super_list):

    flattened = []
    for list in super_list:
        for element in list:
            flattened.append(element)

    print(flattened)
    return flattened


flatten(([[1, 2], [3, 4]]))
