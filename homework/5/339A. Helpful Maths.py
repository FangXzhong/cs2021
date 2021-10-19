s = [int(i) for i in input().replace("+", " ").split(" ")]
a = [str(i) for i in sorted(s)]
print("+".join(a))
