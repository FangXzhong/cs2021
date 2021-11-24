p = int(input())
prices = [int(i) for i in input().strip().split(" ")]
prices.sort()
num = [0, 0]
result = [0, ]
if prices[0] > p:
    print(0)
else:
    home = 0
    opponent = len(prices) - 1
    while num[0] >= num[1] and home < opponent:
        while p >= prices[home]:
            p -= prices[home]
            home += 1
            num[0] += 1
        result.append(num[0] - num[1])
        if p + prices[opponent] > prices[home]:
            opponent -= 1
            num[1] += 1
            p += prices[opponent + 1]
    print(max(result))
