n, l = [int(i) for i in input().split(" ")]
places = [int(i) for i in input().split(" ")]
places.sort()
if n == 1:
    print(max(l - places[-1], places[0]))
else:
    print(max(max((places[i] - places[i - 1])/2 for i in range(1, n)), l - places[-1], places[0]))
