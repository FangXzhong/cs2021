# import numpy as np
# m, n, p, q = [int(i) for i in input().split(" ")]
# matrix = []
# for item in range(m):
#     matrix.append([int(i) for i in input().split(" ")])
# core = []
# for item in range(p):
#     core.append([int(i) for i in input().split(" ")])
# np_matrix = np.array(matrix)
# np_core = np.array(core)
# result = []
# for a in range(m+1-p):
#     result.append([str(np.sum(np_matrix[a:a+p, b:b+q]*np_core)) for b in range(n+1-q)])
#     print(" ".join(result[a]))

m, n, p, q = [int(i) for i in input().split(" ")]
matrix = []
for item in range(m):
    matrix.append([int(i) for i in input().split(" ")])
core = []
for item in range(p):
    core.append([int(i) for i in input().split(" ")])
result = []
for a in range(m+1-p):
    result.append([str(sum(matrix[a+x][b+y]*core[x][y] for x in range(p) for y in range(q))) for b in range(n+1-q)])
    print(" ".join(result[a]))
