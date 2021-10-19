buttons_num, bulbs_num = [int(i) for i in input().split(" ")]
buttons_checked = set()
bulb_set = set()
for i in range(buttons_num):
    statement = [int(i) for i in input().split(" ")]
    if statement[0] not in buttons_checked:
        for j in range(1, len(statement)):
            bulb_set.add(statement[j])
print("YES" if len(bulb_set) == bulbs_num else "NO ")
