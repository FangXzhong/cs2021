n = int(input())
num_list = [int(i) for i in input().split(" ")]
result = []
maxn = num_list[0]
for i in range(n):
    result.append(num_list[i])
    for j in range(i):
        if num_list[j] < num_list[i] and result[j] + num_list[i] > result[i]:
            result[i] = result[j] + num_list[i]
        maxn = max(maxn, result[i])
print(maxn)
