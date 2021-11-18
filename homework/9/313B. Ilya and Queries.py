s = input()
processed = {}
list1 = [0, ] * len(s)
if s[0] == s[1]:
    list1[0] = 1
for i in range(1, len(s) - 1):
    if s[i] == s[i + 1]:
        list1[i] = list1[i - 1] + 1
    else:
        list1[i] = list1[i - 1]
for i in range(int(input())):
    a, b = [int(j) for j in input().split(" ")]
    if a > 1:
        print(list1[b - 2] - list1[a - 2])
    else:
        print(list1[b - 2])
