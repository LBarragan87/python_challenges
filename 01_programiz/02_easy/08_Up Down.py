import os


def up_down(n):
    if n > 0:
        type = "Up"
    elif n == 0:
        type = "Zero"
    else:
        type = "Down"
    print(type)
    return type


os.system("cls")
up_down(5)
up_down(0)
up_down(-5)
