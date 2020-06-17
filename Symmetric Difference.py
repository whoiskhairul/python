n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
temp = list(a.difference(b))
temp = temp+ list(b.difference(a))
temp.sort()
for _ in range(len(temp)):
    print(temp[_])