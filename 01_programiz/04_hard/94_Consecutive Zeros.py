'''
Write a function to find the longest sequence of consecutive zeros in a binary
string.
'''


def longest_zero_sequence(binary_string):
    dividing = binary_string.split("1")
    counter = []
    for group in dividing:
        group_len = len(group)
        counter.append(group_len)
    max_consecutive_zero = max(counter)
    print(max_consecutive_zero)
    return max_consecutive_zero


longest_zero_sequence('101001000100001')
