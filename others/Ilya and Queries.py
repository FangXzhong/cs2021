raw = input()
result = [0, ] * (len(raw))
for i in range(len(raw) - 1):
    if raw[i] == raw[i + 1]:
        result[i] = 1
for i in range(1, len(result) - 1):
    result[i] += result[i - 1]
out = []
for item in range(int(input())):
    start, end = [int(i) for i in input().split()]
    out.append(str(result[end - 2] - result[start - 2]))
print("\n".join(out))
