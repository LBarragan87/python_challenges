'''
instructions:
the club only allows people who are 21 years old or older
return "true" if the person can entre the club. otherwise, return false if
they cannot enter the club
'''
import os
os.system("cls")


def can_enter_club(age):
    '''
    evaluate if the person can enter to the club
    '''
    return age >= 21


print(can_enter_club(25))
print(can_enter_club(21))
print(can_enter_club(20))
