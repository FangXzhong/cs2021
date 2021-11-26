m, n = (int(i) for i in input().split());
ids = [];
for i in range(m):
    ids.append([int(i) for i in input().split()]);
results = [None for i in range(m * n)];
scores = {};
for i in range(m * n):
    results[i] = [int(i) for i in input().split()];
    s = sum(results[i]);
    if s in scores:
        scores[s] += 1;
    else:
        scores[s] = 1;
count = 0;
maxCount = m * n * 0.4;
for i in sorted(scores.keys(), reverse=True):
    if (count + scores[i]) > maxCount:
        break;
    else:
        count += scores[i];
same = [False for i in range(m * n)];
for i in range(m):
    for j in range(n - 1):
        if (results[ids[i][j]] == results[ids[i][j + 1]]):
            same[ids[i][j]] = True;
            same[ids[i][j + 1]] = True;
for i in range(m - 1):
    for j in range(n):
        if (results[ids[i][j]] == results[ids[i + 1][j]]):
            same[ids[i][j]] = True;
            same[ids[i + 1][j]] = True;
print(same.count(True), count);
