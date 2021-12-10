place = []
max_index = []
result = []
for line in range(5):
    # place.append([int(i) for i in input().split(" ")])
    temp = input().strip().split(" ")
    temp1 = []
    for i in range(len(temp)):
        temp[i] = temp[i].strip()
        if temp[i].isdigit():
            temp1.append(temp[i])
    place.append([int(num) for num in temp1])
    max_index.append(place[-1].index(max(place[-1])))
for i in range(len(max_index)):
    if place[i][max_index[i]] == min([place[line][max_index[i]] for line in range(len(place))]):
        result.append((str(i + 1), str(max_index[i] + 1), str(place[i][max_index[i]])))
if not result:
    print("not found")
else:
    print(" ".join(result[0]))
