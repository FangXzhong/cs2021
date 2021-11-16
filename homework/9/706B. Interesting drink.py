n = int(input())
prices = [int(i) for i in input().split(" ")]
prices.sort()
price_index = n - 1
options = [0, ] * prices[-1]
options[-1] = n
for i in range(prices[-1] - 1, 0, -1):
    if i < prices[price_index]:
        delta = 1
        temp = price_index
        if temp > 0:
            while prices[temp - 1] == prices[temp]:
                delta += 1
                temp -= 1
                if temp == 0:
                    break
        options[i - 1] = options[i] - delta
        if options[i - 1] < 0:
            options[i - 1] = 0
            break
        price_index = max(price_index - delta, 0)
    else:
        options[i - 1] = options[i]
for item in range(int(input())):
    money = int(input())
    if money < prices[-1]:
        print(options[money-1])
    else:
        print(n)
