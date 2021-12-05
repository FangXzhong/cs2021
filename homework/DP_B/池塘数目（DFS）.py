def in_field(a, b, n, m):
    return 0 <= a <= n - 1 and 0 <= b <= m - 1


def dfs(x, y):
    global my_map
    my_map[x][y] = "."
    for i in range(-1, 2):
        for j in range(-1, 2):
            tx = x + i
            ty = y + j
            if in_field(tx, ty, n, m) and my_map[tx][ty] == "W":
                dfs(tx, ty)


case_num = int(input().strip())
for case in range(case_num):
    n, m = [int(i) for i in input().strip().split(" ")]
    my_map = []
    for line in range(n):
        my_map.append(list(input().strip()))
    result = 0
    for i in range(n):
        for j in range(m):
            if my_map[i][j] == "W":
                result += 1
                dfs(i, j)
    print(result)
