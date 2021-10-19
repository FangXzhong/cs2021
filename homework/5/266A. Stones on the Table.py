stone_num = input()
s = input()
print(sum(1 if s[i] == s[i-1] else 0 for i in range(1, len(s))))
