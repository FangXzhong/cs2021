case_num = int(input())
for item in range(case_num):
    num = int(input())
    rank = 1
    i = 1
    while True:
        if i % 3 == 0 or i % 10 == 3:
            i += 1
            continue
        if rank == num:
            print(i)
            break
        i += 1
        rank += 1


