'''
Write a function to decode a string that is recursively encoded as count
followed by substring.

input
'3[a]2[bc]'
return
'aaabcbc'

'''


def decode_string(s):
    new_string = s.replace("[", "_")
    new_string = new_string.split("]")
    new_string.pop(-1)

    codes = []
    for substring in new_string:
        code_elements = substring.split("_")
        sub_code = code_elements[1]*int(code_elements[0])
        codes.append(sub_code)
    print("".join(codes))


decode_string('3[a]2[bc]')
