"""
使用的时候注意有几个邻居方向，
同时也要注意横纵坐标的情况如何
"""


def in_field(a, b, n, m):
    return 0 <= a <= n - 1 and 0 <= b <= m - 1


neighbors_direction = [(-1, 0),
                       (0, -1), (0, 1),
                       (1, 0)]
neighbors_direction_eight = [(-1, -1), (-1, 0), (-1, 1),
                             (0, -1), (0, 1),
                             (1, -1), (1, 0), (1, 1)]
place = [[0, 1, 2, 3, 4]] * 4
line = 4
col = 5
for y in range(line):
    for x in range(col):
        neighbors = []
        for item in neighbors_direction:
            if in_field(y + item[0], x + item[1], line, col):
                neighbors.append(place[y + item[0]][x + item[1]])
        print(neighbors)
