n, m = [int(i) for i in input().strip().split()]
students = [int(i) for i in input().strip().split()]
students.sort()
diff = []
for i in range(1, len(students)):
    if i == 1:
        diff.append((1,students[-1] - students[1]))
    elif i == len(students) - 1:
        diff.append((i, students[-2] - students[0]))
    else:
        diff.append((i, students[-1] - students[i] + students[i - 1] - students[0]))
diff.sort(key=lambda x:x[1])
split_place = [item[0] for item in diff[:m - 1]]
split_place.sort()
result = []
if len(split_place) == 1:
    result = students[split_place[0] - 1] - students[0] +\
             students[-1] - students[split_place[0]]
else:
    result = students[split_place[0] - 1] - students[0] +\
             students[-1] - students[split_place[-1]]
    for i in range(1, len(split_place)):
        result += students[split_place[i] - 1] - students[split_place[i - 1]]
print(result)
