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
    tian_quick = 0
    tian_slow = horse_num - 1
    king_quick = 0
    king_slow = horse_num - 1
    raced = 0
    result = 0
    while True:
        if raced == horse_num:
            break
        if tian[tian_quick] > king[king_quick]:
            result += 200
            tian_quick += 1
            king_quick += 1
            raced += 1
        elif tian[tian_quick] < king[king_quick]:
            result -= 200
            tian_slow -= 1
            king_quick += 1
            raced += 1
        else:
            if tian[tian_slow] > king[king_slow]:
                tian_quick += 1
                king_quick += 1
                tian_slow -= 1
                king_slow -= 1
                raced += 1
                result += 200
                continue
            if tian[tian_slow] < king[king_quick]:
                king_quick += 1
                tian_slow -= 1
                raced += 1
                result -= 200
            else:
                king_quick += 1
                tian_slow -= 1
                raced += 1

    print(result)
