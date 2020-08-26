import math

n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)

    x = int(math.sqrt(a))
    y = int(math.sqrt(b))

    if (a == x * x):
        print(y - x + 1)
    else:
        print(y - x)
