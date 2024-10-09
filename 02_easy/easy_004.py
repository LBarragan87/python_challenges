'''
write a function to replace all ocurrences of ":)"
in a string with a smiley face emoji
'''
import os
import emoji
os.system("cls")


def replace_smiley(text):
    '''
    replace ":)" with emoji
    '''
    return text.replace(":)",
                        emoji.emojize(':smiling_face_with_smiling_eyes:'))


MY_TEXT = ":) :) replace test :) :) :)"
print(MY_TEXT)
print(replace_smiley(MY_TEXT))
