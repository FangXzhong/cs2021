num = int(input())
info = list()
for i in range(num):
    x, height = [int(j) for j in input().split(" ")]
    info.append([x, height])
if len(info) < 2:
    print(len(info))
    quit()
total = 2
for i in range(1, len(info) - 1):
    if info[i][1] < info[i][0] - info[i - 1][0]:
        total += 1
    elif info[i][1] < info[i + 1][0] - info[i][0]:
        info[i][0] += info[i][1]
        total += 1
print(total)
