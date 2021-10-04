"""
这道题对我来说还是挺有挑战性的。
其实这道题的思路我还是比较清晰的，最烦的是下标的访问问题。
包括刚开始我的程序因为嵌套了两个大循环超时了，后来改成2*2的循环
"""

n, m, k = [int(i) for i in input().split(" ")]
picture = [[0 for i in range(n)] for j in range(m)]
for i in range(k):
    x, y = [int(j) for j in input().split(" ")]
    if picture[y - 1][x - 1] == 1:
        continue
    picture[y - 1][x - 1] = 1
    if i >= 3:
        for a in range(max(x-2, 0), min(x, n-1)):
            for b in range(max(y-2, 0), min(y, m-1)):
                if picture[b][a] == picture[b + 1][a] == picture[b][a + 1] == picture[b + 1][a + 1] == 1:
                    print(i + 1)
                    quit()
print(0)
