result = []


def queen(A, cur=0):
    if cur == len(A):
        global result
        result.append(tuple(A))
        return 0
    for col in range(len(A)):
        A[cur] = col
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                break
        else:
            queen(A, cur + 1)


queen([None, ] * 8)
for i in range(len(result)):
    print("No. {}".format(i + 1))
    temp = [["0" for a in range(8)] for b in range(8)]
    j = 0
    for item in result[i]:
        temp[item][j] = '1'
        j += 1
    for line in temp:
        print(" ".join(line))
