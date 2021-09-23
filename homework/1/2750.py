feet = int(input())
if feet % 2 != 0:
    print('0 0')
else:
    max_num = feet / 2
    if feet % 4 == 0:
        min_num = feet / 4
    else:
        min_num = (feet - 2) / 4 + 1
    print(str(int(min_num)) + " " + str(int(max_num)))
