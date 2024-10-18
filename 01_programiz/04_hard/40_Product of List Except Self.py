'''
Write a function  that returns  a list of products from all the elements in a
list excluding itself.

Define a function that takes a list of integers as input.
Inside the function, calculate the product of all elements in the list. Then
for each element in the list, divide the total product by that element.
Return a list where each element is the product of all other elements in the
original list.
'''


def product_except_self(nums):
    product = 1
    for num in nums:
        product = product*num
    print(product)
    divitions = []
    for num in nums:
        divitions.append(int(product/num))

    print(divitions)


product_except_self([1, 2, 3, 4])
