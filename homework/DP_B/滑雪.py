def in_field(a, b, n, m):
    return 0 <= a <= n - 1 and 0 <= b <= m - 1

def dfs(x, y):
    global place, result, r, c, neighbor_direction
    count = 1
    temp = []
    for item in neighbor_direction:
        tx = x + item[0]
        ty = y + item[1]
        if in_field(tx, ty, r, c) and place[x][y] > place[tx][ty]:
            temp.append(1)
            if result[tx][ty] != -1:
                temp[-1] += result[tx][ty]
            else:
                temp[-1] += dfs(tx, ty)
    if len(temp) == 0:
        return count
    else:
        count = max(temp)
    return count


neighbor_direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
r, c = [int(i) for i in input().strip().split(" ")]
place = []
result = [[-1 for i in range(c)] for j in range(r)]
for line in range(r):
    place.append([int(i) for i in input().strip().split(" ")])
for i in range(r):
    for j in range(c):
        result[i][j] = dfs(i, j)
print(max([max(item) for item in result]))
