'''
write a function to convert hours into seconds
'''
import os
os.system("cls")


def convert_to_seconds(hours):
    '''
    convert hours into seconds, 60 seconds are in a minute,
    and 60 minutes are in an hour
    '''
    return hours * 60 * 60


print(convert_to_seconds(2))
