def good(middle, max_stone, stone_list):
    count = 0
    before = stones[0]
    for i in range(1, len(stones)):
        if stones[i] - before < middle:
            count += 1
        else:
            before = stones[i]
    return count <= max_stone


L, N, M = [int(i) for i in input().strip().split()]
stones = [0, ]
for stone in range(N):
    stones.append(int(input().strip()))
stones.append(L)
left = 0
right = L + 1
while left < right:
    mid = int((left + right + 1) / 2)
    if good(mid, M, stones):
        left = mid
    else:
        right = mid - 1
print(left)
