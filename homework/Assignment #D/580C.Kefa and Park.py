count = 0


def search(node, money):
    money -= costs[node - 1]
    if costs[node - 1] == 0:
        global m
        money = m
    if money < 0:
        return 0
    elif node not in relations:
        global count
        count += 1
    elif node in relations:
        for children in relations[node]:
            search(children, money)


n, m = [int(i) for i in input().split()]
costs = [int(i) for i in input().split()]
relations = dict()
for item in range(n - 1):
    x, y = [int(i) for i in input().split()]
    if x in relations:
        relations[x].append(y)
    else:
        relations[x] = [y, ]

search(1, m)
print(count)
