'''
Write a function to calculate the minimum number of operations (insertions,
deletions, and substitutions) required to transform one string into another.

Return the minimum number of operations required to transform one string into
another.
'''


def edit_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    min_len = min(len_str1, len_str2)
    index = 0
    counter = 0
    while index < min_len:
        if str1[index] != str2[index] and str1[index] not in str2:
            counter += 1
            index += 1
            continue
        else:
            index += 1
    counter += abs(len_str1-len_str2)
    print(counter)
    return counter


edit_distance('horse', 'ros')
edit_distance('intention', 'execution')
edit_distance('edit', 'distance')
edit_distance('kitten', 'sitting')
