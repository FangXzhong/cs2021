n = int(input())
num_list = [int(i) for i in input().split(" ")]
ways = 0
sub_sum = sum(num_list) / 3
if sub_sum != int(sub_sum):
    print(ways)
else:
    temp_sum = 0
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            print(ways)
            quit()
        temp_sum += num_list[i]
        if temp_sum == sub_sum:
            index1 = i
            break
    temp_sum_reverse = 0
    for j in range(len(num_list) - 1, index1, -1):
        if j == index1 + 1:
            print(ways)
            quit()
        temp_sum_reverse += num_list[j]
        if temp_sum_reverse == sub_sum:
            index2 = j
            break
    if sub_sum != 0:
        zero_index_list_left = []
        temp_sum_mid = 0
        for k in range(i + 1, j + 1):
            temp_sum_mid += num_list[k]
            if temp_sum_mid == 0:
                zero_index_list_left.append(k)
        zero_index_list_right = []
        temp_sum_mid = 0
        for l in range(j - 1, i, -1):
            temp_sum_mid += num_list[l]
            if temp_sum_mid == 0:
                zero_index_list_right.append(l)
        # 不能这么简单地相乘，因为左边索引必须要小于右边的
        # print((len(zero_index_list_left)+1)*(len(zero_index_list_right)+1))

        # 改正上面的，结果超时了
        # result = 1
        # if len(zero_index_list_left) > 0:
        #     for item in zero_index_list_left:
        #         result += 2 * (sum(1 if num > item else 0 for num in zero_index_list_right) + 1)
        #     print(result)
        # else:
        #     print(len(zero_index_list_right) + 1)
        if len(zero_index_list_left)*len(zero_index_list_right) > 0:
            if zero_index_list_left[-1] >= zero_index_list_right[-1]:
                result = 1
                if len(zero_index_list_left) > 0:
                    for item in zero_index_list_left:
                        result += 2 * (sum(1 if num > item else 0 for num in zero_index_list_right) + 1)
                    print(result)
                else:
                    print(len(zero_index_list_right) + 1)
            else:
                print((len(zero_index_list_left) + 1) * (len(zero_index_list_right) + 1))
        else:
            print((len(zero_index_list_left) + 1) * (len(zero_index_list_right) + 1))
    else:
        zero_index_list = []
        temp_sum_mid = 0
        for k in range(i + 1, j):
            temp_sum_mid += num_list[k]
            if temp_sum_mid == 0:
                zero_index_list.append(k)
        print(int(len(zero_index_list)*(len(zero_index_list)+1)/2))