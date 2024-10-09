'''
instructions
assume the pass marks to be 50
return "passed" if the student scored more than 50.
otherwise, return "Failed" if they failed
'''
import os
os.system("cls")


def pass_fail(score):
    '''
    check if the student passed the examination
    '''
    if score >= 50:
        examination = "Passed"
    else:
        examination = "Failed"
    return examination


print(pass_fail(60))
print(pass_fail(50))
print(pass_fail(40))
