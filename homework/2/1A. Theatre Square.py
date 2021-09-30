import math
a, b, c = [int(i) for i in input().split(" ")]
print(math.ceil(a/c)*math.ceil(b/c))
