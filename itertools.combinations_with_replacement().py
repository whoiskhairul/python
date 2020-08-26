from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)
s = list(s)
s.sort()

arr = []
x = list(combinations_with_replacement(s, k))
for j in range(len(x)):
    arr.append(''.join(x[j]))
arr.sort()
for i in arr:
    print(i)
