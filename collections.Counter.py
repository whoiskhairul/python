from collections import Counter

x = int(input())
shoe = list(map(int, input().split()))
c = Counter(shoe)
count = 0

n = int(input())
for i in range(n):
    size, price = input().split()
    size = int(size)
    price = int(price)
    if (c[size] > 0):
        c[size] -= 1
        count += price
print(count)
