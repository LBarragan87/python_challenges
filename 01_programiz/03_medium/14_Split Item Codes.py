'''
Write a function to split item codes into their individual components.

Define a function  that takes a string as input.
Inside the function, divide the item code into its individual components.
Return a list of the individual components of the item code.
'''


def split_item_codes(item_code):
    splitted = item_code.split("-")
    print(splitted)
    return splitted


split_item_codes('ABC-123-XYZ')
