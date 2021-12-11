def in_field(a, b, n, m):
    return 0 <= a <= n - 1 and 0 <= b <= m - 1


def jump(n, m , x, y, steps, went):
    if steps == n * m:
        global count
        count += 1
        return
    tar = [(x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2), (x + 1, y + 2), (x + 2, y + 1),
           (x + 2, y - 1), (x + 1, y - 2)]
    for place in tar:
        if place not in went and in_field(place[0], place[1], n, m):
            jump(n, m, place[0], place[1], steps + 1, went + [(x, y), ])


cases = int(input().strip())
for item in range(cases):
    count = 0
    n, m, x, y = [int(i) for i in input().strip().split(" ")]
    jump(n, m, x, y, 1, [])
    print(count)
