"""
功能应该没啥问题，但是python有递归深度限制，
所以当输入量为好几万的时候，就会出现runtime error，
"""

count = 0


def search(node, money, parent=None):
    if parent is None:
        parent = []
    money -= costs[node - 1]
    if costs[node - 1] == 0:
        global m
        money = m
    if money < 0:
        return 0
    elif relations[node] == parent:
        global count
        count += 1
    elif node in relations:
        for children in relations[node]:
            if children in parent:
                continue
            search(children, money, [node, ])


n, m = [int(i) for i in input().split()]
costs = [int(i) for i in input().split()]
relations = dict()
for item in range(n - 1):
    x, y = [int(i) for i in input().split()]
    if x in relations:
        relations[x].append(y)
    else:
        relations[x] = [y, ]
    if y in relations:
        relations[y].append(x)
    else:
        relations[y] = [x, ]

search(1, m)
print(count)
