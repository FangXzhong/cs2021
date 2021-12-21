def in_field(a, b, n, m):
    return 0 <= a <= n - 1 and 0 <= b <= m - 1


neighbors_direction_eight = [(-1, -1), (-1, 0), (-1, 1),
                             (0, -1), (0, 1),
                             (1, -1), (1, 0), (1, 1)]
n, m = [int(i) for i in input().split(' ')]
start = []
for i in range(n):
    start.append([int(j) for j in input().split(" ")])
result = [['0' for x in range(m)] for y in range(n)]
for y in range(n):
    for x in range(m):
        neighbors = []
        for item in neighbors_direction_eight:
            if in_field(y + item[0], x + item[1], n, m):
                neighbors.append(start[y + item[0]][x + item[1]])
        alive_num = sum(neighbors)
        if start[y][x] == 0:
            if alive_num == 3:
                result[y][x] = "1"
        else:
            if alive_num < 2 or alive_num > 3:
                result[y][x] = "0"
            else:
                result[y][x] = "1"
for line in result:
    print(" ".join(line))
