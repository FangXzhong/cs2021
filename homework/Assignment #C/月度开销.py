def check(up, num_list, max_period):
    temp = 0
    total = 0
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            if temp == 0:
                total += 1
            else:
                total += 1
        else:
            temp += num_list[i]
            if temp + num_list[i + 1] > up:
                temp = 0
                total += 1
    return True if total <= max_period else False


def find(left, right, costs, max_period):
    if left == right:
        print(int(left))
        return 0
    elif left + 1 == right:
        if check(left, costs, max_period):
            print(left)
            return 0
        else:
            print(right)
            return 0
    if check((left + right) // 2, costs, max_period):
        find(left, (left + right) // 2, costs, max_period)
    else:
        find((left + right) // 2, right, costs, max_period)


n, m = [int(i) for i in input().split()]
costs = []
for day in range(n):
    costs.append(int(input().strip()))
find(max(costs), sum(costs), costs, m)
