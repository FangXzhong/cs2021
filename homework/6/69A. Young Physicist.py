list1 = [0, 0, 0]
for i in range(int(input())):
    force = input().split(" ")
    list1[0] += int(force[0])
    list1[1] += int(force[1])
    list1[2] += int(force[2])
if list1 == [0, 0, 0]:
    print("YES")
else:
    print("NO")

