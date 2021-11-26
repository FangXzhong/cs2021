n = int(input())
num = [int(i) for i in input().split(" ")]
stats = dict(zip(list(range(100002)), [0, ] * 100002))
for item in num:
    stats[item] += 1
result = [0]
for i in range(1, 100002):
    if i == 1:
        result.append(stats[1])
    else:
        result.append(max(result[i - 1], result[i - 2] + stats[i] * i))
print(result[-1])
