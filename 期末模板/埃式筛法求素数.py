def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数，保留不能整除的，筛掉可以整除的，即倍数。
def _not_divisible(n):
    return lambda x: x % n > 0


# 求素数函数。
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 100000:
        print(n, end=' ')
    else:
        break