'''
Write a function to add two binary strings and return their sum as a binary
string.
'''


def add_binary(a, b):
    real_number_a = int(a, 2)
    real_number_b = int(b, 2)
    this_sum = real_number_a + real_number_b
    bin_sum = bin(this_sum)
    print(bin_sum[2::])
    return bin_sum[2::]


add_binary("11", "1")
