for i in range(int(input())):
    flag = 0
    num = int(input())
    numbers = [int(i) for i in input().split(" ")]
    if 2048 in numbers:
        print("YES")
        continue
    max_label = max(numbers, key=numbers.count)
    while numbers.count(max_label) > 1:
        numbers.remove(max_label)
        numbers.remove(max_label)
        numbers.append(max_label * 2)
        if 2048 in numbers:
            flag = 1
            break
        max_label = max(numbers, key=numbers.count)
    if flag:
        print("YES")
    else:
        print("NO")
