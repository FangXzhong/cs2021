n, a, b, c = [int(i) for i in input().split(" ")]
a, b, c = sorted([a, b, c])
x, y, z = [n // a, 0, 0]
dict1 = dict()
flag = 1
flag1 = 1
if n == a * x:
    flag = 0
while flag:
    minus_a = n - a * x
    if minus_a < b:
        x = (n - b) // a
        continue
    y = minus_a // b
    if minus_a == y * b:
        flag = 0
        break
    while y >= 0:
        minus_a_b = minus_a - b * y
        if minus_a_b < c:
            y -= 1
            continue
        if minus_a_b % c == 0:
            z = minus_a_b / c
            flag = 0
            y = max(y, 0)
            break
        else:
            y -= 1
    x -= 1 if flag else 0

temp = x + y + z
for i in range(1, int(z) + 1):
    for j in range(x):
        if (i * c + j * a) % b == 0:
            temp = max(temp, x + y + z - i - j + (i * c + j * a) / b)
print(int(temp))
