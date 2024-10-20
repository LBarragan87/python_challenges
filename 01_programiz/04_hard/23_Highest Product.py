'''
Write a function to find the two numbers with the highest product from a list
containing both positive and negative integers.
'''


def highest_product(numbers):
    first_list = numbers.copy()
    second_list = numbers.copy()
    a_index = 0
    products = []
    for number in first_list:
        a = number
        second_list.pop(a_index)
        a_index += 1
        for number in second_list:
            b = number
            product = a * b
            products.append(product)
        second_list = first_list.copy()
    max_product = max(products)
    print(max_product)
    return max_product


highest_product([-10, -3, 1, 2, 3])
