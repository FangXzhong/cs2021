n, max_w = [int(i) for i in input().strip().split(" ")]
gift_list = list()
for case in range(n):
    v, w = [int(i) for i in input().strip().split(" ")]
    value_per_height = v / w
    gift_list.append([v, w, value_per_height])
gift_list.sort(key=lambda x: x[-1], reverse=True)
if max_w > sum([item[1] for item in gift_list]):
    print("%.1f" % sum([item[0] for item in gift_list]))
elif max_w < gift_list[0][1]:
    print("%.1f" % max_w * gift_list[0][2])
else:
    temp_sum = 0
    for i in range(n):
        temp_sum += gift_list[i][1]
        if temp_sum <= max_w < temp_sum + gift_list[i + 1][1]:
            result = sum([item[0] for item in gift_list[:i + 1]]) + (max_w - temp_sum) * gift_list[i + 1][2]
            print("%.1f" % result)
            break
