n, m = [int(i) for i in input().split(" ")]
degree_dict = dict(zip(range(n), [0, ]*n))
A = [[0, ] * n for b in range(n)]
for item in range(m):
    node1, node2 = [int(i) for i in input().split(" ")]
    degree_dict[node1] += 1
    degree_dict[node2] += 1
    A[node1][node2] = A[node2][node1] = 1
D = [[0, ] * n for b in range(n)]
L = list()
for j in range(n):
    D[j][j] = degree_dict[j]
    L.append([str(D[j][i] - A[j][i]) for i in range(n)])
    print(" ".join(L[j]))
