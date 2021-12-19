def check(a, b, c, d):
    for i in range(a, c + 1):
        for j in range(b, d + 1):
            if forest[i][j]:
                return 0
    return 1


n, m = [int(i) for i in input().strip().split()]
forest = []
ans = 0
for line in range(n):
    forest.append([int(i) for i in input().strip().split()])
for line in range(n):
    for col in range(m):
        for k in range(line, n):
            for l in range(col, m):
                if check(line, col, k, l):
                    ans = max(ans, (k - line + 1)* (l - col + 1))
print(ans)
