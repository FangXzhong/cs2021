# x = 0
# state_num = int(input())
# for i in range(state_num):
#     statement = input()
#     if statement[1] == "+":
#         x += 1
#     else:
#         x -= 1
# print(x)

print(sum(1 if input()[1] == "+" else -1 for statement in range(int(input()))))
