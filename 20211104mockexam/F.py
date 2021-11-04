while True:
    monkey_num, kick_num = [int(i) for i in input().split(" ")]
    if monkey_num == kick_num == 0:
        break
    call = 1
    kicked_num = 0
    index_flag = 1
    result_dict = dict(zip(range(1, monkey_num + 1), [1, ] * monkey_num))
    while kicked_num < monkey_num - 1:
        if result_dict[index_flag] == 0:
            index_flag += 1
            if index_flag == monkey_num + 1:
                index_flag = 1
            continue
        if call == kick_num:
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
