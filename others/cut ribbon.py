n, a, b, c = [int(i) for i in input().split()]
a, b, c = sorted([a, b, c])
result = [-100, ] * 4005
result[a] = 1
result[b] = 1
result[c] = 1
for i in range(n + 1):
    if i >= a:
        result[i] = max(result[i], result[i - a] + 1)
    if i >= b:
        result[i] = max(result[i], result[i - b] + 1)
    if i >= c:
        result[i] = max(result[i], result[i - c] + 1)
print(result[n])
