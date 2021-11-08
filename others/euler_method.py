def euler(r):
    prime = [0 for i in range(r + 1)]
    common = []
    for i in range(2, r + 1):
        if prime[i] == 0:
            common.append(i)
        for j in common:
            if i * j > r:
                break
            prime[i * j] = 1
            if i % j == 0:
                break
    return prime


s = euler(10)
print()
