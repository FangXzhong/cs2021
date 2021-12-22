n, m = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
result = [1 for i in range(n)]
temp = {nums[-1], }
for i in range(n - 2, -1, -1):
    result[i] = result[i + 1]
    if nums[i] not in temp:
        temp.add(nums[i])
        result[i] += 1
for item in range(m):
    print(result[int(input()) - 1])
