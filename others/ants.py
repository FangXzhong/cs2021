n = int(input())
for i in range(n):
    l,num = map(int,input().split())
    t = []
    location = list(map(int,input().split()))
    for j in range(num):
        s_min = min(location[j],l-location[j])
        t.append(s_min)
    t_min = max(t)
    t_max = max(max(location),l-min(location))
    print(t_min,t_max)
