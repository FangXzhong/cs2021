lines = int(input())
nums = list()
for i in range(lines):
    temp = input().strip()
    nums.append([int(i) for i in temp.split(" ")])
result = list()
for i in range(lines):
    if i == 0:
        result.append([nums[i][0], ])
    elif i == 1:
        result.append([result[0][0] + nums[1][0], result[0][0] + nums[1][1]])
    else:
        temp = list()
        temp.append(result[i - 1][0] + nums[i][0])
        for j in range(1, i):
            temp.append(max(result[i - 1][j - 1], result[i - 1][j]) + nums[i][j])
        temp.append(result[i - 1][-1] + nums[i][-1])
        result.append(temp)
print(max(result[-1]))
