from collections import Counter
from itertools import combinations

s, k = input().split()
k = int(k)
c = Counter(s)
s = list(c.elements())
s.sort()

for i in range(1, k + 1):
    arr = []
    x = list(combinations(s, i))
    for j in range(len(x)):
        arr.append(''.join(x[j]))

    for i in arr:
        print(i)
