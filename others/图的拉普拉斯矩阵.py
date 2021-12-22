n, m = [int(i) for i in input().strip().split()]
raw = [[0 for i in range(n)] for j in range(n)]
degree = [[0 for a in range(n)] for b in range(n)]
for line in range(m):
    x, y = [int(i) for i in input().strip().split()]
    raw[x][y] = 1
    raw[y][x] = 1
    degree[x][x] += 1
    degree[y][y] += 1
for i in range(n):
    temp = [str(degree[i][j] - raw[i][j]) for j in range(n)]
    print(" ".join(temp))
