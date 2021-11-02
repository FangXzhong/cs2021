number = int(input())
result = "I hate "
flag = True
while number > 1:
    if flag:
        result += "that I love "
    else:
        result += "that I hate "
    number -= 1
    flag = 1 - flag
print(result + "it")
