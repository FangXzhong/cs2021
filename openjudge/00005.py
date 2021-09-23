flag = 1
while flag:
    num = float(input().strip())
    if num == 0:
        break
    sum = 1/2
    i = 1
    while sum < num:
        sum += 1 / (i+2)
        i += 1
    print(str(i)+" card(s)")
