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
case_num = int(input().strip())
for item in range(case_num):
    n = int(input().strip())
    print("".join(str(i+1) for i in result[n - 1]))
