num = int(input())
activities = list()
for i in range(num):
    start, end = [int(i) for i in input().split(" ")]
    if end > 60 or start < 0:
        continue
    activities.append([start, end])
activities.sort(key=lambda x: x[1])
total = 1
selected = 0
for i in range(len(activities)):
    if activities[i][0] <= activities[selected][1]:
        continue
    else:
        selected = i
        total += 1
print(total)
