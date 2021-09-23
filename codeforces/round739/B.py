case_num = int(input())
for item in range(case_num):
    a, b, c = [int(number) for number in input().split(' ')]
    total_num = 2 * abs(a - b)
    d1 = c + abs(a - b)
    d2 = c - abs(a - b)
    if d1 < total_num:
        pass
