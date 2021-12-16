stu_num = int(input().strip())
temp = [int(i) for i in input().strip().split(" ")]
costs = [(temp[i], i) for i in range(len(temp))]
costs.sort(key=lambda x: x[0])
temp.sort()
sequence = [str(costs[i][1] + 1) for i in range(len(costs))]
average_time = sum(temp[i] * (stu_num - i - 1) for i in range(len(temp))) / stu_num
print(" ".join(sequence))
print("%.2f" % average_time)
