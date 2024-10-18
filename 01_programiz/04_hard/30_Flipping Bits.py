'''
Write a function to flip the bits of a given integer.

Return the number obtained after flipping all bits.
In binary representation, flipping a bit means changing
'''


def flip_bits(n):
    binary_input = bin(n)[2::]
    toggled = []
    for number in binary_input:
        if number == "0":
            toggled.append("1")
        else:
            toggled.append("0")
    toggled_bin = "".join(toggled)
    toggled_int = int(toggled_bin, 2)
    print(f"{n} -> {toggled_int}")
    return toggled_int


for n in range(1, 100):
    flip_bits(n)
