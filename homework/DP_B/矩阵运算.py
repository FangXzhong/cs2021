row_a, col_a = [int(i) for i in input().strip().split(" ")]
a = []
for line in range(row_a):
    a.append([int(i) for i in input().strip().split(" ")])
row_b, col_b = [int(i) for i in input().strip().split(" ")]
b = []
for line in range(row_b):
    b.append([int(i) for i in input().strip().split(" ")])
row_c, col_c = [int(i) for i in input().strip().split(" ")]
c = []
for line in range(row_c):
    c.append([int(i) for i in input().strip().split(" ")])
if row_a == row_c and col_b == col_c and col_a == row_b:
    temp = []
    for i in range(row_a):
        temp.append([sum(a[i][k]*b[k][j] for k in range(col_a)) for j in range(col_b)])
    result = []
    for i in range(row_c):
        result.append([str(temp[i][j] + c[i][j]) for j in range(col_c)])
        print(" ".join(result[-1]))
else:
    print("Error!")
