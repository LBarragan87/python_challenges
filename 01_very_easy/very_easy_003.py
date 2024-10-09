'''
example
for this input -> 2
the result shoud be -> 200
reason: 2 meters is equal to 200 centimeters because
1 meter = 100 centimeters
'''
import os
os.system("cls")


def meters_to_centimeters(meters):
    '''
    function to convert meters to centimeters
    '''
    return meters*100


print(meters_to_centimeters(50))
