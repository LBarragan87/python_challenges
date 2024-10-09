'''
instructions

we can find the discoun received by substractin the discounted price from the
original price, i.e.,
discount received = original price - discoundted price

for example, if the original price is 200 and the discounted price is 150, the
discount received is 200 - 150 = 50

return the discount received from the viden original price and discounted price
'''
import os
os.system("cls")


def calculate_discount(original_price, discounted_price):
    '''
    calculate the discount received
    '''
    return original_price-discounted_price


print(calculate_discount(500, 200))
