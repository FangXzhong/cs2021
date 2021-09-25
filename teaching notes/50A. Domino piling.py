m, n = [int(i) for i in input().split(" ")]
print(int(m*n/2) if m*n % 2 == 0 else int((m*n-1)/2))
