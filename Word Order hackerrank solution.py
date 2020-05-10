from collections import Counter
n = int(input())
a = []
for i in range(n):
    a.append(input())
c = Counter(a)
a = list(dict.fromkeys(a))
print(len(a))
for i in range(len(a)):
    print(c[a[i]],end=' ')
