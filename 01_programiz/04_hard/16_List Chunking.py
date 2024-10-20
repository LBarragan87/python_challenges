'''
Write a function to split a list into chunks of a specified size.
'''


def chunk_list(lst, n):
    x = 0
    sub_list = []
    while x+n < len(lst):
        this_list = lst[x:x+n]
        sub_list.append(this_list)
        x += n
    last_list = lst[x:]
    sub_list.append(last_list)
    print(sub_list)
    return sub_list


chunk_list([1, 2, 3, 4, 5, 6], 4)
