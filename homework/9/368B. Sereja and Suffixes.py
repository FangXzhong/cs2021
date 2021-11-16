n, m = [int(i) for i in input().split(" ")]
num = [int(i) for i in input().split(" ")]
processed = dict()
processed[n] = 1
temp = set()
temp.add(num[-1])
for i in range(len(num)-1, 0, -1):
    if num[i-1] not in temp:
        processed[i] = processed[i + 1] + 1
        temp.add(num[i-1])
    else:
        processed[i] = processed[i + 1]
for i in range(m):
    l = int(input())
    print(processed[l])
