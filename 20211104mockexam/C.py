month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for i in range(int(input())):
    start_month, start_day, start_num, end_month, end_day =[int(j) for j in input().split(" ")]
    total_day = 0
    if start_month == end_month:
        total_day = end_day - start_day
    elif end_month - start_month == 1:
        total_day = month_day[start_month] - start_day + end_day
    else:
        for m in range(start_month + 1, end_month):
            total_day += month_day[m]
        total_day += month_day[start_month] - start_day + end_day
    print(start_num * 2 ** total_day)
