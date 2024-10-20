'''
Write a function to return the number of prime numbers that are strictly less
than a given integer.

Define a function that takes an integer as input.
Inside the function, iterate from  2  to the input number. For each iteration,
check if the current number is prime. If it is, increment a counter.
Return the count of prime numbers less than the input number.
'''


def count_primes(n):
    primes = []
    for m in range(2, n):
        if m > 1:
            for i in range(2, (m//2)+1):
                if (m % i) == 0:
                    break
            else:
                print(m)
                primes.append(m)
    print(primes)
    return len(primes)


count_primes(5)
