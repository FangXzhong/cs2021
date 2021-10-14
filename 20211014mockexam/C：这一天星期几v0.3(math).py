"""
    根据提示做就行。
    不过最关键的是，当是1月或2月的时候，y一定得减一，（这也是为什么y有可能等于-1）
    我自己做的时候忽略了y等于-1的情况
"""
day_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
for i in range(int(input())):
    date = input()
    c, y, m, d = (int(date[x:x + 2]) for x in range(0, 8, 2))
    if m < 3:
        m += 12
        if y > 0:
            y -= 1
        else:
            y = 99
            c -= 1
    w = (y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10 + d - 1) % 7
    print(day_dict[w])
