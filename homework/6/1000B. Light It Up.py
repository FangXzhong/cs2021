n, m = [int(i) for i in input().split(" ")]
times = [int(i) for i in input().split(" ")]
times.extend([0, m])
times.sort()
insert_times = times.copy()

untouched_time = 0
for i in range(1, len(times), 2):
    untouched_time += times[i] - times[i - 1]
# print(untouched_time)

insert_time = 0
insert_times.sort()
flag = 0
for i in range(len(insert_times)):
    if i == len(insert_times) - 1:
        flag = 0
    else:
        flag = 1 - flag
    if flag:
        insert_time += insert_times[i + 1] - insert_times[i]
print(max(insert_time, untouched_time))
