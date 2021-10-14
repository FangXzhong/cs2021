for i in range(int(input())):
    num = int(input())
    if num == 1:
        print(0)
        continue
    two_num = 0
    three_num = 0
    while num % 2 == 0:
        num /= 2
        two_num += 1
    while num % 3 == 0:
        num /= 3
        three_num += 1
    if int(num) != 1 or two_num > three_num:
        print(-1)
        continue
    else:
        print(2 * three_num - two_num)
