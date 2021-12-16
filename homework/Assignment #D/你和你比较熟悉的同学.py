def find(node, tree):
    global searched
    if node not in tree.keys() or tree[node] == [-1, ]:
        temp = 1
        searched.append(node)
        return temp
    else:
        temp = 1
        searched.append(node)
        for item in tree[node]:
            if item in searched:
                continue
            temp += find(item, tree)
        return temp


num = int(input().strip())
relations = dict()
for person in range(num):
    temp = [item for item in input().strip().split()]
    temp.remove(":")
    relations[int(temp[0])] = [int(item) for item in temp[1:]]
result = dict()
for root in relations.keys():
    if root not in result.keys():
        searched = [root, ]
        result[root] = find(root, relations)
res = [(item, result[item]) for item in result]
res.sort(key=lambda x: x[1], reverse=True)
print(res[0][1])
