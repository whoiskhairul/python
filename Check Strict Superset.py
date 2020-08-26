count, a, n = 0, set(map(str, input().split())), int(input())
for i in range(n):
    b = set(map(str, input().split()))
    if not a.issuperset(b):
        count += 1
if count:
    print('False')
else:
    print('True')
