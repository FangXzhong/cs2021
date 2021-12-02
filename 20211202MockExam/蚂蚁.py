cases = int(input().strip())
for case in range(cases):
    length, n = [int(i) for i in input().strip().split(" ")]
    places = [int(i) for i in input().strip().split(" ")]
    places.sort()
    result = [0, 0]
    shortest = [min(item, length - item) for item in places]
    result[0] = str(max(shortest))
    longest = [max(item, length - item) for item in places]
    result[1] = str(max(longest))
    print(" ".join(result))
