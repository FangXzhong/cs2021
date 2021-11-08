"""
改到这里为止了，当剩余猴子数小于m的时候就没办法继续排除了
可以写新的代码，但是如果写新的代码，那为什么不一开始就采用新的办法呢？
但是如果写了新的算法，其实就不是改别人的代码了
"""
monkey = []
while True:
    n, m = map(int, input().split())
    if m == 0 and n == 0:
        break
    elif m != 0 or n != 0:
        monkey = list(range(1, n + 1))
        while n != 1:
            k = n // m
            if k == 0:
                temp = monkey * (m // n + 1)
                next_start_index = monkey.index(temp[m]) - 1
                monkey.remove(temp[m-1])
                monkey = monkey[next_start_index:]+monkey[:next_start_index]
                n -= 1
            next_start_index = k*m-k if n % m != 0 else 0
            del monkey[m - 1:k*m:m]
            monkey = monkey[next_start_index:] + monkey[0:next_start_index]  # 调换monkey列表顺序制造圆桌效果
            n -= k
        print(monkey[0])
        monkey.clear()
