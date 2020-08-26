n = int(input())
ar = list(map(int, input().rstrip().split()))
a = []
sum = 0
a = list(dict.fromkeys(ar))
for i in range(len(a)):
    b = ar.count(a[i]) // 2
    sum = sum + b
print(sum)
