num = int(input())
result = 0
for i in range(1, num + 1):
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        continue
    else:
        result += i ** 2
print(result)
