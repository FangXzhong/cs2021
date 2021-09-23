questions_num = int(input())
my_count = 0
for i in range(questions_num):
    list1 = input().split(' ')
    if list1.count('1') >= 2:
        my_count += 1
print(my_count)
