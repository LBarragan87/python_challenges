'''
https://app.programiz.pro/community-challenges/challenge/two-sum

Define a function that takes a list of integers and an integer as inputs.
Inside the function, iterate over the list. For each number, check if there is
another number in the list such that their sum equals the target. If so,
return their indices.
Return a list containing the indices of two numbers that add up to the target.
'''


def two_sum(nums, target):
    original_list = nums.copy()
    new_list = nums.copy()
    for number in new_list:
        a = number
        index_a = nums.index(a)
        new_list.pop(index_a)
        for number in new_list:
            b = number
            index_b = nums.index(b)
            this_sum = a + b
            if this_sum == target:
                result = [index_a, index_b]
                result.sort()
                print(result)
                
                return result
        new_list = original_list.copy()


two_sum([2, 1, 2, 7], 9)
