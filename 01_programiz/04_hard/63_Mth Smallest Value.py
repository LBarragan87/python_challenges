'''
Write a function to find the mth smallest value in k sorted lists.

Return the mth smallest value from all lists.
'''


def find_mth_smallest(list, m):
    new_list = []
    for sub_lst in list:
        new_list += sub_lst
    new_list.sort()
    m_small = new_list[m-1]
    print(m_small)
    return m_small


find_mth_smallest([[1, 3, 5], [2, 4, 6], [0, 7, 8]], 5)
