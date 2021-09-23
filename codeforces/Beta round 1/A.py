a, b, c = [int(i) for i in input().split(" ")]
num1 = a // c if a % c == 0 else a // c + 1
num2 = b // c if b % c == 0 else b // c + 1
print(num1 * num2)
