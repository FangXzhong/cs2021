# n = int(input().strip())
# nums = [int(i) for i in input().strip().split()]
# while 0 in nums:
#     nums.remove(0)
# if len(nums) == 1:
#     print(0)
#     quit()
# nums.sort(reverse=True)
# nums[-2] += nums[-1]
# nums.pop(-1)
# print(sum([nums[i] * (i + 1) for i in range(len(nums))]))


import heapq

n = int(input().strip())
nums = [float(i) for i in input().strip().split()]
result = 0
my_heap = []
for num in range(n):
    heapq.heappush(my_heap, nums[num])
for item in range(n - 1):
    temp1 = heapq.heappop(my_heap)
    temp2 = heapq.heappop(my_heap)
    result += temp1 + temp2
    heapq.heappush(my_heap, temp1 + temp2)
print(result)
