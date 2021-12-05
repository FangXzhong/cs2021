# 过不了，不知道是为什么
case_num = int(input().strip())
for case in range(case_num):
    n, m = [int(i) for i in input().strip().split(" ")]
    mymap = []
    for line in range(n):
        mymap.append(list(input().strip()))
    result = 0
    checked = set()
    if n == 1:
        if m == 1:
            if mymap[0][0] == "W":
                print(1)
                continue
            else:
                print(0)
                continue
        else:
            for j in range(m):
                if mymap[0][j] == "W":
                    if j == 0:
                        neighbors = [mymap[0][1], ]
                        checked.add((0, 1))
                    elif j == m - 1:
                        neighbors = [mymap[0][m - 2], ]
                        checked.add((0, m - 2))
                    else:
                        neighbors = [mymap[0][j - 1], mymap[0][j + 1]]
                        checked.add((0, j - 1))
                        checked.add((0, j + 1))
                    if (0, j) not in checked:
                        result += 1
    else:
        for i in range(n):
            for j in range(m):
                if mymap[i][j] == 'W':
                    neighbors = []
                    if i == 0:
                        if j == 0:
                            neighbors = [mymap[i][j + 1], mymap[i + 1][j], mymap[i + 1][j + 1]]
                            checked.add((i, j + 1))
                            checked.add((i + 1, j))
                            checked.add((i + 1, j + 1))
                        elif j == m - 1:
                            neighbors = [mymap[i][j - 1], mymap[i + 1][j], mymap[i + 1][j - 1]]
                            checked.add((i, j - 1))
                            checked.add((i + 1, j))
                            checked.add((i + 1, j - 1))
                        else:
                            neighbors = [mymap[i][j + 1], mymap[i][j - 1], mymap[i + 1][j], mymap[i + 1][j - 1], mymap[i + 1][j + 1]]
                            checked.add((i, j + 1))
                            checked.add((i, j - 1))
                            checked.add((i + 1, j + 1))
                            checked.add((i + 1, j - 1))
                            checked.add((i + 1, j))
                    elif i == n - 1:
                        if j == 0:
                            neighbors = [mymap[i][j + 1], mymap[i - 1][j], mymap[i - 1][j + 1]]
                            checked.add((i, j + 1))
                            checked.add((i - 1, j))
                            checked.add((i - 1, j + 1))
                        elif j == m - 1:
                            neighbors = [mymap[i][j - 1], mymap[i - 1][j], mymap[i - 1][j - 1]]
                            checked.add((i, j - 1))
                            checked.add((i - 1, j))
                            checked.add((i - 1, j - 1))
                        else:
                            neighbors = [mymap[i][j + 1], mymap[i][j - 1], mymap[i - 1][j], mymap[i - 1][j - 1],
                                         mymap[i - 1][j + 1]]
                            checked.add((i, j + 1))
                            checked.add((i, j - 1))
                            checked.add((i - 1, j + 1))
                            checked.add((i - 1, j - 1))
                            checked.add((i - 1, j))
                    else:
                        if j == 0:
                            neighbors = [mymap[i][j + 1], mymap[i - 1][j], mymap[i + 1][j], mymap[i - 1][j + 1], mymap[i + 1][j + 1]]
                            checked.add((i, j + 1))
                            checked.add((i - 1, j))
                            checked.add((i + 1, j))
                            checked.add((i - 1, j + 1))
                            checked.add((i + 1, j + 1))
                        elif j == m - 1:
                            neighbors = [mymap[i][j - 1], mymap[i - 1][j], mymap[i + 1][j], mymap[i - 1][j - 1],
                                         mymap[i + 1][j - 1]]
                            checked.add((i, j - 1))
                            checked.add((i - 1, j))
                            checked.add((i + 1, j))
                            checked.add((i - 1, j - 1))
                            checked.add((i + 1, j - 1))
                        else:
                            neighbors = [mymap[i][j - 1], mymap[i - 1][j], mymap[i + 1][j], mymap[i][j + 1], mymap[i - 1][j - 1],
                                         mymap[i + 1][j - 1], mymap[i + 1][j + 1], mymap[i - 1][j + 1]]
                            checked.add((i, j - 1))
                            checked.add((i, j + 1))
                            checked.add((i - 1, j))
                            checked.add((i + 1, j))
                            checked.add((i - 1, j - 1))
                            checked.add((i - 1, j + 1))
                            checked.add((i + 1, j - 1))
                            checked.add((i + 1, j + 1))
                    if (i, j) not in checked:
                        result += 1
    print(result)
