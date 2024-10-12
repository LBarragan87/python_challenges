'''
The aim of this challenge is to write code that can analyze code submissions.
We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its
only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
'''


def validate(code):
    if "def" not in code:
        return "missing def"
    elif ":" not in code:
        return "missing :"
    elif "(" not in code and ")" not in code:
        return "missing paren"
    elif '('+')' in code:
        return "missing param"
    elif "    " not in code:
        return "missing indent"
    elif "validate" not in code:
        return "wrong name"
    elif "return" not in code:
        return "missing return"
    else:
        return True


print(validate('def validate(code):\r\n if "def" not in code:\r\n return '
               'missing def"\r\n elif ":" not in code:\r\n return "missing"'
               ' :"\r\n elif "(" not in code and ")" not in code:\r\n return '
               '"missing paren"\r\n elif "():" in code:\r\n return "missing '
               'param"\r\n elif " " not in code:\r\n return "missing indent"'
               '\r\n elif "validate" not in code:\r\n return "wrong name"\r\n'
               'elif "return" not in code:\r\n return "missing return"\r\n'
               'else:\r\n return True'))
