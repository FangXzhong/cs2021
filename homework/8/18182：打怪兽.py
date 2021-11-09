case_num = int(input())
for item in range(case_num):
    n, m, b = [int(i) for i in input().split(" ")]
    skills = dict()
    for skill in range(n):
        time, xi = [int(j) for j in input().split(" ")]
        if time not in skills.keys():
            skills[time] = []
            skills[time].append(xi)
        else:
            skills[time].append(xi)
    hurt = 0
    flag = 1
    for t in sorted(skills.keys()):
        skills[t].sort(reverse=True)
        hurt += sum(skills[t][0: min(len(skills[t])+1, m)])
        if hurt >= b:
            print(t)
            flag = 0
            break
    if flag:
        print("alive")

