def can_reach(base_index, tar_index, floors):
    back = [True, True]
    if floors[tar_index][0] <= floors[base_index][0] <= floors[tar_index][1]:
        for item in range(tar_index, base_index):
            if item == base_index - 1:
                continue
            if floors[item][0] <= floors[base_index][0] <= floors[item][1]:
                back[0] = False
            if floors[item][0] <= floors[base_index][1] <= floors[item][1]:
                back[1] = False
    else:
        back[0] = False
    if not floors[tar_index][0] <= floors[base_index][1] <= floors[tar_index][1]:
        back[1] = False
    return back


def reach_start(x_pos, floor_index, floor_list):
    flag = True
    if floor_list[floor_index][0] <= x_pos <= floor_list[floor_index][1]:
        for item in range(floor_index, len(floor_list)):
            if item == len(floor_list) - 1:
                continue
            if floors[item][0] <= x_pos <= floors[item][1]:
                flag = False
    else:
        flag = False
    return flag


case_num = int(input().strip())
for case in range(case_num):
    n, x, y, max_height = [int(i) for i in input().strip().split()]
    floors = []
    for floor in range(n):
        floors.append([int(i) for i in input().strip().split()])
        if floors[-1][2] > y:
            floors.pop(-1)
    result = [(0, 0), ]
    floors.sort(key=lambda tar: tar[2])
    for i in range(1, len(floors)):
        temp_left = float("inf")
        temp_right = float("inf")

        if floors[i][2] <= max_height:
            flag_l = 0
            flag_r = 0
            for j in range(i):
                if floors[j][0] <= floors[i][0] <= floors[j][1]:
                    flag_l = 1
                if floors[j][0] <= floors[i][1] <= floors[j][1]:
                    flag_r = 1
            if flag_l == 0:
                temp_left = 0
            if flag_r == 0:
                temp_right = 0

        for j in range(i):
            if floors[i][2] - floors[j][2] <= max_height:
                have_left, have_right = can_reach(i, j, floors)
                if have_left:
                    temp_left = min(abs(floors[i][0] - floors[j][0]) + result[j][0],
                                    abs(floors[i][0] - floors[j][1]) + result[j][1],
                                    temp_left)
                if have_right:
                    temp_right = min(abs(floors[i][1] - floors[j][0]) + result[j][0],
                                     abs(floors[i][1] - floors[j][1]) + result[j][1],
                                     temp_right)
        if temp_left == float("inf"):
            temp_left = 0
        if temp_right == float("inf"):
            temp_right = 0
        result.append((temp_left, temp_right))
    temp = float("inf")
    for i in range(len(floors)):
        if y - floors[i][2] <= max_height and reach_start(x, i, floors):
            temp = min(abs(x - floors[i][0]) + result[i][0],
                       abs(x - floors[i][1]) + result[i][1],
                       temp)
    if temp == float("inf"):
        temp = 0
    print(int(y + temp))
