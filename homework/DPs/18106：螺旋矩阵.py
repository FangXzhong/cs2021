n = int(input())
result = [[0 for i in range(n)] for j in range(n)]
a = 0
b = 0
edge = [n, n, -1, 0]
forward = 0
for i in range(1, n ** 2 + 1):
    if forward == 0:
        result[a][b] = i
        b += 1
        if b == edge[0]:
            forward = 1
            b -= 1
            a += 1
            edge[0] -= 1
    elif forward == 1:
        result[a][b] = i
        a += 1
        if a == edge[1]:
            forward = 2
            a -= 1
            b -= 1
            edge[1] -= 1
    elif forward == 2:
        result[a][b] = i
        b -= 1
        if b == edge[2]:
            forward = 3
            b += 1
            a -= 1
            edge[2] += 1
    else:
        result[a][b] = i
        a -= 1
        if a == edge[3]:
            forward = 0
            a += 1
            b += 1
            edge[3] += 1
for item in result:
    print(" ".join([str(num) for num in item]))
