n,d = input().split()
n = int(n)
d = int(d)
a = list(map(int,input().split()))

for i in range(0,d):
    a.append(a[i])
for i in range(0,d):
    a.pop(0)
for i in range(0,n):
    print(a[i] , end=' ')
