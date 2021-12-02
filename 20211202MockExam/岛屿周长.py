n, m = [int(i) for i in input().strip().split(" ")]
picture = []
for line in range(n):
    picture.append([int(i) for i in input().strip().split(" ")])
result = 0
if n == 1:
    if m == 1:
        print(4)
    else:
        for j in range(m):
            if picture[0][j] == 1:
                if j == 0:
                    neighbors = [picture[0][1], ]
                elif j == m - 1:
                    neighbors = [picture[0][m - 2], ]
                else:
                    neighbors = [picture[0][j - 1], picture[0][j + 1]]
                result += 4 - sum(neighbors)
        print(result)
else:
    for i in range(n):
        for j in range(m):
            if picture[i][j] == 1:
                neighbors = []
                if i == 0:
                    if j == 0:
                        neighbors = [picture[i][j + 1], picture[i + 1][j]]
                    elif j == m - 1:
                        neighbors = [picture[i][j - 1], picture[i + 1][j]]
                    else:
                        neighbors = [picture[i][j + 1], picture[i][j - 1], picture[i + 1][j]]
                elif i == n - 1:
                    if j == 0:
                        neighbors = [picture[i][j + 1], picture[i - 1][j]]
                    elif j == m - 1:
                        neighbors = [picture[i][j - 1], picture[i - 1][j]]
                    else:
                        neighbors = [picture[i][j + 1], picture[i][j - 1], picture[i - 1][j]]
                else:
                    if j == 0:
                        neighbors = [picture[i][j + 1], picture[i + 1][j], picture[i - 1][j]]
                    elif j == m - 1:
                        neighbors = [picture[i][j - 1], picture[i + 1][j], picture[i - 1][j]]
                    else:
                        neighbors = [picture[i][j + 1], picture[i][j - 1], picture[i + 1][j], picture[i - 1][j]]
                result += 4 - sum(neighbors)
    print(result)
