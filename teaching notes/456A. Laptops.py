"""
挺有意思的一道题，关键是超时问题怎么优化
"""

num = int(input())
items = list()
for i in range(num):
    if i == 0:
        items.append(tuple(int(j) for j in input().split(" ")))
        continue
    if i == 1:
        items.append(tuple(int(j) for j in input().split(" ")))
        items.sort(key=lambda item: item[0])
        if items[0][1] < items[1][1]:
            continue
        else:
            print("Happy Alex")
            quit()
    temp = tuple(int(j) for j in input().split(" "))
    items.append(temp)
    items.sort(key=lambda item: item[0])
    if not items[0][1] < items[1][1] < items[2][1]:
        print("Happy Alex")
        quit()
    else:
        del items[1]
print("Poor Alex")
