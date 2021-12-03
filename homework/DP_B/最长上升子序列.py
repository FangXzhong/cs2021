n = int(input().strip())
nums = [int(i) for i in input().strip().split(" ")]
result = [1, ] * n
last = [nums[0], ]
for i in range(1, n + 1):
    for j in range(i):
        if nums[j] < nums[i - 1]:
            result[i - 1] = max(result[i - 1], result[j] + 1)
print(max(result))
