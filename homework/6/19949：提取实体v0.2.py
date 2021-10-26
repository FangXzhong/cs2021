sentences = list()
# tar = set()
result = 0
for i in range(int(input())):
    sentences.append(input())

flag = 0  # 这个变量用来指示连续的主体所包含的单词索引终止位置
for item in sentences:
    skip_time = 0  # 如果一个主体包含了多个单词，那么就需要跳过后续所有的单个单词
    item_split = item.split(' ')
    for j in range(len(item_split)):
        if skip_time > 0:
            skip_time -= 1
            continue
        if item_split[j][:3] == item_split[j][-3:] == "###":
            flag = j
            while item_split[flag][:3] == "###":
                flag += 1
            temp = " ".join(item_split[k][3:-3] for k in range(j, flag + 1))
            # tar.add(temp)
            result += 1
            skip_time = flag - j
print(result)
