'''
Write a function to create a numeric seesaw.
For an integer as input, return a list of numbers from
1 to that number and then back down to 1
'''


def numeric_seesaw(n):
    initial_list = list(range(1, n+1))
    endlist = list(range(1, n))
    endlist.reverse()
    print(initial_list+endlist)
    return initial_list+endlist


numeric_seesaw(5)
