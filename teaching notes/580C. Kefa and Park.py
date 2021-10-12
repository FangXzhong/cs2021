n, m = [int(i) for i in input().split(" ")]
cost = [int(i) for i in input().split(" ")]
result = [0,]*n # 用于存储最终节点消耗的列表，索引号=节点号-1，如[1,2,0,0]
nodes = dict() # 用于存储节点关系的字典，如1能到2和3，则{1:[2,3]}
money = m - cost[0]
result[0] = cost[0]
for i in range(n - 1):
    x, y = [int(i) for i in input().split(" ")]
    if x in nodes:
        nodes[x].append(y)
    else:
        nodes[x] = list()
        nodes[x].append(y)
while nodes:
    selected_node = min(nodes.keys())
    for item in nodes[selected_node]:
        result[item - 1] = result[selected_node - 1] + cost[item - 1]
    print(result)
    del nodes[selected_node] 
print(result)
