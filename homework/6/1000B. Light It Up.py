# n, m = [int(i) for i in input().split(" ")]
# times = [int(i) for i in input().split(" ")]
# times.extend([0, m])
# times.sort()
#
# untouched_time = 0
# for i in range(1, len(times), 2):
#     untouched_time += times[i] - times[i - 1]
#
# insert_time = 0
# if len(times) % 2 == 0:
#     flag_list = [1, 0] * (int(len(times) / 2) - 1) + [1, ]
# else:
#     flag_list = [1, 0] * int(len(times) / 2)
# for i in range(len(times)):
#     for num_checking in (times[i] - 1, times[i] + 1):
#         if num_checking in times or num_checking > times[-1] or num_checking < 0:
#             continue
#         checking_list = times.copy()
#         checking_list.append(num_checking)
#         checking_list.sort()
#         checking_flag = flag_list.copy()
#         if num_checking > times[i]:
#             if i == len(times) - 2:
#                 checking_flag.append(1 - flag_list[i])
#             else:
#                 checking_flag.insert(i + 1, 1 - flag_list[i])
#                 for k in range(i + 2, len(checking_flag)):
#                     checking_flag[k] = 1 - checking_flag[k]
#         else:
#             if i == len(times) - 1:
#                 checking_flag.append(1 - flag_list[-1])
#             else:
#                 checking_flag.insert(i, 1 - flag_list[i])
#                 for k in range(i, len(checking_flag)):
#                     checking_flag[k] = 1-checking_flag[k]
#         checking_time = sum(checking_list[j + 1] - checking_list[j] if checking_flag[j] == 1 else 0 for j in
#                             range(len(checking_list) - 1))
#         insert_time = checking_time if checking_time > insert_time else insert_time
#
# print(max(insert_time, untouched_time))


n, m = [int(i) for i in input().split(" ")]
times = [int(i) for i in input().split(" ")]
times.extend([0, m])
times.sort()

untouched_time = 0
for i in range(1, len(times), 2):
    untouched_time += times[i] - times[i - 1]

insert_time = 0
for i in range(len(times)):
    for num_checking in (times[i] - 1, times[i] + 1):
        if num_checking in times or num_checking > times[-1] or num_checking < 0:
            continue
        checking_list = times.copy()
        checking_list.append(num_checking)
        checking_list.sort()
        temp = 0
        for j in range(1, len(checking_list), 2):
            temp += checking_list[j] - checking_list[j - 1]
        insert_time = temp if temp > insert_time else insert_time
print(max(insert_time, untouched_time))
