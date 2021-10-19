dict1 = dict()
num = int(input())
num_list = [int(i) for i in input().split(" ")]
for item in num_list:
    if item in dict1.keys():
        print(dict1[item])
        continue
    if item == 4:
        print("YES")
        continue
    if item == 1:
        print("NO")
        continue
    sqr_num = int(item**0.5)
    if sqr_num ** 2 == item:
        flag = 1
        for j in range(2, int(sqr_num**0.5)+2):
            if (sqr_num % j) == 0:
                print("NO")
                dict1[item] = "NO"
                flag = 0
                break
        if flag:
            print("YES")
            dict1[item] = "YES"
    else:
        print("NO")
