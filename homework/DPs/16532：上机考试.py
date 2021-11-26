m, n = [int(i) for i in input().strip().split()]
place = []
for i in range(m):
    place.append([int(j) for j in input().strip().split()])
detail = []
for i in range(m*n):
    detail.append([int(j) for j in input().strip().split()])
scores = [sum(item) for item in detail]
scores.sort(reverse=True)
result = [0, 0]
max_good = int(m * n * .4)
good = 0
for i in range(max_good + 1):
    if scores[i] != scores[max_good]:
        good += 1
result[1] = str(good)
same = [0, ] * (m * n)
for i in range(m):
    for j in range(n):
        left_index = [i, j - 1]
        right_index = [i, j + 1]
        up_index = [i - 1, j]
        down_index = [i + 1, j]
        if i == 0:
            up_index = down_index
        elif i == m - 1:
            down_index = up_index
        if j == 0:
            left_index = right_index
        elif j == n - 1:
            right_index = left_index
        if m == 1:
            neighbors = [place[left_index[0]][left_index[1]], place[right_index[0]][right_index[1]]]
        else:
            neighbors = [place[left_index[0]][left_index[1]], place[right_index[0]][right_index[1]], place[up_index[0]][up_index[1]], place[down_index[0]][down_index[1]]]
        temp = [detail[item] for item in neighbors]
        if detail[place[i][j]] in temp:
            same[place[i][j]] = 1
result[0] = str(sum(same))
print(" ".join(result))
