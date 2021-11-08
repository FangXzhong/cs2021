while True:
    monkey_num, kick_num = [int(i) for i in input().split(" ")]
    if monkey_num == kick_num == 0:
        break
    call = 1  # 报数，报到几号就是几号
    kicked_num = 0  # 被踢出的猴子的数量
    index_flag = 1  # 当前要报数的猴子的序号
    result_dict = dict(zip(range(1, monkey_num + 1), [1, ] * monkey_num))
    while kicked_num < monkey_num - 1:
        if result_dict[index_flag] == 0:  # 如果这个猴子已经被踢出了，下一个
            index_flag += 1
            if index_flag == monkey_num + 1:  # 超出总数就从头开始
                index_flag = 1
            continue
        if call == kick_num:
            "当满足踢出条件时"
            result_dict[index_flag] = 0
            call = 0
            kicked_num += 1
        index_flag += 1
        call += 1
        if index_flag == monkey_num + 1:
            index_flag = 1
    for id, symbol in result_dict.items():
        if symbol == 1:
            print(id)
            break
