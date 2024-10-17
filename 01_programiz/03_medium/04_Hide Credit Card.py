'''
Write a function to hide a credit card number.

The function takes in the credit card number as an argument.
Inside the function replace all the digits of the card number with asterisks
(*), except for the last four digits.

Return the new credit card number.
'''


def mask_credit_card(card_number):
    hiden = (chr(42))*(len(str(card_number))-4)
    card_end = (str(card_number))[-4::]
    masked = hiden+card_end
    print(masked)
    return masked


mask_credit_card(7241565286751867)
mask_credit_card(432576918258826)
mask_credit_card(14673883458645)
mask_credit_card(4444444444444444)
