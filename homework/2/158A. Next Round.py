n, k = [int(i) for i in input().split(' ')]
scores = [int(i) for i in input().split(' ')]
result = 0
for i in range(len(scores)):
    if scores[i] >= scores[k-1] and scores[i] > 0:
        result += 1
print(result)
