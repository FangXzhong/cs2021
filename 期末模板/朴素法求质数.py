primesNumber = []


def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def primes(number):
    for i in range(2, number):
        if is_prime(i):
            primesNumber.append(i)


primes(10000)
print(primesNumber)
