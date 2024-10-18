'''
Write a function to calculate the accumulating sum of a list of numbers.

Return a new list where each element is the cumulative sum up to that index.
'''


def cumulative_sum(numbers):
    sum_list = []
    accumulate_sum = 0
    for number in numbers:
        accumulate_sum += number
        sum_list.append(accumulate_sum)
    print(sum_list)
    return sum_list


cumulative_sum([1, 2, 3, 4])
