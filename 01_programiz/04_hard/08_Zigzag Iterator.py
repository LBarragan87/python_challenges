'''
Zigzag Iterator

The zigzag iterator should take two 1D integer lists as input and return the
elements alternately from each of the lists.
'''


def zigzag_iterator(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    max_len = max(len1, len2)
    index = 0

    zig_zag_list = []
    while index <= max_len:
        try:
            zig_zag_list.append(list1[index])
        except IndexError:
            "do nothing"
        try:
            zig_zag_list.append(list2[index])
        except IndexError:
            "do nothing"
        index += 1

    print(zig_zag_list)


zigzag_iterator([1, 2], [3, 4, 5, 6])
