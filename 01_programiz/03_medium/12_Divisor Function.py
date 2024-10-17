def find_divisors(n):
    number_to_evaluate = list(range(1, n+1))
    divisors = []
    for number in number_to_evaluate:
        if n % number == 0:
            divisors.append(number)

    print(divisors)
    return divisors


find_divisors(15)
