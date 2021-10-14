num = int(input())
num_list = [int(i) % 2 for i in input().split(" ")]
print(num_list.index(1)+1) if sum(num_list) == 1 else print(num_list.index(0)+1)
