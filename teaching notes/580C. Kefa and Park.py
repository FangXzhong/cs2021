# n, m = [int(i) for i in input().split(" ")]
# cost = [int(i) for i in input().split(" ")]
# result = [0, ] * n  # 用于存储最终节点消耗的列表，索引号=节点号-1，如[1,2,0,0]
# nodes = dict()  # 用于存储节点关系的字典，如1能到2和3，则{1:[2,3]}
# money = m
# result[0] = cost[0]
# not_leave_node = set()  # 用于统计哪些节点是叶子节点
# for i in range(n - 1):
#     x, y = [int(i) for i in input().split(" ")]
#     not_leave_node.add(x)
#     if x in nodes:
#         nodes[x].append(y)
#     else:
#         nodes[x] = list()
#         nodes[x].append(y)
# while nodes:
#     selected_node = min(nodes.keys())
#     for item in nodes[selected_node]:
#         result[item - 1] = result[selected_node - 1] + cost[item - 1]
#     del nodes[selected_node]
#
# total_set = set(list(range(1, n + 1)))
# leave_node = total_set - not_leave_node
# print(leave_node)
# print(result)
# print(sum(1 if result[i-1] <= money else 0 for i in leave_node))
# 事实证明以上内容是因为我没有理清题意。题目只要求连续的，我把总的算进去了。。。

"""
    这是第二个版本，事实证明这玩意儿，大部分能过，
    但是在节点不按顺序来的时候，比如 4 1，5 4这样的情况出现的时候就祭了
    还是用dfs写函数做吧
"""
# n, m = [int(i) for i in input().split(" ")]
# cost = [int(i) for i in input().split(" ")]
# result = [float('inf'), ] * n  # 用于存储最终节点消耗的列表，索引号=节点号-1，如[1,2,0,0]
# nodes = dict()  # 用于存储节点关系的字典，如1能到2和3，则{1:[2,3]}
# money = m
# result[0] = cost[0]
# not_leave_node = set()  # 用于统计哪些节点是叶子节点
# not_rightness = set()  # 用于统计不符合要求的节点
# for i in range(n - 1):
#     x, y = [int(i) for i in input().split(" ")]
#     not_leave_node.add(x)
#     if x in nodes:
#         nodes[x].append(y)
#     else:
#         nodes[x] = list()
#         nodes[x].append(y)
# while nodes:
#     selected_node = min(nodes.keys())
#     for item in nodes[selected_node]:
#         if cost[selected_node - 1] != 0:
#             result[item - 1] = result[selected_node - 1] + cost[item - 1]
#             if result[item - 1] > m:
#                 not_rightness.add(item)
#                 if item in nodes:
#                     del nodes[item]
#         else:
#             result[item - 1] = cost[item - 1]
#     del nodes[selected_node]
# total_set = set(list(range(1, n + 1)))
# leave_node = total_set - not_leave_node
# correct_node = leave_node - not_rightness
# print(sum(1 if result[item - 1] <= m else 0 for item in correct_node))

"""
之前就是题目看错了，祭了。还得是先认真看题，搞了这么久结果白搞
"""
n, m = [int(i) for i in input().split(" ")]
costs = [int(i) for i in input().split(" ")]
relations = dict()
results = [0, ] * n
for i in range(n - 1):
    node1, node2 = [int(j) for j in input().split(" ")]
    if node1 not in relations:
        relations[node1] = set()
        relations[node1].add(node2)
    else:
        relations[node1].add(node2)
    if node2 not in relations:
        relations[node2] = set()
        relations[node2].add(node1)
    else:
        relations[node2].add(node1)

