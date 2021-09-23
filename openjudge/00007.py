import math
item_num = int(input())
result_list = list()
for i in range(item_num):
    [x, y] = [float(item) for item in input().split(" ")]
    r = math.sqrt(x ** 2+y ** 2)
    s = math.pi * r**2 / 2
    year_num = s // 50 + 1
    result_list.append([i+1, int(year_num)])
for item in result_list:
    print("Property {}: This property will begin eroding in year {}.".format(item[0], item[1]))
print("END OF OUTPUT.")
