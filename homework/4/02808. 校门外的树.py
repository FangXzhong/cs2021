l, m = [int(i) for i in input().split(" ")]
result = [1, ] * (l + 1)
for j in range(m):
    start, end = [int(i) for i in input().split(" ")]
    for k in range(start, end + 1):
        result[k] = 0
print(sum(result))
