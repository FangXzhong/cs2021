s = input()
if len(s) < 7:
    print("NO")
    quit()
for i in range(7, len(s)+1):
    if s[i-7] == s[i-1] == s[i-2]==s[i-3]==s[i-4]==s[i-5]==s[i-6]:
        print("YES")
        quit()
print("NO")
