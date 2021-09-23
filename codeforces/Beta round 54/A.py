s = input()
target = 'hello'
result = list()
i = 0
for word in s:
    if i == 5:
        break
    if word == target[i]:
        result.append(1)
        i += 1
if len(result) == 5:
    print("YES")
else:
    print("NO")
