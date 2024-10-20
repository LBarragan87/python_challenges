'''
Write a function to find the median of a list of integers.

Define a function that takes a list of integers as input.
Inside the function, sort the list and find the middle value. If the size of
the list is even, calculate the mean of the two middle values.
Return the median value.


- If the size of the list is odd, there is one middle value.
- If the size is even, there are two middle values and we take their average.

'''
import math


def find_median(lst):
    lst.sort()
    lst_len = len(lst)

    medians = []
    if lst_len % 2 == 0:
        medians.append(lst[(int(lst_len/2))-1])
        medians.append(lst[int(lst_len/2)])
    else:
        medians.append(lst[math.floor(int(lst_len)/2)])
    print(medians)
    return medians


find_median([2, 1, 3])
