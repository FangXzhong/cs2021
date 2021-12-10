n = int(input().strip())
height = [int(i) for i in input().strip().split(" ")]
height_re = height[::-1]
up = []
down = []
for i in range(len(height)):
    if i == 0:
        up.append(1)
        down.append(1)
    else:
        up.append(1)
        down.append(1)
        for j in range(i):
            if height[i] > height[j]:
                up[-1] = max(up[-1], up[j] + 1)
            if height_re[i] > height_re[j]:
                down[-1] = max(down[-1], down[j] + 1)
down.reverse()
total = [up[i] + down[i] - 1 for i in range(len(up))]
print(max(total))

