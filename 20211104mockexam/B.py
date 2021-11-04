str = input()
result = ""
for s in str:
    if "a" <= s <= "z":
        result += s.upper()
    elif "A" <= s <= "Z":
        result += s.lower()
    else:
        result += s
print(result)
