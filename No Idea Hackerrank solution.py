from collections import Counter
n , m = input().split()
m = int(m)
count = 0
count2 = 0
arr = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
counter = Counter(arr)
c = sum(counter[v] for v in set(a))

counter = Counter(arr)
d = sum(counter[v] for v in set(b))
print(counter)
print(c-d)