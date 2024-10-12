'''
Challenge
Custom zip
The built-in zip function "zips" two lists. Write your own implementation of
this function.

Define a function named zap. The function takes two parameters, a and b. These
are lists.

Your function should return a list of tuples. Each tuple should contain one
item from the a list and one from b.

You may assume a and b have equal lengths.

If you don't get it, think of a zipper.

For example:

zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)
Should return:

[(0, 5),
 (1, 6),
 (2, 7),
 (3, 8)]
 '''


def zap(list1, list2):
    list1_len = len(list1)
    list2_len = len(list2)
    min_len = min(list1_len, list2_len)
    init = 0
    new_list = []
    while init < min_len:
        sub_list = (list1[init], list2[init])
        new_list.append(sub_list)
        init += 1
    return new_list


print(zap([1, 2], [3, 4]))
