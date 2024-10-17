'''
Write a function to check if you have hit the jackpot in a slot machine.

To "hit the jackpot" means all four slots show the same symbol or number.
'''


def check_jackpot(slot_machine_outcome):
    first_symbol = slot_machine_outcome[0]
    for symol in slot_machine_outcome:
        if symol != first_symbol:
            print(False)
            return False
    print(True)
    return True


check_jackpot(["@", "@", "1", "@"])
