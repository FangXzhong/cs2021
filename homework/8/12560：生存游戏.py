n, m = [int(i) for i in input().split(' ')]
start = []
for i in range(n):
    start.append([int(j) for j in input().split(" ")])
result = [['0' for x in range(m)] for y in range(n)]
for a in range(n):
    for b in range(m):
        neighbor_list = []
        if 0 < a < n - 1:
            if 0 < b < m - 1:
                neighbor_list += start[a - 1][b - 1: b + 2]
                neighbor_list += start[a + 1][b - 1: b + 2]
                neighbor_list.append(start[a][b - 1])
                neighbor_list.append(start[a][b + 1])
            elif b == 0:
                neighbor_list += start[a - 1][b: b + 2]
                neighbor_list += start[a + 1][b: b + 2]
                neighbor_list.append(start[a][b + 1])
            else:
                neighbor_list += start[a - 1][b - 1: b + 1]
                neighbor_list += start[a + 1][b - 1: b + 1]
                neighbor_list.append(start[a][b - 1])
        elif a == 0:
            if 0 < b < m - 1:
                neighbor_list.append(start[a][b - 1])
                neighbor_list.append(start[a][b + 1])
                neighbor_list += start[a + 1][b - 1: b + 2]
            elif b == 0:
                neighbor_list.append(start[a][b + 1])
                neighbor_list += start[a + 1][b: b + 2]
            else:
                neighbor_list.append(start[a][b - 1])
                neighbor_list += start[a + 1][b - 1: b + 1]
        else:
            if 0 < b < m - 1:
                neighbor_list.append(start[a][b - 1])
                neighbor_list.append(start[a][b + 1])
                neighbor_list += start[a - 1][b - 1: b + 2]
            elif b == 0:
                neighbor_list.append(start[a][b + 1])
                neighbor_list += start[a - 1][b: b + 2]
            else:
                neighbor_list.append(start[a][b - 1])
                neighbor_list += start[a - 1][b - 1: b + 1]
        neighbor_num = sum(neighbor_list)
        if neighbor_num < 2:
            result[a][b] = '0'
        elif neighbor_num < 4 and start[a][b] == 1:
            result[a][b] = '1'
        elif neighbor_num > 3:
            result[a][b] = '0'
        elif neighbor_num == 3:
            result[a][b] = '1'
for item in result:
    print(" ".join(item))
        