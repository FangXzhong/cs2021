for i in range(int(input())):
    num_list = [int(i) for i in input().split(" ")]
    num_sum = sum(num_list)
    if num_sum == 24 or num_sum == -24:
        print("YES")
        continue
    else:
        one_negative = [num_sum - 2 * j for j in num_list]
        if 24 in one_negative:
            print("YES")
            continue
        else:
            one_positive = [-num_sum + 2*j for j in num_list]
            if 24 in one_positive:
                print("YES")
                continue
            else:
                flag = 0
                for a in range(4):
                    if flag:
                        break
                    for b in range(a, 4):
                        if flag:
                            break
                        if num_sum - 2*num_list[a] - 2* num_list[b] == 24:
                            print("YES")
                            flag = 1
                            continue
                if not flag:
                    print("NO")

