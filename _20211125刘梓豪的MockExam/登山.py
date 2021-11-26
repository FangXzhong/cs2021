n = int(input().strip())
spots = [int(i) for i in input().strip().split(" ")]
result = []
up = 0
down = 0
for i in range(n):
    if i == 0:
        result.append([1, 1])
    else:
        if spots[i] == spots[i - 1]:
            result.append(result[i - 1])
            continue
        if spots[i] < spots[down]:
            result.append([result[up][0], max(result[i - 1][0], result[down][1]) + 1])
            down = i
        elif spots[i] > spots[up]:
            result.append([result[up][0] + 1, max(result[i - 1])])
            up = i
        else:
            result.append([result[up][0], max(result[i - 1][0] + 1, result[i - 1][1])])
            
print(max(result[-1]))

