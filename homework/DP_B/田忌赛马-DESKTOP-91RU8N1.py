while True:
    horse_num = int(input().strip())
    if horse_num == 0:
        break
    tian = [int(i) for i in input().strip().split(" ")]
    king = [int(i) for i in input().strip().split(" ")]
    tian.sort(reverse=True)
    king.sort(reverse=True)
    result = 0
    for i in range(horse_num):
        if tian[0] > king[0]:
            tian.pop(0)
            king.pop(0)
            result += 200
        elif tian[-1] > king[-1]:
            tian.pop(-1)
            king.pop(-1)
            result += 200
        else:
            if tian[-1] < king[0]:
                result -= 200
                tian.pop(-1)
                king.pop(0)
    print(result)
