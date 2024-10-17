'''
Write a function to find a subsequence of from a given list of integers.

Define a function that takes a list of integers and an integer
Inside the function,calculate the sum for each subsequence of length
Return the maximum sum found.
'''


def largest_sum_subsequence(numbers, k):
    x_start = 0
    x_end = x_start + k

    groups = []
    sumas = []
    while x_end <= len(numbers):
        suma = 0
        sublist = numbers[x_start:x_start+k]
        for elemento in sublist:
            suma += elemento
        groups.append(list(sublist))
        sumas.append(suma)
        x_start += 1
        x_end = x_start + k
    print(groups)
    print(sumas)
    maximo = max(sumas)
    print(maximo)
    return maximo


largest_sum_subsequence([1, 2, 3, 4, 5], 3)
