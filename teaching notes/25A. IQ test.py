num = int(input())
numbers = [int(i) % 2 for i in input().split(" ")]
if sum(numbers) == 1:
    print(numbers.index(1)+1)
else:
    print(numbers.index(0)+1)
