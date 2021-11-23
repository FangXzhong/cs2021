n = int(input())
activities = list()
for item in range(n):
    a, b = [int(i) for i in input().split(" ")]
    activities.append((a, b))
activities.sort(key=lambda x: x[1])
if (0, 0) in activities:
    result = [1, ]
else:
    result = [0, ]
for i in range(1, 61):
    temp = list()
    result.append(result[i - 1])
    for item in activities:
        if item[1] == i:
            temp.append(item)
    for item in temp:
        if item[0] >= 1:
            result[i] = max(result[i], result[item[0] - 1] + 1)
        else:
            result[i] = max(result[i], 1)
print(result[-1])
