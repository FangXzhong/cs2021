num = int(input())
result = 0
for i in range(num):
    statement = input()
    if statement.count("1") >= 2:
        result += 1
print(result)
