a = input().lower()
vowels = "aoyeui"
b = ''
for item in a:
    if item not in vowels:
        b += item
print("." + ".".join(list(b)))
