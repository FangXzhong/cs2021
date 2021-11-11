case_num = int(input())
remember = {}
for item in range(case_num):
    n = int(input())
    if n == 1:
        a = int(input())
        b = int(input())
        print(min(a, b))
        continue
    a = [int(i) for i in input().split(" ")]
    b = [int(i) for i in input().split(" ")]
    time = [(a[i], b[i]) for i in range(n)]
    if tuple(time) in remember.keys():
        print(remember[tuple(time)])
        continue
    time.sort(key=lambda x: x[0], reverse=True)
    total = time[0][0]
    deliver_time = time[0][0]
    fetch_time = 0
    for i in range(1, len(time)):
        fetch_time += time[i - 1][1]
        if time[i][0] == deliver_time:
            continue
        temp = max(time[i][0], fetch_time)
        if temp <= total:
            total = temp
            deliver_time = time[i][0]
        else:
            break
    result = min(total, sum(b))
    print(result)
    remember[tuple(time)] = result
