a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_count, b_count = 0, 0
for i in range(len(a)):
    if a[i] > b[i]:
        a_count += 1
    elif b[i] > a[i]:
        b_count += 1
print(a_count, b_count)
