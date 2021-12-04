t, m = [int(i) for i in input().strip().split(" ")]
items = []
for item in range(m):
    items.append([int(i) for i in input().strip().split(" ")])
result = [[], ]
result[0] = [items[0][1] if temp_time >= items[0][0] else 0 for temp_time in range(1, t + 1)]
for thing in range(1, m):
    result.append([0, ]*t)
    for temp_time in range(1, t + 1):
        result[-1][temp_time - 1] = result[-2][temp_time - 1]
        if temp_time > items[thing][0]:
            result[-1][temp_time - 1] = max(result[-2][temp_time - 1], items[thing][1] + result[thing - 1][temp_time - items[thing][0] - 1])
        elif temp_time == items[thing][0]:
            result[-1][temp_time - 1] = max(result[-1][temp_time - 1], items[thing][1])
print(result[-1][-1])
