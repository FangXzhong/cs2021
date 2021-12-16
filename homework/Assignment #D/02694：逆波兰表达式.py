def calculate(flag, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if flag == "+":
        return num1 + num2
    elif flag == "-":
        return num1 - num2
    elif flag == "*":
        return num1 * num2
    elif flag == "/":
        return num1 / num2


def deal(raw_index):
    global flags
    flag = raw[raw_index]
    raw_index += 1
    if raw[raw_index] in flags:
        num1, raw_index = deal(raw_index)
    else:
        num1 = raw[raw_index]
    raw_index += 1
    if raw[raw_index] in flags:
        num2, raw_index = deal(raw_index)
    else:
        num2 = raw[raw_index]
    return calculate(flag, num1, num2), raw_index


raw = input().strip().split(" ")
flags = ["+", "-", "*", "/"]
flag_list = []
temp_num = []
print("%.6f" % deal(0)[0])
