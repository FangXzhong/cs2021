# 这道题我整了半天，最后发现只要能被幸运数整除的就行，而不只是4和7

number = int(input())
if number % 4 == 0 or number % 7 == 0 or number % 47 == 0 or number % 74 == 0 or number % 447 == 0 or number % 474 == 0 \
        or number % 477 == 0 or number % 774 == 0 or number % 747 == 0:
    print("YES")
elif sum(0 if item in '47' else 1 for item in str(number)) == 0:
    print("YES")
else:
    print("NO")
