n = int(input())
nums = [int(i) for i in input().split()]
result = [0 for num in range(n)]
result1 = [0 for num1 in range(n)]
sub_sum = sum(nums) / 3
if sub_sum != int(sub_sum):
    print(0)
    quit()
temp = 0
for i in range(n):
    if i >= 1:
        result[i] = result[i - 1]
    temp += nums[i]
    if temp == sub_sum:
        result[i] += 1
temp1 = 0
for i in range(n - 1, 1, -1):
    if i < n - 1:
        result1[i] = result1[i + 1]
    temp1 += nums[i]
    if temp1 == sub_sum:
        result1[i] += result[i - 2]
print(max(result1))
