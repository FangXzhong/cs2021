while True:
    horse_num = int(input().strip())
    if horse_num == 0:
        break
    tian = [int(i) for i in input().strip().split(" ")]
    king = [int(i) for i in input().strip().split(" ")]
    tian.sort(reverse=True)
    king.sort(reverse=True)
    if tian == king:
        print(0)
        continue

