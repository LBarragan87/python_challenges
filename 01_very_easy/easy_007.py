'''
instructions:
assume voting age to be 18

example:
for this input -> 20
the result should be -> True

reason: the input age is 20, wich is greader than 18.
Therefore, the person is elegible to vote
'''
import os
os.system("cls")


def elegible_to_vote(age):
    '''
    check if the person age is greater than 18
    '''
    return age >= 18


print(elegible_to_vote(18))
print(elegible_to_vote(20))
