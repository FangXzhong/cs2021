mice = list()
for i in range(int(input())):
    mice.append([item for item in input().split(" ")])
    mice[i][0] = int(mice[i][0])
mice.sort(key=lambda x: x[0], reverse=True)
for mouse in mice:
    print(mouse[1])
