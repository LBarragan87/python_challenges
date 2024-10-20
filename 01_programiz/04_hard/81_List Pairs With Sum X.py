'''
Write a function to find all pairs from two lists whose sum is equal to a
given number.

Return a list of tuples where each tuple represents a pair of numbers whose
sum is equal to the given number.
'''


def find_pairs(lst1, lst2, x):
    touples = []
    for a in lst1:
        for b in lst2:
            if a + b == x:
                my_tuple = (a, b)
                touples.append(my_tuple)
    print(touples)
    return touples


find_pairs([1, 2, 3], [2, 3, 4], 6)
