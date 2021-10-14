"""
    这道题感觉不难，但是非常烦琐，
    并且报错了之后由于不知道输入，也不清楚是哪里错了。
    所以我自己感觉，做题之前应该先把思路理清楚。

    很显然，我们应该先放大的，6*6的没啥可说的，直接放。5*5和4*4的一箱子只能放一个，剩下一些空位。
    然后3*3的就不好说了。不过从上面这个讨论来看，我们大致清楚了应该按照小方块能不能被和大块一起放完进行讨论。

    于是我们可以直接先把4*4及以上的加在总箱数上面，然后利用math.ceil(3*3个数 / 4)来放完3*3的，
    这样一来，我们就放完了3*3及以上的箱子并得到了放完这些需要的箱子个数。

    然后就看一看空位能不能放完2*2的，如果不能再加箱子，也是利用math.ceil()，最后看能不能放完1*1的


    被注释掉的是我第一遍写的代码，看得出来思路很乱，就是想到什么写什么，到后面自己都搞不清楚自己的意思是什么。
    所以我做完这道题的感想是，拿到题目不要急着写代码，先把自己的思路弄清晰，把代码当成实现思路的一个工具，
    这样写出来的东西又快又准确又清晰
"""
import math

rest_dict = {0: 0, 1: 5, 2: 3, 3: 1}  # 这个是剩余的3*3个数和能放的2*2个数的字典映射
while True:
    message = input()
    if message == "0 0 0 0 0 0":
        break
    a1, a2, a3, a4, a5, a6 = [int(i) for i in message.split(" ")]
    total = a4 + a5 + a6 + math.ceil(a3 / 4)
    placed_2 = a4 * 5 + rest_dict[a3 % 4]
    if a2 > placed_2:
        total += math.ceil((a2 - placed_2) / 9)
    placed_1 = 36 * total - 36 * a6 - 25 * a5 - 16 * a4 - 9 * a3 - 4 * a2
    if a1 > placed_1:
        total += math.ceil((a1 - placed_1) / 36)
    print(int(total))

# while True:
#     message = input()
#     if message == "0 0 0 0 0 0":
#         break
#     num = [int(i) for i in message.split(" ")]
#     total = 0
#     total += num[5] + num[4] + num[3]
#     num[0] -= num[4] * 11
#     if num[1] < num[3] * 5:
#         num[0] -= (num[3] * 5 - num[1]) * 4
#         num[1] = 0
#     else:
#         num[1] -= num[3] * 5
#     if num[0] < 0:
#         num[0] = 0
#     if num[2] % 4 == 0:
#         total += num[2] / 4
#         rest = 0
#     else:
#         total += num[2] // 4 + 1
#         rest = num[2] % 4
#     if num[0] <= 0 and num[1] <= 0:
#         print(int(total))
#     else:
#         if rest == 1:
#             if num[1] > 5:
#                 num[1] -= 5
#                 num[0] -= 7
#             else:
#                 num[0] -= 27 - 4*num[1]
#                 num[1] = 0
#         elif rest == 2:
#             if num[1] > 3:
#                 num[1] -= 3
#                 num[0] -= 6
#             else:
#                 num[0] -= 18 - 4*num[1]
#                 num[1] = 0
#         elif rest == 3:
#             if num[1] > 1:
#                 num[1] -= 1
#                 num[0] -= 5
#             else:
#                 num[0] -= 9 - 4 * num[1]
#                 num[1] = 0
#         if num[1] <= 0 and num[0] <= 0:
#             print(int(total))
#         else:
#             if num[1] > 0 and num[1] % 9 == 0:
#                 print(int(total + num[1] / 9 + math.ceil(num[0]/36)))
#             else:
#                 print(int(total + math.ceil(num[0]/36)))
