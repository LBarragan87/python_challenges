'''
Write a function to check if a number is a straight digital number.

A straight digital number is one where the difference between two consecutive
digits is constant.
'''


def is_straight_digital(n):
    numeros_str = list(str(n))
    numero_len = len(numeros_str)-1
    numeros_int = []
    for numero_str in numeros_str:
        numeros_int.append(int(numero_str))

    diff = numeros_int[1] - numeros_int[0]
    inicial = 1
    while inicial <= numero_len:
        if numeros_int[inicial] - numeros_int[inicial-1] != diff:
            print(False)
            return False
        inicial += 1
    print(True)
    return True


is_straight_digital(24680)
