for i in range(int(input())):
    angle = int(input())
    if 360 % (180-angle) == 0:
        print("YES")
    else:
        print("NO")
