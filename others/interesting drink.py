store_num = int(input())
prices = [int(i) for i in input().split()]
prices.sort()
result = [0, ] * (prices[-1] + 1)
price_index = 0
for i in range(len(result)):
    result[i] = result[i - 1]
    if i >= prices[price_index]:
        add_num = 1
        for j in range(price_index + 1, store_num):
            if prices[j] == prices[price_index]:
                add_num += 1
            else:
                price_index = j - 1
                break
        result[i] += add_num
        price_index += 1
for item in range(int(input())):
    temp = int(input())
    if temp >= prices[-1]:
        print(store_num)
    else:
        print(result[temp])
