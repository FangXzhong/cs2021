# def deal1(coin):
#     score = 0
#     if coin == 0:
#         return 0, 0
#     if coin % 2 == 0:
#         coin /= 2
#         score += coin + deal1(deal1(coin)[0])[1]
#         return coin, score
#     else:
#         coin -= 1
#         score += 1 + deal1(deal1(coin)[0])[1]
#         return coin, score
#
#
# for i in range(int(input())):
#     print(int(deal1(int(input()))[1]))
# 上面这个能用，但是超时了，主要问题估计是递归在层数较多的时候复杂度太高

