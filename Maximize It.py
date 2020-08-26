k, m = list(map(int, input().split()))
res = 0
for i in range(k):
    arr = list(map(int, input().split()))
    res = res + max(arr) ** 2
print(res)
print(res % m)
