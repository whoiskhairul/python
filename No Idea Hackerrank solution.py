from collections import Counter
n , m = input().split()

arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

counter = Counter(arr)
c = sum(counter[v] for v in a)

counter = Counter(arr)
d = sum(counter[v] for v in b)

print(c-d)
