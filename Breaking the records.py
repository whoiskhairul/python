
_, arr =input(), list(map(int, input().split()))
l, h, lc, hc = arr[0], arr[0], 0, 0

for i in range(1,len(arr)):
    if arr[i]<l:
        lc+=1
        l = arr[i]
    elif arr[i]>h:
        hc+=1
        h = arr[i]
print(hc, lc)